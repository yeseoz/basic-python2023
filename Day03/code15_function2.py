# 함수
# 함수 만드는 방법 4가지
# 1. 파라미터 o 리턴 o
# 2. 파라미터 o 리턴 x
# 3. 파라미터 x 리턴 o
# 4. 파라미터 x 리턴 x

def add(x, y): # 값을 돌려주지 않는 리턴은 리턴을 생략할 수 있음
    result = x + y
    print(result)

def sub(x, y):
    result = x - y
    print(result)

def mul(x, y):
    result = x * y
    print(result)

def div(x, y):
    result = x // y
    print(result)

def hello():
    print('Hello~!!!')
    return

def hello2():
    msg = 'Hello, Hello'
    return msg

# 함수 호출
hello()
print(hello2())

add(1024, 5)
sub(1024, 1000)
mul(512, 2)
div(108, 10)
