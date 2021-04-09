#조건문

# a=-1
# #
# if a>0:
#     print('양수')
#     print(a)
# else:
#     print('음수')
#     print(a)

#실습 회원등급 출력


# a=int(input('점수를입력해주세요'))
#
# # a90보다 크면 굿 아니면 try출력
#
# if a>90:
#     print('good')
# else:
#     print('try')
#
# 실습)비밀번호 체크
# pw='1234'
# a=input()
#
# if pw==a:
#     print('문이열립니다')
# else:
#     print('추방')


# 실습)어떤수 짝수이면 짝수라고 홀수이면 홀수 출력

# a=int(input('숫자를입력해주세요'))
#
# if a==0:
#     print('짝수도 홀수도 아닙니다')
#
# elif a%2==0:
#     print('짝수입니다')
#
# else:
#     print('홀수입니다')


#실습)90점이상은 a 89-80점b, 79-70점은c ,69-60점 d ,59 은 f

# incert = 101
#
# if incert>100:
#     print('잘못입력하였습니다')
# elif incert>=90:
#     print('A점입니다')
# elif incert>=80:
#     print('B점입니다')
# elif incert>=70:
#     print('C점입니다')
# elif incert>=60:
#     print('D점입니다')
# else:
#     print('F학점입니다')

#if문은 하나로하고 elif으로 해야 한문장으로 출력이 되지 if if 반복하면 그해당하는값을 모두 출력이 된다


#실스)몸무게와 키를 입력받아서 비만여부출력
#0.95 1.05
# a=100
# wight=60    #몸무게
# height=170   #키
#
# average=(height-100)*0.9
#
# print('nomar은',average)
#
# average1=average*0.95
# average2=average*1.05
#
# print('오차범위는',average1,average2)
#
# # if average1<wight and wight>average2:
# #     print('정상')
#
# if average1<wight:
#     print('정상')
# elif average2>wight:
#     print('정상')
#
# else:
#     print('비정상')


#강사님이한거
# height=165.5
# weight=60.1
# normal=(height-100)*0.9
# print('정상체중',normal)
#
# if weight<normal*0.95:
#     print('미달')
# elif weight<=normal*1.05:
#     print('정상입니다')
# else:
#     print("비만입니다")

#실습)계산기 두수 기호까지 입력받음  플러스면 플러스 마이너스면 마이너스

# a=int(input('첫번째 숫자를 입력해주세요'))
# b=int(input('두번째 숫자를 입력해주세요'))
# c=input('기호를 입력해주세요')
#
# if c=='+':
#     print(a+b)
# elif c=='-':
#     print(a-b)
# elif c=='*':
#     print(a*b)
# elif c=="/":
#     print(a/b)
# else:
#     print('다시엽력해주세요')


# 한번에 두수를 입력

# data=int(input('두수를 입력해주세요').split())   #int 값을 넣으면 에러
# data=input('두수를 입력해주세요').split()
#
# print(data)
# a=int(data[0])
# b=int(data[1])
#
# c=input('기호를 입력해주세요')
#
# if c=='+':
#     print(a+b)
# elif c=='-':
#     print(a-b)
# elif c=='*':
#     print(a*b)
# elif c=="/":
#     print(a/b)
# else:
#     print('다시엽력해주세요')



#2)
# data= input('계산식은? 예) 숫자 기호 숫자').split()
# print(data)
#
# a=int(data[0])
#
# b=int(data[2])
#
# sign=data[1]
#
# if sign =='+':
#     print('%d+%d=%d'%(a,b,a+b))
# elif sign=='-':
#     print('%d+%d=%d'%(a,b,a-b))
# elif sign == '*':
#     print('%d+%d=%d' % (a, b, a * b))
# elif sign == '/':
#     print('%d+%d=%d' % (a, b, a / b))
# else:
#     print('잘못 된 기호입니다')

#3)
# data = input('계산식은')
# cal = eval(data)
# print(cal)        # eval 로 저절로 계산이 된다 하지만 지향하지않는다

#3-1)
# import os
# print(os.listdir())
#
# data = input('계산식은')
#
# print(eval(data))

#실습)두수를 입력받아서 큰수를 화면에 출력

# data=input('두수를 입력해주세요').split()
#
# a=int(data[0])
# b=int(data[1])

# a=int(input('숫자를입력해주세요'))
# b=int(input('숫자를입력해주세요'))

# if a>b:
#     print(a)
# elif b>a:
#     print(b)
#
# else:
#     print('두수는 같습니다')



#거스름돈 계산 현재있는 금액과 물품구입금액을 입력받고 비교 거스름돈을 구하는 프로그램
#출력 돈이 부족한경우 거스름돈 얼마 부족하지않으면 계산완료

# a=int(input('받은돈을 입력해주세요'))
# b=int(input('물품값을 입력해주세요'))
#
# if a>b:
#     print(a-b,'원 거스름돈입니다',sep='')
# elif b>a:
#     print(b-a,'원 이부족합니다',sep='')
# else:
#     print('계산완료')

#논리연산자
# a=10;b=20
# print(a>0 and b>0)
# print(a>0 and b>0)  # and 는 둘다 참이여야된다 한개라도 조건성립이안되면 거짓이 된다
#
# print(a>0 or b<0)  # or 을 또는 둘중에 한개라도 조건이 성립되면 true
# print(not a>0)  # not 은 반대로 성립해준다

#실습
# a=10; b=20
# if a==0 or b==0:
#     print('0이 아닌수를 입력하세요')
#
# elif a>0 and b>0:
#     print('둘다 양수입니다')
# # elif a>0 or b<0:
# #     print('둘중 b가 음수입니다')
# # elif a<0 or b>0:
# #     print('둘중 a가 음수입니다')
#
# elif a>0 or b>0:
#     print('둘중 하나가 음수입니다')
# else:
#     print('둘다 음수입니다')

#보기메뉴를 보고 음식을 선택하면 가야할 코너를 알려주는 프로그램
#1자장면 2 짬뽕 3설렁탕 4비빔박 5피자 6스파게티 메뉴를 선택하세요
#1,2번이면 중식 3,4번이면 한식 5,6번이면 양식

# price={'1':['자장면',5000],'2':['짬뽕',6000],'3':['설렁탕',7000],
#        '4':['비빔박,6000'],'5':['피자,10000'],'6':['스파게티,7000']}
#
# print('-'*22)
# print('[국제식당]오늘의메뉴')
# print('-'*22)
# # data= ('1.짜장면\n,2.짬뽕\n,3.설렁탕\n,4.비빔박\n,5.피자\n,6.스파게티')
# print(price)
#
# no=input('보기메뉴를 골르세요')
#
# print(price[no[0]],'선택')
#
# print(price[no][1],'원')
#
# if no in ['1','2']:
#     print('중식코너')
# elif no in ['3', '4']:
#     print('한식코너')
# elif no in ['3', '4']:
#     print('양식코너')
# else:
#     print('잘못')

# if a == 1 or a==2:
#     print('중식으로가주세요')
#
# elif a== 3 or a==4:
#     print('한식으로가주세요')
#
# elif a== 5 or a== 6:
#     print('양식으로가주세요')
#
# else:
#     print('다시입력해주세요')

# if a in [1,2]:
#     print('중식으로가주세요')
#
# elif a in [3,4]:
#     print('한식으로가주세요')
#
# elif a in [5,6]:
#     print('양식으로가주세요')
#
# else:
#     print('다시입력해주세요')

#2번째 실습

price={'1':['자장면',5000,'중식'],'2':['짬뽕',6000,'중식'],'3':['설렁탕',7000,'한식'],
       '4':['비빔박,6000','한식'],'5':['피자,10000','양식'],'6':['스파게티,7000','양식']}

print('-'*22)
print('[국제식당]오늘의메뉴')
print('-'*22)

print(price)

no=input('보기메뉴를 골르세요')




# if no in ['1','2']:
#     print('중식코너')
#
# elif no in ['3', '4']:
#     print('한식코너')
#
# elif no in ['5', '6']:
#     print('양식코너')

incert=price.keys()
if no in incert:
    print(price[no][0], '선택')
    print(price[no][1], '원')
    print(price[no][2], '코너')
else:
    print('다시입력해주세요')

#강사님이하신거
# price =({'1':['자장면', 5000,'중식'],'2':['짬뽕',6000,'중식'],'3':['설렁탕',8000,'한식'],
#          '4':['비빔밥',10000,'한식'],'5':['피자',12000,'양식'],'6':['스파게티',9000,'양식']})
# print('-' * 22)
# print('[국제식당]오늘의 메뉴')
# print('-' * 22)
# print('1.자장면\n2.짬뽕\n3.설렁탕\n4.비빔밥\n5.피자\n6.스파게티')
# print('-' * 15)
# no = input('메뉴는?')
# menukey = price.keys()
# if no in menukey:
#     print(price[no][0] ,'선택')
#     print(price[no][1] ,'원')
#     print(price[no][2] ,'코너')
# else:
#     print('다시입력해 주세요')

