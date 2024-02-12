from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton
from qfluentwidgets import ComboBox, LineEdit


class Layout(QWidget):
    def __init__(self, parent=None, config=None):
        super().__init__(parent=parent)
        self.config = config
        self.hBoxLayout = QVBoxLayout(self)
        self.lay1 = QHBoxLayout(self)
        self.lay2 = QHBoxLayout(self)
        self.lay3 = QHBoxLayout(self)
        self.pat_styles = ['普通', '地毯', '拖动礼物']
        self.student_name = []
        self.label1 = QLabel('列表选择你要添加邀请的学生，修改后请点击确定：', self)
        for i in range(0, len(self.config.static_config['student_names'])):
            if self.config.static_config['student_names'][i][self.config.server_mode + '_implementation']:
                self.student_name.append(self.config.static_config['student_names'][i][self.config.server_mode + '_name'])
        self.input1 = ComboBox(self)
        self.input = LineEdit(self)
        self.input.setFixedWidth(650)
        self.ac_btn = QPushButton('确定', self)

        self.favor_student1 = self.config.get('favorStudent1')
        self.input1.addItems(self.student_name)
        # self.input1.setText(','.join(self.favor_student))
        self.favor_student1 = self.check_valid_student_names()
        self.config.set('favorStudent1', self.favor_student1)
        self.input.setText(','.join(self.favor_student1))


        self.label2 = QLabel('选择摸头方式：', self)
        self.input2 = ComboBox(self)
        self.pat_style = self.config.get('patStyle') or '普通'
        self.input2.addItems(self.pat_styles)
        self.input2.setText(self.pat_style)
        self.input2.setCurrentIndex(self.pat_styles.index(self.pat_style))


        self.lay1.setContentsMargins(10, 0, 0, 0)
        self.lay1.addWidget(self.label1, 20, Qt.AlignLeft)
        self.lay1.addWidget(self.input1, 0, Qt.AlignRight)
        self.lay1.addSpacing(16)
        self.lay1.addStretch(1)
        self.lay1.setAlignment(Qt.AlignCenter)

        self.lay2.setContentsMargins(10, 0, 0, 0)
        self.lay2.addWidget(self.label2, 20, Qt.AlignLeft)
        self.lay2.addWidget(self.input2, 0, Qt.AlignRight)
        self.lay2.addSpacing(16)
        self.lay2.addStretch(1)
        self.lay2.setAlignment(Qt.AlignCenter)

        self.lay3.setContentsMargins(10, 0, 0, 0)
        self.lay3.addWidget(self.input, 0, Qt.AlignLeft)
        self.lay3.addWidget(self.ac_btn, 20, Qt.AlignRight)
        self.lay3.addSpacing(16)
        self.lay3.addStretch(1)
        self.lay3.setAlignment(Qt.AlignCenter)

        self.hBoxLayout.addSpacing(16)
        self.hBoxLayout.setAlignment(Qt.AlignCenter)

        self.hBoxLayout.addLayout(self.lay1)
        self.hBoxLayout.addLayout(self.lay3)
        self.hBoxLayout.addLayout(self.lay2)
        self.__init_Signals_and_Slots()

    def __add_student_name_in_the_last(self):
        self.favor_student1.append(self.input1.currentText())
        self.favor_student1 = self.check_valid_student_names()
        self.config.set('favorStudent1', self.favor_student1)
        self.input.setText(','.join(self.favor_student1))

    def __accept_pat_style(self):
        self.pat_style = self.input2.text()
        self.config.set('patStyle', self.pat_style)

    def __student_name_change_by_keyboard_input(self):
        text = self.input.text()
        self.favor_student1 = text.split(',')
        self.config.set('favorStudent1', self.favor_student1)
        print(self.favor_student1)

    def __init_Signals_and_Slots(self):
        self.input2.currentTextChanged.connect(self.__accept_pat_style)
        self.input1.currentTextChanged.connect(self.__add_student_name_in_the_last)
        self.ac_btn.clicked.connect(self.__student_name_change_by_keyboard_input)

    def check_valid_student_names(self):
        temp = []
        appeared_names = []
        for fav in self.favor_student1:
            if fav in self.student_name and (fav not in appeared_names):
                temp.append(fav)
                appeared_names.append(fav)
        return temp
