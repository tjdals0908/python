#class : 객체를 만들기 위한 틀
class Car:
    #속성: 필드
    name ='아오닉스5'
    color ='실버'
    pw=False
    #기능:메소드
    def power(self):
        pw = not Car.pw

c1=Car()
print(c1.name)
c2=Car()
print(c2.power())