#모듈
# import time
# print(time.localtime().tm_year,'년')
# print(time.localtime().tm_mon,'월')
# print(time.localtime().tm_mday,'일')
# p=time.localtime()
#
# print(p.tm_year)
# print(p.tm_mon)
# print(p.tm_mday)
#
# print(time.localtime().tm_hour,'시',time.localtime().tm_min,'분')

#실습 인터넷에 나와있는거 시간 구하기 간편하게 출력
import datetime #import datetime 입력받음
# from datetime import datetime
# now= datetime.now()
# print(now)
# print(now.strftime('%y-%m-%d %H:%M:%S'))

#실습 time 만들기 (sleep함수 : 프로그램 실행 속도 제어 입력한 값이 지나면 출력이됨)
# import time
# print('시작')
# time.sleep(10)
# print('3초지남')
#-------------------------------------------------------------

#1초마다 화면에 타이머 출력
#결과
# 1.타이머시작
# 1초
# 2초
# 3초
# 타이머 종료
# import time
# print('타이머시작')
# for x in range(1,1000):
#     time.sleep(1)
#     print(x,'초지남',sep='')
# print('종료')

#-------------------------
# random 모듈
#난수모듈 , 주사위 게임
# import random
# a=random.randint(1,6)
#
# data=['홍길동','이순신','김순희','이철수']
# save = {}
#
# for name in data:
#     save[name] = random.randint(1,6)
# for name,no in save.items():
#     print(name,no)

#-----------------강사님이한거-------------------------
#난수모듈
#주사위 게임
# import random
#
# a = random.randint(1,6)
# b = random.randint(1,6)
# print('A:', a, 'B:', b)
# if a>b:
#     print('A승')
# elif b>a:
#     print('B승')
# else:
#     print('무승부')
#----------------------------------------------------

# import random
# print(random.sample(range(1,46),6))

#-----------------------------------------------------
#chice()
# print(random.choice(['가위','바위','보']))


#shuffle():섞는다
# data = ['나비','나비','벌','벌','꽃','꽃','꽃']
# random.shuffle(data)
# print(data)

# import turtle
# turtle.shape('turtle')
# turtle.color('red')
# for x in range(1,5):
#     turtle.forward(100)
#     turtle.right(90)
# turtle.done()

