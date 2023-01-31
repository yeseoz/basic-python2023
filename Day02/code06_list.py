# 복합형

# 리스트 = 배열 
arr= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(arr)
sum = 0
for i in arr:
    sum +=i

print(sum)

arr1 = [1,2,3]
arr2 = [1.1,2.2,3.3]
arr3 = ['Hello',13,'World!',True]

print(arr3)
print(type(arr3))

arr4 = [] # 빈 리스트
arr5 = list()
print(arr5)

arr6 = [1,2,3,4,[6,7,8,[9,10]]]
print(arr6)

arr7 = [[1,2,3,4],[5,6,7,8]]
print(arr7)

# 튜플
tuple1 = (1,2,3,4)
print(tuple1)

arr5.append(4)
print(arr5)

# 주석 단축기 ctrl + k + c
# tuple1.append(4) 튜플은 수정, 변경할 수 없음 (리스트는 가능)
# 결과값을 만들 때 사용하기 위해 만들어진게 아닐까?

print(type(tuple1))

# 딕셔너리 => 비순차적 for문으로 함부로 돌릴 수 없음
spiderman = {'name' : 'Peter Parker',
              'age' : 18,
           'weapon' : 'Web Shooter'}

print(spiderman)
print(spiderman['weapon'])
print(type(spiderman))

# 집합
set1 = set([1,2,3,4,])
print(set1)

set1 = set("Hello World")
print(set1)

