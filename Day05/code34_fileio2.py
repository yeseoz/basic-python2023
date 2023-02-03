# 파일 읽어 오기
file = open('./Day05/sample05.txt','r', encoding = 'utf-8')

while True:
    text = file.read()
    
    if not text: break

    print(text)

file.close() # 파일을 open 하면 반드시 close 해야함
