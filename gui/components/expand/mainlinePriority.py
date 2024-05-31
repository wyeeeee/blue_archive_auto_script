from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QVBoxLayout
from qfluentwidgets import LineEdit, ComboBox
from gui.util import notification


class Layout(QWidget):
    def __init__(self, parent=None, config=None):
        super().__init__(parent=parent)
        self.config = config
        self.info_widget = self.parent()
        self.hBoxLayout = QVBoxLayout(self)
        self.lay1 = QHBoxLayout(self)
        self.lay2 = QHBoxLayout(self)
        self.lay1_hard = QHBoxLayout(self)
        self.lay2_hard = QHBoxLayout(self)

        self.label = QLabel('普通关卡与次数（如"1-1-1,1-2-3"表示关卡1-1打一次，然后关卡1-2打三次）：', self)
        self.input = LineEdit(self)
        self.accept = QPushButton('确定', self)
        self.label_hard = QLabel('困难关卡设置同上，(注意：次数最多为3），逗号均为英文逗号，日服、国际服可填max：', self)
        self.input_hard = LineEdit(self)
        self.accept_hard = QPushButton('确定', self)

        self.hard_task_combobox = ComboBox(self)
        self.each_student_task_number_dict = {
            "根据学生添加关卡": [],
            "爱丽丝宝贝": [],
        }
        for i in range(0, len(self.config.static_config["hard_task_student_material"])):
            self.each_student_task_number_dict.setdefault(self.config.static_config["hard_task_student_material"][i][1],
                                                          [])
            temp = self.config.static_config["hard_task_student_material"][i][0] + "-3"
            (self.each_student_task_number_dict[self.config.static_config["hard_task_student_material"][i][1]].append(
                temp))
        for key in self.each_student_task_number_dict.keys():
            self.hard_task_combobox.addItem(key)
        self.hard_task_combobox.currentIndexChanged.connect(self.__hard_task_combobox_change)
        _set_main = self.config.get('mainlinePriority')
        _set_hard = self.config.get('hardPriority')

        self.setFixedHeight(200)

        self.input.setText(_set_main)
        self.input_hard.setText(_set_hard)

        self.input.setFixedWidth(700)
        self.input_hard.setFixedWidth(700)

        self.lay1.setContentsMargins(10, 0, 0, 10)
        self.lay2.setContentsMargins(10, 0, 0, 10)
        self.lay1_hard.setContentsMargins(10, 0, 0, 10)
        self.lay2_hard.setContentsMargins(10, 0, 0, 10)

        self.accept.clicked.connect(self.__accept_main)
        self.accept_hard.clicked.connect(self.__accept_hard)

        self.lay1.addWidget(self.label, 0, Qt.AlignLeft)
        self.lay2.addWidget(self.input, 1, Qt.AlignLeft)
        self.lay2.addWidget(self.accept, 0, Qt.AlignLeft)
        self.lay1_hard.addWidget(self.label_hard, 0, Qt.AlignLeft)
        self.lay2_hard.addWidget(self.input_hard, 1, Qt.AlignLeft)
        self.lay2_hard.addWidget(self.accept_hard, 0, Qt.AlignLeft)

        self.lay1.addStretch(1)
        self.lay1.setAlignment(Qt.AlignCenter)
        self.lay2.setAlignment(Qt.AlignCenter)
        self.lay1_hard.addStretch(1)
        self.lay1_hard.setAlignment(Qt.AlignCenter)
        self.lay1_hard.addWidget(self.hard_task_combobox, 0, Qt.AlignRight)

        self.lay2_hard.setAlignment(Qt.AlignCenter)

        self.hBoxLayout.addSpacing(16)
        self.hBoxLayout.setAlignment(Qt.AlignCenter)

        self.hBoxLayout.addLayout(self.lay1)
        self.hBoxLayout.addLayout(self.lay2)

        self.hBoxLayout.addLayout(self.lay1_hard)
        self.hBoxLayout.addLayout(self.lay2_hard)

    def __accept_main(self):
        try:
            from module.normal_task import readOneNormalTask
            input_content = self.input.text()
            self.config.set('mainlinePriority', input_content)
            input_content = input_content.split(',')
            temp = []
            for i in range(0, len(input_content)):
                temp.append(readOneNormalTask(input_content[i]))
            self.config.set("unfinished_normal_tasks", self.config['unfinished_normal_tasks'])  # refresh the config unfinished_normal_tasks
            notification.success('设置成功', f'你的普通关卡已经被设置为：{input_content}', self.config)
        except Exception as e:
            notification.error('设置失败', f'请检查输入格式是否正确，错误信息：{e}', self.config)

    def __accept_hard(self):
        try:
            from module.hard_task import readOneHardTask
            input_content = self.input_hard.text()
            self.config.set('hardPriority', input_content)
            input_content = input_content.split(',')
            temp = []
            for i in range(0, len(input_content)):
                temp.append(readOneHardTask(input_content[i]))
            self.config.set("unfinished_hard_tasks", temp)                                         # refresh the config unfinished_hard_tasks
            notification.success('设置成功', f'你的困难关卡已经被设置为：{input_content}', self.config)
        except Exception as e:
            notification.error('设置失败', f'请检查输入格式是否正确，错误信息：{e}', self.config)

    def __hard_task_combobox_change(self):
        if self.hard_task_combobox.currentText() == "根据学生添加关卡":
            return
        st = ""
        if self.input_hard.text() != "":
            st = self.input_hard.text() + ","
        self.input_hard.setText(
            st + ','.join(self.each_student_task_number_dict[self.hard_task_combobox.currentText()]))
        self.__accept_hard()

