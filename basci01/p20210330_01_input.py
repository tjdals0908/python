
#사용자에게 입력받기

# a=input('이름은 입력해주세요')
#
# print('입력한값은',a)

#실습 나이를 입력받아 화면에 출력

# age=input('나이를입력해주세요')
#
# print('당신의나이는',age,'입니다',sep='')  #


#날씨를 입력받아 오늘의 날씨 출력

# weather=input('날씨입력')
#
# txt='오늘의 날씨는'
#
# print(txt,weather,sep='')

#도움말 출력
# help(input)


#사용자가 입력한 값에 100울 더해서 출력
# a=input('숫자는?')        # 입력되면 input은 문자로 인식
# a=int(a)                #int는 정수로 변환해주는 함수
# a=float(a)                #실수로 형변환해서 반환 해줌
# print(a+100)

#실습1 두수를 입력받아서 사칙연산프로그램
# in1 = int(input('숫자를입력'))
# in2 = int(input('숫자를입력'))
#
# print('%d+%d=%d'%(in1,in2,in1+in2))
# print('%d-%d=%d'%(in1,in2,in1-in2))
# print('%d*%d=%d'%(in1,in2,in1*in2))
# print('%d/%d=%.2f'%(in1,in2,in1/in2))

# print('두수의합은',in1+in2)
# print('두수의곱하기는',in1*in2)
# print('두수의나누기는',in1/in2)
# print('두수의빼기는',in1-in2)

# data = input('두수를 입력해주세요').split()

# a= int(data.split()[0])
# b= int(data.split()[1])
# print(a,'+',b,'=',a+b)

# print(data[0])  #0번 인덱스
# print(data[1])  #1번 인덱스
#
# # a,b=map(int,data) #data의 각값을 int 함수를 적용한후 a,b에 대입
#
# print(data)
#
# print(data[0],'+',data[1]) #인덱스 입력해수 출력

# a,b = map(int,data)
# print(data[0],data[1])

r= float(input('반지름을 입력해주세요'))

print(r*r*3.14)

print(r**2*3.14)   #r의 값을 **숫자  하면 r을 숫자만큼 곱한다

