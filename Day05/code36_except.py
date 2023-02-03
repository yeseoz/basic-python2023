# 예외 처리
def add(a,b):
    return a + b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

try:
    x,y = input('두 수를 입력하세요 > ').split()
    x = int(x)
    y = int(y)
except Exception as e:
    print(e)
    exit()
finally:
    print('계속되나요?') # 계속 됩니다! 그리고 exit() 실행됨

# if y == 0: # 원시적인 방법
#     print('y에 0을 넣지 마세요')
#     exit()

print('계산 테스트')
try:
    print(div(x, y))
except ZeroDivisionError as e: # 원하는 예외마다 다른 메시지를 처리하고 싶은경우
    print('0으로 나누면 안되요!')
except Exception as e: # Exception 클래스에서 자동으로 error 메시지 띄어줌  => 맨마지막에 처리해 줘야함
    print(e)
finally: # try문에서 예외가 발생하든 안하든 나온다.  => 네트웍통신이나 DB연결 할때 사용
    print('계산은 계속됩니다!!')


print(add(x, y))
print(mul(x, y))