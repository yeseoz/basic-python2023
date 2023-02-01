# for문
arr = [1, 2, 3, 4, 5]
sum = 0

for item in arr:
    print(f'{item:2.2f}')
    sum += item

print('합계는',sum)

# 홀짝
vals = [i for i in range(1, 11)] # 리스트를 편하게 만드는 방법
print(vals)

#continue / break  # 반복문에만 사용 if문에는 사용 불가능
num = 0
for item in vals:
    num += 1
    if num % 2 == 0:
        #continue # 이후의 것을 수행하지 않고 다시 for문으로 감
        break # vreak를 만나면 for문을 완전히 탈출    
    else:
        print(num,'번 수는', item, '입니다.')
