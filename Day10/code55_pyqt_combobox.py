# 체크버튼 라디오 버튼
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lblOption = QLabel('선택값 : ', self) # self. 안붙이면 initUI의 변수임 self 붙이면 전역변수가됨
        self.lblOption.move(20, 20)

        cbOption = QComboBox(self)
        cbOption.addItem('Option1')
        cbOption.addItem('Option2')
        cbOption.addItem('Option3')
        cbOption.addItem('Option4')
        cbOption.addItem('Option5')

        cbOption.move(20,40)

        cbOption.activated[str].connect(self.onActivated) # Option1

        # 필수설정
        self.setWindowTitle('콤보박스')
        self.setGeometry(300, 300, 300, 300)
        self.show()
    
    # 슬롯 함수
    def onActivated(self,text):
        self.lblOption.setText('선택값 : ' +  text)
        self.lblOption.adjustSize() # 글자수 만큼 라벨의 넓이를 조정

if __name__ =='__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())