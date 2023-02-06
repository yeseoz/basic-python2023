# 콘솔 출력 보충
# 이스케이프 캐릭터 (탈출 문자)
print('1. Hello.\r\nWorld')
print('2. Hello.\nWorld') # 권장


print('3. Hello.\n\tWorld') # t 탭
print('4. Hello.\n\t\bWorld') # b 백스페이스

print('5. Hello.\n\'World\'') # 문자열내 홑따옴표
print('6. Hello. "World"')  # 6, 7번 동일
print("7. Hello.\n\"World\"")

print('7. Hello. \\ World') # \를 문자열에 표현
print('8. Hello\0') # 문자열의 마지막을 표현

# 파이썬과 같은 최신언어는 쓸 필요 잘없음 
# C, C++, JAVA 같은 언어는 사용안하면 문제가 생기는 경우가 있음

# 문자열 포맷팅 - 구닥다리
# %로 포맷코드를 시작함
me = '저'
name = '예서'
age = 27
print('%s는 %s 입니다. %d살 입니다.'%(me, name, age)) # 순서를 바꾸면 안됩니다.

print(f'{254.112233:.2f}') # 최신식 방법

print('%4.4f'%(254.112233)) # 구식 전체자리수. 소수점
