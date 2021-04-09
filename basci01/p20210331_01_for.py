#반복문 반복적으로 수행해야할일

# data1=[1,2,3,4,5]
#
# for x in data1:
#     print('python',x)
#
# for x in [1,2,4,5,6,54]:
#     print('python',x)

# data=['이선희','최불암','Bts']
#
# for x in [data]:
#     print(data[x])
#
# for x in [0,1,2]:
#     print(data[x])

    # print(data[1])
    # print(data[2])

#실습 0-9출력

# for i in [0,1,2,3,4,5,6,7,8,9]:
#     print(i)

#실습 0-100출력

#range(start값,stop값,step) 스텝은 얼마씩 증가 할건지 , *정수* 를 생성하는거다
# print (list(range(1,100,2))) # 1에서 스타트 100까지 2씩증가
# print (list(range(101)))  #한개 숫자만 들어가면 stop이 인식 되고 1개씩 증가 디폴트값이다
# print (list(range(10,20))) #start,stop

#합계를 구하기

# s=0 #합계를 저장할 변수
# for x in range(1,101,1):
#     s += x
# print(s)

#실습)사용자가 입력받은수로 합 구하기
# s=0
# incert=int(input())
#
# for x in range(1,incert+1,1):
#     s += x
# print(s)

#실습) 합이 1부터 100까지 합이 2000이 넘을대 수를 출력

# s=0
#
# for x in range(1,101,1):
#     s +=x
#     if s>2000:
#         break
# # print('x=',x,'s=',s)
# print(s-x)

#실습)바보라는 글자가 발견되면 강퇴
#처음 한거
# data=['안녕','반가워','방가','헬로','오늘만나']
# bad=['바보','멍청이','안녕']
# incert=input()
#
# for x in data:
#     print(x)
#     if x in bad:
#         print('강퇴')
#         break
# else:   #for문이 정상수행했다면 break문을 실행하지 않았을때
#     print('바른말사용')

#2번째한거------------------------------------------
# bad=['바보','멍청이']
# incert=input()
#
# for x in bad:
#     # print(x)
#     if x in incert:
#         print('강퇴')
#         break
# else:   #for문이 정상수행했다면 break문을 실행하지 않았을때
#     print('바른말사용')
#-------------------------------------------------

#continue
# data=[3,4,6,8,7,10]
#
# for x in data:
#     # if x%2 ==0:
#     if x % 2 == 1: continue #홀수이면 리턴 (스킵된다) 즉 참일때 스킵
#     print(x)

#실습) 어떤학생의 점수리스트가 주어졌을대 모든점수가 60점이 넘으면 합격하는 프로그램을 작성하시오
#예 점수리스트 [65,45,95,55,70]
        #또는 [68,78,86,72]

# data=[70,70,50,90,85]
#
# print(data)
# for x in data:
#
#     if x<60:
#         print('불합격입니다')
#         break
# else:
#     print('합격')
#-----------------------------------------------

#실습)강사님이하신거------------------------
# data = [65,88,45,90,70]
# # data=input('점수는?').split()
# #print(data)
# data = map(int , data)
# for x in data:
#     # print(x)
#     if x<60:
#         print('불합격')
#         break
# else:
#     print('합격')
#------------------------------------------------------

#-----------------------------------------------------
#set: 중복데이터 허용불가
# asia = {'한국','중국','일본'}
# asia.add('베트남')
# asia.add('중국')
# asia.remove('일본')
# asia.update({'한국','중국','태국'})       #업데이트는 넣는거  여러개 넣을때
# print(asia)
#-----------------------------------------------------

#----------------------------------------------------------
#실습 어떤 학생의 점수리스트가 주어졌을때 모든점수의 합계과 300점이 넘으면 합격하는 프로그램 작성
# 점수 [50,20,20,10,20]
# s=0
# data=[50,10,10,70,50]
# for x in data:
#     # print(x)
#     s += x
#     # print(s)
#     if s>300:
#         print('합격입니다')
#         break
# else:
#     print('불합격입니다')
#-----------------------------------------------------