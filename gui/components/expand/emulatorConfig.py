from PyQt5.QtWidgets import QFileDialog

from .expandTemplate import TemplateLayout

class Layout(TemplateLayout):
    def __init__(self, parent=None, config=None):
        configItems = [
            {
                'label': '在运行Baas时打开模拟器(启动模拟器的功能开关，关闭后不会启动模拟器)',
                'key': 'open_emulator_stat',
                'type': 'switch'
            },
            {
                'label': '是否模拟器多开（打开后无视已经启动的模拟器进程，将再启动一个模拟器）)',
                'key': 'multi_emulator_check',
                'type': 'switch'
            },
            {
                'label': '等待模拟器启动时间(模拟器从开始启动到桌面加载完成的时间(秒)，一般默认)',
                'type': 'text',
                'key': 'emulator_wait_time'
            },
            {
                'label': '选择模拟器地址',
                'type': 'text_and_file_button',
                'key': 'program_address'
            }
        ]

        super().__init__(parent=parent, configItems=configItems, config=config)

    def _choose_file(self, line_edit):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("Executable files (*.exe);;Link files (*.lnk)")
        file_dialog.setOption(QFileDialog.DontUseNativeDialog, False)
        if file_dialog.exec_():
            file_names = file_dialog.selectedFiles()
            if file_names:
                file_path = file_names[0]
                line_edit.setText(file_path)
                self.config.set('program_address', file_path)
