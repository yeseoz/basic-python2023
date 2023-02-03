# 좀 더 복잡한 계산기
def calc(option, *args):
    result = 0
    if option =='add':
        for i in args:
            result += i

    elif option == 'mul':
        result = 1
        for i in args:
            result *=i

    elif option == 'sub': 
        result = args[0]
        for i in args[1:]:
            result -= i

    elif option == 'div':
        result = args[0]
        for i in args[1:]:
            result /=i

    return result

print(calc('add', 5, 7, 17)) # 29
print(calc('mul', 512, 4)) # 2048
print(calc('mul',512, 2, 2)) # 2048
print(calc('sub',10, 248, 396)) # -634
print(calc('div',100,5)) # 20.0

# 여러값을 리턴할 때는 튜플을 사용한다.
def new_calc(x,y):
    return(x*y, x/y, x+y, x-y)
# 받을 때는 튜플 (소괄호) 생략가능
res1, res2 ,res3, res4 = new_calc(5,7)
#(res1, res2 ,res3, res4) = new_calc(5,7)
print(res1,res2, res3, res4)
