# if문
name = '다원'
state = '아픔'

if name == '예서':
    print('진료실에서 담당의사를 만납니다.')
    if state == '아픔':
        print('주사실로 갑니다.')
    else:
        print('나가세요')
elif name == '다원':
    print('주사실로 갑니다.')
else :
    print('조용히 기다립니다.')
