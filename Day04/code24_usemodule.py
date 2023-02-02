# 모듈 사용   모듈은 무조건 클래스로 되어 있진 않음 / 클래스로 된 것과 아닌 것을 사용할 수 있어야함
import math as m  # 클래스로 안된 모듈 
import code22_person as p # 우리가 만든 클래스
from code23_car import Car # 쓰고 싶은 클래스만 골라서 사용가능

print(m.pi)

print(m.tan(0))
print(m.ceil(3.1)) # 올림 => 4
print(m.pow(2, 10)) # = print(2 ** 10)

# 우리가 만든 모듈을 사용 (생성자를 사용해야함)
me = p.Person('홍길순',155,'여성')
print(me) 

mycar = Car()
print(mycar)

