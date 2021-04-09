
 #변수: 데이타를 저장하기위한 공간
 #변수명: 저장된 데이터를 접근하기 위한 이름
 #=: 대입연산자


# a = 10
#
# print(a)
#
# a= 'hello python'
#
# print(a)
# a=3.14
#
# print(a)
# 사칙연산 더하기 빼기 곱하기 나누기 퍼센트(나머지 구하는거) , //는 몫을 구하는거


# a=50
# b=3
#
# print('a+b=',a+b)
#
# print('a-b=',a-b)
#
# print('a*b=',a*b)
#
# print('a/b=',round (a/b,3) )
#
# # print('a/b=&d'%(a/b))
#
# print('a/b=%.2f'%(a/b))
#
#
# print('a&b=',a%b) #나머지
# print ('a//b=',a//b) #몫구하기

incert=10000
a=3600
b=60

sigan = incert//a
siganex = incert%a

min = siganex//b

sec = siganex&b


print(sigan,'시간')
print(min,'분')
print(sec,'초')

#
a=30; b=20

print(a,'+',b,'=',a+b)      #이렇게 되어잇는걸 포맷 문자로 변환해보자
print('%d+%d=%d'%(a,b,a+b))



#포맷문자열을 이용한 사칙연산

print('%d+%d=%d'%(a,b,a+b))
print('%d*%d=%d'%(a,b,a*b))
print('%d/%d=%d'%(a,b,a/b))
print('%d/%d=%.2f'%(a,b,a/b))  # f를 입력하고 .2를 하면  소숫점 2자리만 입력이 된다

print('%d %% %d=%.2f'%(a,b,a%b))



