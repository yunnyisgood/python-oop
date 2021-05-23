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

    def del_contacts(ls, name):
        for i, j in enumerate(ls):  # 이때 i는 인덱스 번호(순서를 가리킴), j는 요소
            if j.name == name:  # 같은지 확인할 때는 요소가 필요
                del ls[i]  # 삭제할 때는 인덱스 번호가 필요


    @staticmethod
    def main():  #  만약 1번을 누르면 입력받고 출력되도록.
        ls = []
        while 1:
            menu = int(input('0. 종료\n 1. 입력\n 2. 출력\n  3. 수정\n 4. 삭제 '))  # 이자리는 항상 실행되어야 하는 부분

            if menu == 0:  # if부터 조건 시작
                print('프로그램이 종료됩니다')
                break

            elif menu == 1: # 입력과 출력을 분리해서 실행한다.
                # 리스트 ls에 입력받은 값인 c를 추가해 ->
                ls.append(Contacts(input('이름'), input('전화번호'), input('이메일'), input('주소')))

            elif menu == 2:
                for i in ls:
                    print(f'출력결과-> {i.get_contacts()}')

            elif menu == 3:  # 삭제 기능자체가 finite -> 그럼 while이 아닌 for문을 사용
                name = input('수정할 이름: ')
                edit_info = Contacts(name, input('전화번호'), input('이메일'), input('주소'))
                Contacts.del_contacts(ls, name)
                ls.append(edit_info)  # 새로 수정한 정보를 추가한다.

            elif menu == 4:  # 삭제 기능자체가 finite -> 그럼 while이 아닌 for문을 사용
                name = input('삭제할 이름: ')
                Contacts.del_contacts(ls, name)
                print('삭제가 정상적으로 실행하였습니다')

            else:
                print('다시 입력해주세요')



Contacts.main()







