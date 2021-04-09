#반복문 : while
#while True: #조건이 참일때 무한반복

#실습 1-10까지 while문으로 출력
#----------1번째 방법---------
# a=0
# while True:
#     a += 1  #1씩증가
#     if a > 10:
#         break
#     print(a)
#-------------------------------

#-------2번째 방법----------------
# a=0
# while a<10:
#     a += 1  #1씩증가
#     print(a)
#--------------------------------

#---------합 구하는방법-------------
# a=0 #증가하는 변수
# sum=0   #합계를 누적할변수
# while True:
#     a += 1
#     if a>10:
#         break
#     sum += a
# print(sum)
#--------------------------------

#a가 증가하면서 합계를 구하고 그 합계가 2000넘으면 종료
#1)
# a=0
# sum=0
# while True:
#     a = a+1
#     sum += a
#     if sum>2000:
#         print(a,sum)
#         break

#2)
# a=0
# sum=0
# while sum<2000:
#     a = a+1
#     sum += a
# print(a,sum)

#사용자가 입력한 수를 누적하다가 만약 0을 입력하면 종료하고  누적합계를 출력
#1번째방법 -추천
# incert=0
# sum=0
# while True:
#     incert = int(input('더할값을 입력해주세요'))
#     sum += incert
#     if incert==0:
#         break
# print('총합계는',sum,'입니다',sep='')


# incert = 1
# sum=0
# while incert != 0:
#     incert = int(input('더할값을 입력해주세요'))
#     sum += incert
# print('총합계는',sum,'입니다',sep='')

#------------------------------------------------------------------



# for b in range(7,0,-1):
#     print('*' * b,)
# for y in range(1,7,1):
#     print('1')

        # '★' *y)

# for y in range(1,7,1):
#     print('*'*y)
#     print('\n')

for x in range(7,0,-1), for in range(1,7,1):
    print('0'*x,end='');print('*'*x)




#----------------------------------------------------------------

#4일째 ===================================================================================
#실습2)구구단을 출력하는 프로그램을 만들어봅시다


# for dan in range(2,20,1):
#     # print(dan)
#     for x in range(1,10,1):
#         print(dan,'*',x,'=',dan*x,' ',end = ' ')
#     print('-----',dan,'단','------')
#--------------------------------------------------------------------------------------

#실습3) 숫자를 입력받아 그범위 안의 수 중 0부터 3의 배수를 출력하는 프로그램 만드렁주세요 0,3,6,9,12
# incert=int(input())
# for x in range(0,100,incert):
#     print(x, end='\t')
# print()
# for x in range(0,incert+1):
#     if x%3==0:
#         print(x,end='\t')

#실습4) 숫자 두개와 기호를 입력받아 계산기 프로그램을 만들어 봅시다 단 사용자가 q를 입력하면 계산기 프로그램 종료

# while True:
#     incert1 = int(input('첫번째 숫자를 입력하세요'))
#     incert2 = int(input('두번째 숫자를 입력하세요'))
#     sign=input('기호를 입력(+,-,*,/)')

    # sign=='+'
    # print('두수의합은',incert1+incert2)
    # continue
    # sign=='-'
    # print('두수의합은',incert1-incert2)
    # continue
    # sign=='*'
    # print('두수의합은',incert1*incert2)
    # continue
    # sign=='/'
    # print('두수의합은',incert1/incert2)
    # continue
    # sign=='q'
    # print('종료')
    # break
#-------------------------강사님 한거--------------------------------------

#예1)
# while True:
#     a=int(input('first:'))
#     b=int(input('second:'))
#     sign = input('기호:')
#     if sign=='+':
#         print(a+b)
#     elif sign =='-':
#         print(a-b)
#     elif sign == '*':
#         print(a*b)
#     elif sign =='/':
#         print(a/b)
#     else:
#         print('잘못된 기호')
#
#     if input('종료(y)?')=='y': break

# 2)
# while True:
#     a = input('first:')
#     if a == 'q': break
#     a = int(a)  #처음부터 int 변환 안해도 후에 int 로 변환 해줌
#     b = int(input('second:'))
#     #원하는 기호가 입력될때가 계속입력
#     while True:
#         sign = input('기호:')
#         if sign in ['+', '-', '*', '/']:
#             break
#
#     if sign == '+':
#         print(a + b)
#     elif sign == '-':
#         print(a - b)
#     elif sign == '*':
#         print(a * b)
#     elif sign == '/':
#         print(a / b)
#     else:
#         print('잘못된 기호')

#실습5) 반학생들의 점수가 딕셔너리로 저장되어 있을때 값이 90점 이상인 학생들의 key만 출력하시오--------------
#예시
# dicA={1:80,2:80,3:56,4:50,5:90,6:70,7:90}
# val=list(dicA.values())
# key=list(dicA.keys())
#
# dic_val= map(int,val)
# dic_key= map(int,key)
#
# print(list(dic_val))
# print(list(dic_key))
#
# for i in


#(----강사님이 한거-------------------)

dicA={1:80,2:80,3:56,4:50,5:92,6:70,7:92}
# print(dicA.keys())
# print(dicA.values())
# print(dicA.items())
# for no,score in dicA.items():
#     if score>90:
#         print(no,'번이 90점이상입니다')



#실습6) listA=[홍길동, 이순신 ,김순희 이철수 ] 일 판매수량을 입력받아 히스토그램을 그리는 프로그램----------------
# 예 홍길동 ****** 결과물
# 이순신 *******
# 김순희 ******
# 이철수 ******
#사원의 판매수량 입력받아 >>저장 해야됨
#히스토그램 그리기

# 1)사원의 판매수량 입력
#2)히스토그램 그리기
#데이터구조: {'홍길동':10, '이순신':15, '김순희':5, '이철수':7}


# data1=['홍길동','이순신','김순희','이철수']
# save = {}
# for name in data1:
#     save[name]=int(input(name+'?'))
# print(save)
# for name1,salqty in save.items():
#     print(name,'*'*salqty)


# data = ['홍길동','이순신','김순희','이철수']
# qty={} #판매수량을 저장할 딕셔너리
# for name in data:
#     qty[name] = int(input(name + '?'))
# print(qty)
# for name, saleqty in qty.items():
#     print(name, '*' * saleqty)



