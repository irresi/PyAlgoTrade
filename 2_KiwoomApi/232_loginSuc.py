import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyStock")
        self.setGeometry(300, 300, 300, 150)

        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.kiwoom.dynamicCall("CommConnect()")

        self.text_edit = QTextEdit(self) #다른 메서드에서도 이 변수를 사용해 객체에 접근하기 위해 self를 쓴다.
        self.text_edit.setGeometry(10, 60, 280, 80) #(sx,sy, 높이, 너비)로 위치, 크기를 조절
        self.text_edit.setEnabled(False) #False : 수정 불가(쓰기 모드), True : 수정 가능(읽기 모드)

        self.kiwoom.OnEventConnect.connect(self.event_connect) # 연결 통신 상태가 바뀔 때 OnEventConnect라는 이벤트가 발생한다.
        #connect메서드 : 이벤트와 이벤트 처리 베서드 연결

    def event_connect(self, err_code):
        if err_code == 0:
            self.text_edit.append("로그인 성공")
        else:
            print(err_code)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()