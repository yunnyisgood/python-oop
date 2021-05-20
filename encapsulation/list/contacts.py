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
        menu = int(input('1. 주소록 추가\n 0. 프로그램 종료'))
        while True:
            c = Contacts(input('이름'), input('전화번호'), input('이메일'), input('주소'))
            print(c.get_contacts())

            if menu == 0:
                print('프로그램이 종료됩니다')
                break

        # c = Contacts(input('이름'), input('전화번호'), input('이메일'), input('주소'))
        # print(c.get_contacts())
        # c2 = Contacts(input('이름'), input('전화번호'), input('이메일'), input('주소'))
        # print(c2.get_contacts())


Contacts.main()







