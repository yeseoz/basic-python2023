# 위키독스 참조 https://wikidocs.net/21920
# MFC랑 비슷한듯
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon # 아이콘 쓸때 사용

# Qt 예제할 때는 거의 클래스를 만든다
class MyApp(QWidget):
    def __init__(self):
        super().__init__()     
        self.initUI()  
        
    def initUI(self):
        # GUI 화면 설정
        self.setWindowTitle('Simple Window')
        # 아이콘 추가
        self.setWindowIcon(QIcon('./Day09/iot.png'))
        #self.move(1920//2-200,1080//2-100) # self.move()안하면 정중앙에 뜸
        self.resize(400, 200)
        self.show() # 핵심! 이거 없으면 안보임


if __name__ == '__main__':
    app = QApplication(sys.argv) # 실행할때 파라미터가 필요하면 쓰겠다. 입력 안해도 상관없음
    ex = MyApp() # 내가 쓰고 싶은 위젯 생성
    sys.exit(app.exec_()) # 끝을 낸다