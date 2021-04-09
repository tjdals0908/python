#딕셔너리   (제이슨오브젝트)

data = {'a':10,'b':20,'c':30,'d':40}    #'변수명':10   콜론으로 대입시킬수있다

#딕셔너리는 기본적으로 순서가 없다 그래서 [1:5] 출력이 안된다

print(data['d'])



# data= {'홍길동':[20,165,5],'이순신':[45,170,6]}
#
# print(data['홍길동'])
#
# print(data['홍길동'][0])

# data= {'홍길동':{'나이':20,'키':165.5},'이순신':{'나이':45,'키':170}}
#
# print(data['홍길동']['나이'])
#
# data= {1:['홍길동',20,165,5],2:['이순신',45,170]}
#
#
# #딕셔너리 데이타 추가
# data={}
# data['홍길동']=20
# data['이순신']=[45,170,8]
#
# print(data)


#실습) 컴퓨터 언어를 입력받아 딕셔너리에 저장
# {'backend':'java' , 'fornted': 'html5'}


# lang={}; front={}
# back = input('backend언어는')
# fron = input('fronted d언어는')
#
# lang['backend'] = back
#
# front['fronted']=fron
#
# print('backend언어는',lang,'fronted언어는',front)



#
data={1:'고질라',2:'귀멸의칼날',3:'더박스'}        #키는 앞 , 벨류스는 뒤쪽
print(list(data.keys()))
print(list(data.values()))


print(list(data.values())[0])  #벨류 인덱스 출력


#연습중

lang={}; back={}

langIn=input()
backIn=input()

lang['backed'] = langIn
back['front'] = backIn

print(lang)

