# 매개변수 개수 일정치 않은 경우
def add(*args):
    result = 0
    for i in args:
        result += i

    return result

print(add(1,2,3,4,5))
print(add(1,2,3,4,5,6,7,8,9,10))