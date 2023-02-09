# 위키독스 참조 https://wikidocs.net/21920
# MFC랑 비슷한듯
import sys
from PyQt5.QtWidgets import QApplication, QAction, QMainWindow, qApp, QDesktopWidget # QMainWindow 써야 상태바가 나옵니다. 
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate, QTime

# Qt 예제할 때는 거의 클래스를 만든다
class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()     
        self.initUI()  
        
    def initUI(self):
        # 액션
        actExit = QAction(QIcon('./Day09/exit.png'),'Exit',self) 
        actExit.setShortcut('Ctrl+Q') # 단축키 지정
        actExit.setStatusTip('앱 종료') # 메뉴에 마우스를 올렸을 때, 상태바에 나타날 상태팁
        actExit.triggered.connect(qApp.quit)

        actSave = QAction(QIcon('./Day09/save.png'),'Save',self)
        actSave.setShortcut('Ctrl+S')
        actSave.setStatusTip('앱 저장')

        actEdit = QAction(QIcon('./Day09/edit.png'),'Edit',self)
        actEdit.setShortcut('Ctrl+E')
        actEdit.setStatusTip('앱 수정')

        actPrint = QAction(QIcon('./Day09/print.png'),'Print',self)
        actPrint.setShortcut('Ctrl+P')
        actPrint.setStatusTip('프린트')

        menubar = self.menuBar() # 메뉴바 생성
        menubar.setNativeMenuBar(False)
        filemanu = menubar.addMenu('&File') # 파일 메뉴 // &F => File메뉴의 단축키를 Alt+F로 지정하겠다
        filemanu.addAction(actExit) 

        # 툴바
        toolbar = self.addToolBar('MainToolBar') # 툴바 타이틀은 없어도 됨
        toolbar.addAction(actSave)
        toolbar.addAction(actExit)
        toolbar.addAction(actEdit)
        toolbar.addAction(actPrint)

       
        # 상태바
        now = QDate.currentDate() # 현재 시간 날짜를 반환
        time = QTime.currentTime()
        self.statusBar().showMessage(now.toString('yyyy-MM-dd') + ' '+time.toString('hh:mm:ss')) # 현재 날짜를 문자열로 출력
        #self.statusBar().showMessage('StatusBar message')  # 저장했을때 저장했습니다. 실패했을때 실패 했습니다.
        self.setWindowIcon(QIcon('./Day09/iot.png'))
        # GUI 화면 설정
        self.setWindowTitle('Bar Window')
        #self.move(200,200) # self.move()안하면 정중앙에 뜸
        self.resize(400, 200)
        self.setCenter()
        self.show() # 핵심! 이거 없으면 안보임
    
    #화면 중심 셋팅
    def setCenter(self):
        qr = self.frameGeometry() # 창 자기자신의 위치와 크기정보
        cp = QDesktopWidget().availableGeometry().center() # 모니터 화면의 가운데 위치를 파악
        qr.moveCenter(cp) # 창의 직사각형 위치를 화면의 중심의 위치로 이동
        #self.move(qr.topLeft()) # 현재창을, 화면의 중심으로 이동했는 직사각형 qr의 위치로 이동

if __name__ == '__main__':
    app = QApplication(sys.argv) # 실행할때 파라미터가 필요하면 쓰겠다. 입력 안해도 상관없음
    ex = MyApp() # 내가 쓰고 싶은 위젯 생성
    sys.exit(app.exec_()) # 끝을 낸다