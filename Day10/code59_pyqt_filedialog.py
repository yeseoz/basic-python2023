# 다이얼로그
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit(self)
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction('Open',self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('파일열기')
        openFile.triggered.connect(self.onClicked)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False) # 기본 메뉴바? 일 수도 ?
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        # 필수설정
        self.setWindowTitle('파일다이얼 로그')
        self.setGeometry(300, 300, 300, 300)
        self.show()

    def onClicked(self):
        fname = QFileDialog.getOpenFileName(self, '파일열기', './')
        
        if fname[0]: # 파일을 선택했다면
            file = open(fname[0], 'rt', encoding='utf-8')
            with file:
                data = file.read()
                self.textEdit.setText(data)

            file.close()


        QMessageBox.about(self, '성공', '로드했습니다.') # 일반적인 메시지

    # 메인윈도우에 기본적으로 있는 슬롯
    def closeEvent(self, event) ->None:
        reply = QMessageBox.question(self, '종료', '정말 종료하시겠습니까?',
                                     QMessageBox.StandardButton.Yes| QMessageBox.StandardButton.No, QMessageBox.StandardButton.No) # QMessageBox.Yes ,No 해도 작동 됨
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ =='__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())