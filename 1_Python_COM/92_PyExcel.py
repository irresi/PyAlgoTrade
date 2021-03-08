"""파이썬으로 엑셀 다루기
excel : workbook <- workwsheet
                 <- workwsheet

좀 더 안전한 버전
https://stackoverflow.com/questions/41492210/win32com-excel-application-cant-open-documents-anymore

"""

"""
import win32com.client
excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True
#여기까지만 수행하면 엑셀이 열렸다가 닫힌다. 엑셀은 워크북이 없으면 자동으로 종료가 된다.,
wb = excel.Workbooks.Add()
ws = wb.Worksheets("Sheet1")
ws.Cells(1, 1).Value = "Pythond" #셀의 1행 A1열에 다음 문자열이 입력된다
wb.SaveAs('C:\\Users\\skybl\\PycharmProjects\\pythonProject\\PyAlgoTrade\\1_Python_COM\\Example.xlsx') # 절대경로만 사용가능
print(ws.Cells(1,1).Value)
excel.Quit()
"""

import win32com.client as w3c
excel = w3c.Dispatch("Excel.Application")
excel.Visible = True
wb = excel.Workbooks.Open('C:\\Users\\skybl\\PycharmProjects\\pythonProject\\PyAlgoTrade\\1_Python_COM\\Example.xlsx') #워크북 객체를 얻음
ws = wb.ActiveSheet #현재 Active상태인 Worksheet선택
ws.Cells(1,2).Value = "is"
ws.Range("C1").Value = "good"
ws.Range("C1").Interior.ColorIndex = 10
ws.Range("A2:C2").Interior.ColorIndex = 27 #다음과 같이 범위 설정을 통해 색을 바꿀 수 있다.