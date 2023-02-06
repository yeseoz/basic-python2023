import os

# 2. 주소록 시작 클래스 생성
class Contact:
    def __init__(self, name, phone_num, email, addr): # 생성자 선언
        self.__name = name
        self.__phone_num = phone_num
        self.__email = email
        self.__addr = addr

        # 3. str 재정의 => 인스턴스 변수에 저장된 정보를 화면에 출력하기 위해
    def __str__(self):
        str_res = (f'이  름: {self.__name}\n'
                   f'핸드폰: {self.__phone_num}\n'
                   f'이메일: {self.__email}\n'
                   f'주  소: {self.__addr}')
        return str_res
    
    # 8. Contact클래스에서 __name에 접근할 수 있도록 하기
    def isNameExist(self,name):
        if self.__name == name:
            return True
        else:
            return False

# 10. 각 멤버변수 접근하는 함수
    def getName(self) -> str:
        return self.__name
    
    def getPhoneNum(self) -> str:
        return self.__phone_num
    
    def getEmail(self) -> str:
        return self.__email
    
    def getAddr(self) -> str:
        return self.__addr

# 5. 정보 입력 받기
def set_contact():
    name, phone_num, email, addr = input('정보입력(이름, 폰번호, 이메일, 주소(구분자/) ').split('/')
    #print(name, phone_num, email, addr)
    contact = Contact(name, phone_num, email, addr)
    return contact

# 6. 메뉴 만들기
def get_menu():
    str_menu = ('주소록 프로그램 v0.1\n'
                '1. 연락처 추가\n'
                '2. 연락처 출력\n'
                '3. 연락처 삭제\n'
                '4. 종료\n')
    print(str_menu)
    menu = input('메뉴입력: ')
    return int(menu)


# 7. 연락처 출력하기
def get_contacts(lst_contact):
    for item in lst_contact:
        print(item)
        print('==================')

# 9. 연락처 삭제하기
def del_contact(lst_contact,name):
    for i, item in enumerate(lst_contact):
        if item.isNameExist(name):
            del lst_contact[i]

# 11. 파일 db 연결
def save_contacts(list):
    file = open('C:/Users/LG/Documents/GitHub/studyPython2023/Study/contacts.txt','w', encoding='utf-8')
    for item in list:
        text = f'{item.getName()}/{item.getPhoneNum()}/{item.getEmail()}/{item.getAddr()}'
        file.write(f'{text}\n')

    file.close()

# 12. 주소록 연결
def load_contacts(list):
    try: # 15-1 파일이 없어서 생기는 예외는 파일생성하고 함수를 빠져나감
        file = open('C:/Users/LG/Documents/GitHub/studyPython2023/Study/contacts.txt','r', encoding='utf-8')
    except Exception as e: 
        # print('contacts.txt 파일이 없습니다.')
        # print('파일을 생성하고, 다시 실행하세요.') # 안조아
        # exit()
        f = file = open('C:/Users/LG/Documents/GitHub/studyPython2023/Study/contacts.txt','w', encoding='utf-8')
        f.close()
        return

    while True:
        line = file.readline().replace('\n','') #15. 문장끝 \n 제거
        if not line: break

        lines = line.split('/')
        contact = Contact(lines[0], lines[1], lines[2], lines[3])
        list.append(contact)

    file.close()

# 추가 
def clearConsole():
    command = 'clear'
    if os.name in('nt', 'dos'):
        command = 'cls'
    os.system(command)

# 4. 실행
def run():
    lst_contact = []
    load_contacts(lst_contact)
    clearConsole()
    #first = Contact('예서', '010-9167-6132', 'kys021697@naver.com','경남 김해시')
    #set_contact()
    while True:
        sel_menu = get_menu()
        if sel_menu == 1:
            clearConsole()
            contact = set_contact()
            lst_contact.append(contact)
            input()
            clearConsole()
        elif sel_menu == 2:
            clearConsole()
            get_contacts(lst_contact)
            input()
            clearConsole()
        elif sel_menu == 3:
            clearConsole()
            name = input('삭제할 이름을 입력하세요: ')
            del_contact(lst_contact, name)
            input()
            clearConsole()
        elif sel_menu == 4:
            save_contacts(lst_contact)
            break

# 1. 프로그램 시작
if __name__ == '__main__':
    #print('프로그램을 시작합니다.')
    run()
#print('프로그램을 종료합니다.')