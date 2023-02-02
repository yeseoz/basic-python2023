# 자동차 클래스

class Car:
    __number = '368서 5890'

    def get_number(self) -> str:
        return self.__number
    
    # 클래스 외부에선 변경 x, 멤버함수로는 내부를 조작o
    def set_number(self,number):
        self.__number = number
    
    def __init__(self, __number='368서 5890') -> None:
        self.__number = __number
        print('__init__')
        

    # def __new__(cls):
    #     print('__new__')
    #     return super().__new__(cls) # 부모클래스(상속)

    def __str__(self) -> str:
        return f'차번호는 {self.__number}'

yourcar = Car('88호 7645')
print(yourcar)
yourcar.__number = '54라 9999' #외부에서는 멤버변수에 접근 불가
print(yourcar)
print('클래스 내부함수 사용!')
yourcar.set_number('55오 5555')
print(yourcar)

mycar = Car()
print(mycar)
print(f'제차는 이거고 번호는 {mycar.get_number()}에용~')

mycar.__number = '132거 1234'
print(mycar)
