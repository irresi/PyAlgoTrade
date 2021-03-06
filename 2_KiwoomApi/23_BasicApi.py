"""
개발가이드를 무조건 봐야 한다.
여기서 시키는 순서를 하나라도 틀리면 오류가 난다.
이 것 때문에 몇 시간을 찾아봤다.
https://download.kiwoom.com/web/openapi/kiwoom_openapi_plus_devguide_ver_1.5.pdf

그리고 요구하는 32bit 운영체제만 제공하기 때문에 32비트 환경으로 바꿔야 한다.

"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *
from PyQt5.QtCore import *
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyStock")
        self.setGeometry(300,300,300,150) # 창의 위치 및 크기 조절

        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1") # OCX를 불러온 것
        #파이썬에서 키움증권의 클래스를 사용하려면 PyQt의 QAxWidget 클래스룰 사용해 인스턴스를 생성해야 한다.
        #키움증권에서 제공하는 클래스는 각각 고유의 CLSID또는 ProgID를 가지는데 해당 값을 QAxWidget 클래스의 생성자로 전달하면 인스턴스가 생성된다
        btn1 = QPushButton("Login", self)
        btn1.move(20,20)
        btn1.clicked.connect(self.btn1_clicked)

        btn2 = QPushButton("Check state", self)
        btn2.move(20,70)
        btn2.clicked.connect(self.btn2_clicked)

    def btn1_clicked(self):
        ret = self.kiwoom.dynamicCall("CommConnect()")
        print(self.kiwoom.dynamicCall("GetConnectState()"))
    def btn2_clicked(self):
        if self.kiwoom.dynamicCall("GetConnectState()")==0:
            self.statusBar().showMessage("Not connected")
        else:
            self.statusBar().showMessage("Connected")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()