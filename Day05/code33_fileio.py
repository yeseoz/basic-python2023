# 파일 만들기
file = open('../sample07.txt','w', encoding='utf-8') # 파일 쓰기로 만듦

file.write('안녕하세요~\n')
file.write('와~ 두번째 파일이다!!\n')
file.write('절대경로에 파일이 생성될겁니다.\n')


file.close()
print('smaple01.txt이 생성되었습니다.')
# 글자/인코딩
# ASCII -> 한단어를 표현하는 체계(영어)
# UNICODE(UTF-8) -> 모든 나라언어를 다 표현 가능 

# 파일/ 폴더 경로
# 절대 경로 : root 폴더 부터 모든 경로를 다 적어주는 것
# 상대 경로 : 내 위치를 기준으로 경로 설정

