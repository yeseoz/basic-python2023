# 람다 함수 (한번 쓰고 버릴 함수)
def add(x, y):
    return x + y

print(add(7, 4))

# 람다함수를 사용하면
print((lambda x, y : x + y)(7, 4))

# 지금은 쓰지말자 복잡하니..