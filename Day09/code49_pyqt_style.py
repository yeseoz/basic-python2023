# 스타일
import sys
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 스타일 설정
        lbl_red = QLabel('Red')
        lbl_red.setStyleSheet("color: red;"
                              "border-style : solid;" # 경계선을 실선
                              "border-width : 2px;" # 경계선 두께
                              "border-color : #FA8072;" #경계선의 색성
                              "border-radius : 10px") # 경계선의 모서리를 3px 만큼 둥글게

        lbl_green = QLabel('Green')
        lbl_green.setStyleSheet("color: green;"
                              "border-style : dashed;" # 경계선 점선
                              "border-width : 5px;" 
                              "border-color : #7FFFD4;") 
                               
        lbl_blue = QLabel('Blue')

        # QVBoxLayout 세로로 / QHBoxLayout 가로로 위치
        vbox = QVBoxLayout() # 레이아웃을 세로로 구분짓는다
        vbox.addWidget(lbl_red) # 위젯 추가
        vbox.addWidget(lbl_green)

        self.setLayout(vbox)
        # 기본설정 - 사이즈, show() 필수!!
        self.setWindowTitle('스타일 지정')
        self.setGeometry(300, 300, 300, 300)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())