# 클래스 생성

class Person:
    #pass  # 단순히 오류를 없애기 위해서 pass
    name  = '익명' #속성 변수
    height = ''
    gender = ''
    blood_type = 'A'

# 1. 생성자 추가
    # def __init__(self) -> None:
    #     self.name = '홍길동'
    #     self.height = '170'
    #     self.gender = 'male'
    #     self.blood_type = 'AB'

# 2. 파라미터를 받는 생성자 실행
    def __init__(self, name = '홍길동', height = '170', gender = 'male') -> None: # 매개변수
        self.name = name
        self.height = height
        self.gender = gender

    def walk(self): # self 파라미터 무조건 들어가야함 함수에는 없음 클래스에만 있음
        print(f'{self.name}이(가) 걷습니다.')

    def run(self,option):
        if option == 'Fast':
            print(f'{self.name}이(가) 빨리 뜁니다!!!!')
        else:
            print(f'{self.name}이(가) 천천히 뜁니다.')

    def stop(self):
        print(f'{self.name}이(가) 멈춥니다.')

# 3. 생성자외 매직 메서드(펑션) __str__
    def __str__(self) -> str:
        return f'출력: 이름은 {self.name}, 성별은 {self.gender}'

yeseo = Person() # 객체를 생성 하면 실체(instance)가 만들어짐
yeseo.name = '예서'
yeseo.height = '158'
yeseo. gender = 'female'
yeseo.blood_type = 'RH+ O'

print(f'{yeseo.name}의 혈액형은 {yeseo.blood_type} 입니다.')
yeseo.run('Fast')

# 1. 초기화 후 객체 생성
hong = Person()
hong.run('Slow')

print('============================')
# 2. 파라미터를 받는 생성자 실행
ashely = Person('ashely', '170', 'female')
print(ashely.name)
print(ashely.height)
print(ashely.gender)
print(ashely.blood_type)
print(ashely)