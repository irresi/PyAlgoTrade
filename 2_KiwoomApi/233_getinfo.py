"""
TR : 서버로부터 데이터를 주고받는 행위
이번 절에서는 종목 코드를 입력 받은 후 사용자가 조회 버튼을 클릭하면
해당 종목에 대한 종목명과 거래량을 출력하는 프로그램을 만든다.


/********************************************************************/
/// ########## Open API 함수를 이용한 전문처리 C++용 샘플코드 예제입니다.

 [ opt10001 : 주식기본정보요청 ]

 [ 주의 ]
 PER, ROE 값들은 외부벤더사에서 제공되는 데이터이며 일주일에 한번 또는 실적발표 시즌에 업데이트 됨

 1. Open API 조회 함수 입력값을 설정합니다.
	종목코드 = 전문 조회할 종목코드
	SetInputValue("종목코드"	,  "입력값 1");


 2. Open API 조회 함수를 호출해서 전문을 서버로 전송합니다.
	CommRqData( "RQName"	,  "opt10001"	,  "0"	,  "화면번호");

/********************************************************************/

OpenApi+의 TR처리 순서
1) SetInputValue 메서드를 사용해 TR 입력 값을 설정합니다.
2) CommRqData 메서드를 사용해 TR을 서버로 송신합니다.
3) 서버로부터 이벤트가 발생할 때까지 이벤트 루프를 사용해 대기합니다.
4) CommGetData 메서드를 사용해 수신 데이터를 가져옵니다.
입력 -> 요청 -> 대기 -> 데이터 가져오기

"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #Kiwoom login
        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.kiwoom.dynamicCall("CommConnect()")

        self.kiwoom.OnEventConnect.connect(self.event_connect)
        self.kiwoom.OnReceiveTrData.connect(self.receive_trdata)

        self.setWindowTitle("PyStock")
        self.setGeometry(300,300,300,150)

        label = QLabel('종목코드: ', self)
        label.move(20,20)

        self.code_edit = QLineEdit(self)
        self.code_edit.move(80,20)
        self.code_edit.setText("039490")

        btn1 = QPushButton("조회",self)
        btn1.move(190,20)
        btn1.clicked.connect(self.btn1_clicked)

        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(10,60,280,80)
        self.text_edit.setEnabled(False)
    def event_connect(self, err_code):
        if err_code ==0:
            self.text_edit.append("로그인 성공")
    def btn1_clicked(self):
        code = self.code_edit.text()
        self.text_edit.append("종목코드: " + code)

        #SetInputValue
        self.kiwoom.dynamicCall("SetInputValue(Qstring, Qstring)", "종목코드", code)
        self.kiwoom.dynamicCall("CommRqData(Qstring, Qstring, int, Qstring)","opt10001_req", "opt10001", 0, "0101")

    def receive_trdata(self, screen_no, rqname,trcode,recordname, prev_next, data_len, err_code, msg1, msg2):
        if rqname =="opt10001_req":
            name = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "종목명")
            volume = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "거래량")
            price = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "현재가")
            self.text_edit.append("종목명: "+name.strip())
            self.text_edit.append("거래량: "+volume.strip())
            self.text_edit.append("현재가: "+price.strip(' -'))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()