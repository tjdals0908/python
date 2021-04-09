
#내장 함수

# data=[5,8,4,6]
# sum(data)   #sum 함수
# print(sum(data))    #sum 함수 프린트


#사용자 함수 mysum 정의 된거
# def mysum(a,hell):    #def 는 정의한다 ?
#     print('합계')
#     print(a,hell)
#
# #쓸려면 mysum 호출
#
# mysum(data)
#
# mysum(data,'hello') #오류가 난다 2개의 값이 있어서 그래서 mysum (매개변수에 2개 즉 넘기는거와 받는거 변수 수는 같아야한다)


#-----------강사님이 한거-----------------------
#사용자함수 sum정의:
# 매개변수:리스트, 반환값:합계
# data=[5,18,4,6]
# def mysum(data):
#     s=0
#     for x in data:
#         s += x
#     #print(s)
#     return s
# r=mysum(data)
#
# print('린턴값:',r)

#----------max함수 min함수--------------

# data=[5,18,4,6]
#
# max=max(data)
# print('가장큰값은',max)
# min=min(data)
# print('가장작은값은',min)
#---------------------

# def mymax(data):
#     max= data[0]
#
#     for x in data:
#         # print(x)
#         if x>max:
#             max=x
#     return max
#
# data = [5, 18, 4, 6]
#
# print('가장큰값은',mymax(data))


# def mymin(minData):
#     min=minData[0]
#     for y in minData:
#         if min>y:
#             min = y
#     return min
# data=[6,10,20,50,30,10]
#
# print(mymin(data))
#
# result=mymin(data)
# print(result)


#ord()함수
#한글은 유니코드체계
# print(ord('A'), len('A')),'A'.encode(),len('A'.encode())
# print(ord('가'), len('가'), '가'.encode(),len('가'.encode())) #인코드는 바이트단위로 변홤
#
# print(chr(44032))
#----------------------------------------------------------------------------

#실습) 산칙연산 함수 (매개변수는 : 두수, 반환값은 : 결과 )

# def add(a,b):
#     return a+b
#
# def sub(a,b):
#     return a-b
#
# a=int(input('처음숫자'))
# b=int(input('두번째 숫자'))
#
# print(add(a,b))
# print(sub(a,b))

#실습3) 월급 구하기
# 년봉,시급,초과근무시간을 매개변수로 받아 월급을 계산하고 반환하는 함수
# (월급 = 년봉/12 + 시급*초과근무시간)

def wor(year,time,over):
    return year/12+time*over

year=100000000
time=10000
over=5

print('월급은',wor(year,time,over))
#-----------------------------------------



