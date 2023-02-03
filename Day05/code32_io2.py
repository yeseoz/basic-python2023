# 다중 입력
# x, y = input('두 영단어를 입력 하세요 > ').split() # 공백으로 하는것이 일반적이다.

# print(x)
# print(y)

# 완전 다중입력 (갯수 상관 없음)
inputs = list(map(str, input('단어를 입력하세요 > ').split())) # map() 들어오는 값을들 나열해 줌

print(inputs)

inputs = list(map(int, input('정수를 입력하세요 > ').split()))

print(inputs)
