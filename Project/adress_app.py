# 주소록 앱
# 2023-02-06
# Yeseo

# 15. 예외처리 
# 15-1 파일 없을 때 나는 예외
# 15-2 입력시 / 개수가 다를 때 예외
# 15-3 메뉴번호 입력 숫자외 예외

import os # 운영체제용 모듈

# 2. 클래스 생성                                 
class Contact:
    # 생성자 - 이름, 전번, 이메일,주소
    def __init__(self, name, phone_num, email, addr) -> None:
        self.__name = name
        self.__phone_num = phone_num
        self.__email = email
        self.__addr = addr

    # 4. __str__ 재정의
    def __str__(self) -> str:
        str_res = (f'이  름: {self.__name}\n'
                   f'핸드폰 : {self.__phone_num}\n'
                   f'이메일 : {self.__email}\n'
                   f'주  소 : {self.__addr}')
        return str_res

    # 10. 객체 존재여부 확인 / 클래스 함수
    def isNameExist(self, name):
        if self.__name == name:
            return True
        else:
            return False

    # 12. 각 멤버변수 접근하는 함수
    #getName, getPhoneNum, getEmail, getAddr
    def getName(self) -> str:
        return self.__name
    
    def getPhoneNum(self) -> str:
        return self.__phone_num
    
    def getEmail(self) -> str:
        return self.__email
    
    def getAddr(self) -> str:
        return self.__addr

# 5. 사용자 입력
def set_contact():
    name, phone_num, email, addr = input('정보입력(이름, 전번, 이메일, 주소[구분자/] : ').split('/')
    #print(name, phone_num, email, addr)
    # 7. Contact 객체 만들기
    contact = Contact(name, phone_num, email, addr)
    return contact

# 9. 주소록 출력
def get_contacts(list):
    for item in list:
        print(item)
        print('==========')

# 10. 주소록 삭제
def del_contact(list, name):
    count = 0 
    for i, item in enumerate(list): # 리스트 인덱스 추가생성
        if item.isNameExist(name):
            count += 1
            del list[i] # 리스트 삭제

    if count > 0: # 11. 
        print('삭제했습니다.')
    else: print('삭제할 주소록이 없습니다.')

# 13. 주소록 파일 저장
def save_contacts(list):
    file = open('C:\Source\studyPython2023\Project\contacts.txt','w', encoding='utf-8')
    for item in list:
        text = f'{item.getName()}/{item.getPhoneNum()}/{item.getEmail()}/{item.getAddr()}'
        file.write(f'{text}\n')

    file.close()

# 14. 주소록 읽어오기
def load_contacts(list):
    try: # 15-1 파일이 없어서 생기는 예외는 파일생성하고 함수를 빠져나감
        file = open('C:\Source\studyPython2023\Project\contacts.txt','r', encoding='utf-8')
    except Exception as e: 
        # print('contacts.txt 파일이 없습니다.')
        # print('파일을 생성하고, 다시 실행하세요.') # 안조아
        # exit()
        f = file = open('C:\Source\studyPython2023\Project\contacts.txt','w', encoding='utf-8')
        f.close()
        return

    while True:
        line = file.readline().replace('\n','') #15. 문장끝 \n 제거
        if not line: break

        lines = line.split('/')
        contact = Contact(lines[0], lines[1], lines[2], lines[3])
        list.append(contact)

    file.close()

# 추가. 화면 클리어를 위한 함수   *--콘솔프로그램이라면 항상 이렇게 만들어야함--*
def clear_console():
    command = 'clear' # Linux, Unix 화면 클리어 명령어
    if os.name in ('nt', 'dos'): # nt 거나 dos 라면 => windows 운영체제라면
        command = 'cls' # 윈도우 화면 클리어 명렁어

    os.system(command)    

# 6. 메뉴 표시
def get_menu():
    str_menu = ('주소록 앱 v0.5\n'
                '1. 연락처 추가\n'
                '2. 연락처 출력\n'
                '3. 연락처 삭제\n'
                '4. 앱 종료')
    print(str_menu)
    try:
        menu = int(input('메뉴 입력 : '))
    except Exception as e: # 숫자외 입력 예외 처리
        menu = 0 # 15-3 제대로 넣지 않으면 다 무시(모두다 0으로 바꿔버림)

    return menu


# 3. 전체 실행
def run():
    contacts = list() # 주소를 담기위한 빈 리스트 생성
    load_contacts(contacts) # 14. 주소록 읽어오기
    # temp = Contact('예서', '010-9167-6132','kys021697@naver.com',
    #                '김해시 삼계로...')
    clear_console()
    while(True):
        sel_menu = get_menu()
        if sel_menu == 1:
            #clear_console()
            try: # 15-2 연락처 입력 잘못했을 때 예외처리
                contact = set_contact()
                contacts.append(contact)
                input('주소록 입력 성공') # 아무것도  안받는 입력
            except Exception as e:
                print('이름/전번/이메일/주소순으로 똑바로 입력하세요.')
                input()
            finally:
                clear_console()
        elif sel_menu == 2:
            #clear_console()
            get_contacts(contacts)
            input('주소록 출력 완료')
            clear_console()
        elif sel_menu == 3:
            name = input('삭제할 이름 입력 : ')
            del_contact(contacts, name)
            input()
            clear_console()
        elif sel_menu == 4: #13. 종료시 주소록 파일 저장
            save_contacts(contacts)
            break
        else:
            clear_console() 

# 1. 메인실행영역
if __name__ == '__main__':
    # print('주소록 앱 시작합니다')
    run()


