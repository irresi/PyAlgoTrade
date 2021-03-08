"""
이베스트 투자증권 xing api 나 대신증권 api CYBOS Plus와 달리 키움 Open Api+는 OCX(Object Linking and Embedding Custom Control)방식을 사용
OCX 방식이 파이썬에서 사용하기 더 힘들다.
PyQt 패키지의 QAxContainer 모듈을 통해 사용할 것
파이썬 GUI 모듈 : wxPython1, PyQt5, TkInter(구식이지만 간단) 등

이벤트 루프 : 무한 반복하면서 이벤트를 처리하는 상태
""""""
import sys # 모듈명.변수와 같은 방식으로 함수를 써야 함
from PyQt5.QtWidgets import * # 모듈명을 생략
app = QApplication(sys.argv) #인스턴스 생성, 현재 소스코드에 대한 절대경로 전달
#label = QLabel("Hello PyQt")
label = QPushButton("Quit")
label.show()
app.exec_() # 이벤트 루프에 진입, 사용자가 발생한 이벤트를 그때그때 처리해줌
"""

"""
12.23 위젯과 윈도우
다른 위젯에 포함되지 않은 최생위 위젯을 window 라고 한다.
일반적으로 QMainWindow나 QDialog를 사용한다
"""
import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyStock")
        self.setGeometry(300,300,300,400) # 창의 위치 및 크기 조절

        btn1 = QPushButton("Click me", self)
        btn1.move(20,20)
        btn1.clicked.connect(self.btn1_clicked)

    def btn1_clicked(self):
        QMessageBox.about(self,"message","clicked") #창 이름, 버튼에 써진 것

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()