from functools import partial
from typing import Union

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout
from qfluentwidgets import ComboBox, SwitchButton, PushButton, LineEdit

from core.utils import delay
from gui.util import notification
from gui.util.config_set import ConfigSet


class ConfigItem:
    label: str
    key: Union[str, None]
    selection: Union[list[str], bool, str, list[int], callable, None]
    type: str

    def __init__(self, **kwargs):
        self.label = kwargs.get('label')
        self.key = kwargs.get('key')
        self.selection = kwargs.get('selection')
        self.type = kwargs.get('type')


class TemplateLayout(QWidget):
    patch_signal = pyqtSignal(str)

    def __init__(self, configItems: Union[list[ConfigItem], list[dict]], parent=None, config=None):
        super().__init__(parent=parent)
        self.config = config
        if isinstance(configItems[0], dict):
            _configItems = []
            for item in configItems:
                assert isinstance(item, dict)
                _configItems.append(ConfigItem(**item))
            configItems = _configItems

        self.vBoxLayout = QVBoxLayout(self)
        self.vBoxLayout.addSpacing(16)
        self.vBoxLayout.setAlignment(Qt.AlignCenter)

        for ind, cfg in enumerate(configItems):
            confirmButton = None
            selectButton = None
            optionPanel = QHBoxLayout(self)
            labelComponent = QLabel(cfg.label, self)
            optionPanel.addWidget(labelComponent, 0, Qt.AlignLeft)
            optionPanel.addStretch(1)
            if cfg.type == 'switch':
                currentKey = cfg.key
                inputComponent = SwitchButton(self)
                inputComponent.setChecked(self.config.get(currentKey))
                inputComponent.checkedChanged.connect(partial(self._commit, currentKey, inputComponent, labelComponent))
            elif cfg.type == 'combo':
                currentKey = cfg.key
                inputComponent = ComboBox(self)
                inputComponent.addItems(cfg.selection)
                inputComponent.setCurrentIndex(cfg.selection.index(self.config.get(currentKey)))
                inputComponent.currentIndexChanged.connect(
                    partial(self._commit, currentKey, inputComponent, labelComponent))
            elif cfg.type == 'button':
                inputComponent = PushButton('执行', self)
                inputComponent.clicked.connect(cfg.selection)
            elif cfg.type == 'text':
                currentKey = cfg.key
                inputComponent = LineEdit(self)
                inputComponent.setText(str(self.config.get(currentKey)))
                self.patch_signal.connect(inputComponent.setText)
                confirmButton = PushButton('确定', self)
                confirmButton.clicked.connect(partial(self._commit, currentKey, inputComponent, labelComponent))
            elif cfg.type == 'label':
                inputComponent = QLabel(cfg.selection, self)

            else:
                raise ValueError(f'Unknown config type: {cfg.type}')
            optionPanel.addWidget(inputComponent, 0, Qt.AlignRight)
            if selectButton is not None:
                optionPanel.addWidget(selectButton, 0, Qt.AlignRight)
            if confirmButton is not None:
                optionPanel.addWidget(confirmButton, 0, Qt.AlignRight)
            self.vBoxLayout.addLayout(optionPanel)
            self.vBoxLayout.setContentsMargins(20, 0, 20, 20)

    def _commit(self, key, target, labelTarget):
        value = None
        if isinstance(target, ComboBox):
            value = target.currentText()
        elif isinstance(target, SwitchButton):
            value = target.isChecked()
        elif isinstance(target, LineEdit):
            value = target.text()
        assert value is not None
        self.config.update(key, value)
        notification.success('设置成功', f'{labelTarget.text()}已经被设置为：{value}', self.config)


class ConfigItemV2(ConfigItem):
    label: str
    key: str
    dataType: str

    def __init__(self, **kwargs):
        self.label = kwargs.get('label')
        self.key = kwargs.get('key')
        self.dataType = kwargs.get('dataType', 'str')


class ComboBoxCustom(ComboBox):
    def __init__(self, parent=None, inputComponent: LineEdit = None, key: str = None, config=None, mapping=None):
        super().__init__(parent=parent)
        self.itemsLabels = []
        self.inputComponent = inputComponent
        self.config = config
        self.key = key
        self.mapping = mapping
        self.items = []

    def _onItemClicked(self, index):
        self.setCurrentIndex(index)
        if self.inputComponent:
            value = eval(self.inputComponent.text())
            if self.itemsLabels[index][0] in value:
                return
            value.append(self.itemsLabels[index][0])
            self.inputComponent.blockSignals(True)
            self.inputComponent.setText(str(value))
            self.inputComponent.blockSignals(False)
            _value = []
            for item in value:
                _value.append(self.mapping[item])
            self.config[self.key] = _value

    def addItems(self, texts: list[list[str]]):
        self.itemsLabels = texts
        for text in texts:
            self.addItem(text[0])


class TemplateLayoutV2(QWidget):
    def __init__(self, configItems: list[dict], parent=None, config=None, all_label_list: list = None, cs: ConfigSet=None):
        super().__init__(parent=parent)

        _all_label_list = []
        # event => func
        self.mapping = {}
        # func => event
        self.mapping_v2 = {}
        for label in all_label_list:
            if config['event_name'] == label[0]:
                continue
            _all_label_list.append(label)
            self.mapping[label[1]] = label[0]
            self.mapping_v2[label[0]] = label[1]
        all_label_list = _all_label_list
        del _all_label_list

        self.config = config
        self.cs = cs
        self.vBoxLayout = QVBoxLayout(self)
        self.vBoxLayout.addSpacing(16)
        self.vBoxLayout.setAlignment(Qt.AlignCenter)
        self.setMinimumWidth(400)
        self.setStyleSheet('''
            QLabel {
                font-size: 16px;
                font-family: "Microsoft YaHei";
            }
        ''')

        self.cfs = []

        for ind, cfg in enumerate(configItems):
            optionPanel = QHBoxLayout(self)
            cfg = ConfigItemV2(**cfg)
            self.cfs.append(cfg)
            labelComponent = QLabel(cfg.label, self)
            optionPanel.addWidget(labelComponent, 0, Qt.AlignLeft)
            optionPanel.addStretch(1)
            currentKey = cfg.key
            inputComponent = LineEdit(self)
            inputComponent.setMinimumWidth(200)
            if currentKey == 'pre_task' or currentKey == 'post_task':
                inputComponent.setText(self.parseToDisplay(self.config.get(currentKey)))
            else:
                inputComponent.setText(str(self.config.get(currentKey)))
            inputComponent.textChanged.connect(partial(self._commit, currentKey, inputComponent))
            optionPanel.addWidget(inputComponent, 0, Qt.AlignRight)
            if currentKey == 'pre_task' or currentKey == 'post_task':
                comboTip = ComboBoxCustom(self, inputComponent, currentKey, self.config, self.mapping_v2)
                comboTip.addItems([x for x in all_label_list])
                optionPanel.addWidget(comboTip, 0, Qt.AlignRight)
            self.vBoxLayout.addLayout(optionPanel)
            self.vBoxLayout.addSpacing(8)
            self.vBoxLayout.setContentsMargins(20, 0, 20, 20)

    def parseToDisplay(self, list_data):
        _res = []
        for item in list_data:
            _res.append(self.mapping[item])
        return str(_res)

    @delay(0.8)
    def _commit(self, key, target, *args):
        value = target.text()
        try:
            for cf in self.cfs:
                if cf.key == key:
                    if key == 'pre_task' or key == 'post_task':
                        value = eval(value)
                        value = list(map(lambda x: self.mapping_v2[x], value))
                    elif cf.dataType == 'int' or cf.dataType == 'list':
                        value = eval(value)
                    else:
                        value = value
        except:
            notification.error('设置失败', '请检查输入的数据是否正确', self.cs)
            return
        self.config[key] = value
        notification.success('表单修改成功', f'{cf.label}已经被设置为：{value}', self.cs)
