# 윈도우 창닫기 앱
# 2023.02.09
# Yeseo

import sys
from PyQt5.QtWidgets import QApplication,QPushButton,QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton('Quit', self) # QPushButton('버튼에 표시된 텍스트', 버튼이 위치할 부모위ㅣ젯)
        btn.move(320,170)
        btn.resize(btn.sizeHint()) # 글자크기에 따라 사이즈 조정해줌
        # 버튼 툴팁
        btn.setToolTip('이거 누르면 그냥 꺼져요! <b>조심하세요</b>')

        btn.clicked.connect(QCoreApplication.instance().quit) # 생성된 객체를 instance라 부름
        # 버튼이 눌리면(clicked) 현재 인스턴스(instance())가 종료 됨

        self.setWindowIcon(QIcon('./Day09/iot.png'))
        self.setWindowTitle('Quit Button')
        self.setGeometry(800, 300, 400, 200) # x, y, w, h
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())