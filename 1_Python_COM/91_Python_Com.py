"""
Component Object Model : 컴포넌트 객체를 이용해 프로그램을 개발하는 모델
ex) 컨테이너 이용해 집짓기
+프로그래밍 언어와 상관없이 개발된 객체를 사용할 수 있게 해준다.
파이썬에서 다른 프로그래밍 언어로 작성된 COM객체를 생성하려면 win32com.client라는 모듈의 Dispatch 메서드를 사용하면 된다.
"""


import win32com.client
word = win32com.client.Dispatch("Word.application")
word.Visible = True