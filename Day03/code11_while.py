# while문
hit = 0

while hit < 11:
    hit += 1 
    print(f'나무를 {hit}번 찍었습니다.')
    
    if(hit == 10):
        print('나무가 넘어갔습니다!!!')
        break
    else:
        print('나무가 아직 넘어가지 않았습니다. 끈질긴 놈')

print('나무찍기 완료')
