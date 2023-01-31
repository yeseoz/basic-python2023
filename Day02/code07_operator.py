# 연산자
# 할당 연산 assignment
# 2 = 1 (X)
val = 1 # val 에 1이라는 값을 넣겠다.


# equal 연산자
print(1 == 1)

# 사칙연산
print(1 + 1)
print(1 - 1)
print(10 * 10)
print(1024 / 2) # 소수나누기
print(1024 // 2) # 정수나누기
print(4 // 3)
print(4 % 3) # 나머지

# print(6 / 0)  # 0을 나눌 수 없음. 무한대 값이 나옴 
# print(6 // 0)

print(2 ** 10) # 2^10

# 문자열 연산 -> 덧셈과 곱셈만 가능
first = 'Hello'
second = 'World'
print(first+second)
print(first+' '+second)
print(first,second)

print(first * 4)

#문자열 길이
print(len(first)) 
print(first[0])
print(first[1])
print(first[2])
print(first[3])
print(first[4])
#print(first[5]) 인덱스는 0 부터 시작하기 때문에 5는 존재 하지 않는다. 오류 실행

# 파이썬에서 인덱스를 찾는 특이한 방법
print(first[-1])
print(first[-2])
print(first[-3])
print(first[-4])
print(first[-5])

# 리스트 자르기(스플릿)
current = '2023-01-31 15:14:02' # 현재 시간
print(len(current))
print(current[0:4])
print(current[5:7])
print(current[8:10])
print(current[11:13])
print(current[14:16])
print(current[17:])

print(current[-19:-15])

# 리스트 연산
que = [1, 2, 3, 4, 5]
que[0] = 7

print(que)

# que 인덱스는 4까지 존재하기 때문에 인덱스 5에 값을 집어 넣을 수 없음
# que[5] = 10
# print(que)

que.append(10) # 맨 마지막에 값 추가
print(que)

que.insert(3, 99) # 특정 인덱스에 추가
print(que)

que.remove(3) # 특정 값 삭제
print(que)

# 문자열 == 문자 리스트
title = 'python'
print(title)

# title[0] = 'P' 문자 리스트는 변경이 불가능함.
print('P' + title[1:])

#튜플은 수정이 안됨
# tup = (1, 2, 3, 4, 5)
# tup[1] = 9

# print(tup)

# 문자열 포맷팅
print("I'm so happy {0} to you!!".format(2)) # 숫자(문자, 정수, 실수 ...)를 {0}로 표현? 컴퓨터 숫자는 0에서 시작되니까
# 최신식 문자열 포맷팅 -> 로그인 할때 인사? 000님 안녕하세요!
# 구식형을 쓰면 길이가 좀 길어집니다.
preword = 2
sayHello = 'Hey'
print(f"I'm so happy {preword} to you!!, {sayHello}!!") 

pi = 3.141592
print(f'파이는 {pi:0.2f}입니다.')
print(f'파이는 {pi:10.3f}입니다.')

# 문자열을 특정문자로 자르기
full_name = 'Yeseo. Kim'
vals = full_name.split() # space로 자르기
print(type(vals))
print(vals)

vals = full_name.split('.') # . 으로 자르기
print(vals)

print(full_name.replace('Yeseo.','YESEO.'))

# 문자열 공백 없애기 -> 검색창 공백이 앞에 들어갔을 때 없어버리는 용도로 사용
hi = '           Hello~ Bye~          '
print(hi.lstrip() + '|')
print(hi.rstrip() + '|')
print(hi.strip() + '|')

# 문자열에서 값을 찾기
print(full_name.index('s'))
print(full_name.find('e')) # 인덱스로 찾으면 없는 문자 오류나는데 find 쓰면 안남

# 찾는 단어의 개수
print(full_name.count('e'))

# 모든 단어를 대문자/소문자로 변경
print(full_name.upper()) # 대문자로 변경
print(full_name.lower()) # 소문자로 변경

# 연산자 우선 순위
print(3 + 4 * 2)
print((3 + 4) * 2)
