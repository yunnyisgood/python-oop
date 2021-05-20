'''
이름, 전화번호, 이메일, 주소를 받아서연락처 입력, 출력, 삭제하는 프로그램을 완성하시오.
'''


class Contacts(object):
    def __init__(self, name, phone, email, add):
        self.name = name
        self.phone = phone
        self.email = email
        self.add = add


    def get_contacts(self):
        return f'이름:{self.name}, 전화번호 : {self.phone}, 이메일:{self.email}, ' \
               f'주소: {self.add}'


    @staticmethod
    def main():  #  만약 1번을 누르면 입력받고 출력되도록.
        while 1:
            menu = int(input('0. 종료\n 1. 입력\n 2. 출력 '))  # 이자리는 항상 실행되어야 하는 부분

            if menu == 0:  # if부터 조건 시작
                print('프로그램이 종료됩니다')
                break
            elif menu == 1: # 입력과 출력을 분리해서 실행한다.
                c = Contacts(input('이름'), input('전화번호'), input('이메일'), input('주소'))
            elif menu == 2:
                print(f'출력결과-> {c.get_contacts()}')
            else:
                print('다시 입력해주세요')

        # c = Contacts(input('이름'), input('전화번호'), input('이메일'), input('주소'))
        # print(c.get_contacts())
        # c2 = Contacts(input('이름'), input('전화번호'), input('이메일'), input('주소'))
        # print(c2.get_contacts())


Contacts.main()







