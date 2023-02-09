# 레이아웃 박스 배치
import sys
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btnOk = QPushButton('Ok')
        btnCancel = QPushButton('Cancel')

        hbox = QHBoxLayout() # 수평박스
        hbox.addStretch(1) # 신축성있는 빈공간
        hbox.addWidget(btnOk)
        hbox.addWidget(btnCancel)
        hbox.addStretch(1)

        vbox = QVBoxLayout() # 수직 박스
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

        # 필수설정
        self.setWindowTitle('박스 배치')
        self.setGeometry(300, 300, 300, 300)
        self.show()



if __name__ =='__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())