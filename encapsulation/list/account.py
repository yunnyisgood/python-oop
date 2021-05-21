import random


class Account(object):
    def __init__(self, customer, balance):
        self.customer = customer
        self.balance = balance
        self.bank_name = 'SC은행'

        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account_number = num1 + '-' + num2 + '-' + num3



    def get_account(self):
        return f'<생성된 계좌정보>\n 은행이름: {self.bank_name}\n 계좌번호: {self.account_number}\n' \
               f'예금주: {self.customer}, 초기잔액: {self.balance}'


    @staticmethod
    def main():
        account_lists = []
        while True:
            select = input('0. 종료\n 1. 입력\n 2. 출력\n 3.수정\n 4.삭제')
            if select == '0':
                print('프로그램 종료됩니다')
                break
            elif select == '1':
                account_lists.append(Account(input('예금주를 입력하세요'), input('초기잔액을 입력하세요')))
            elif select == '2':
                for i in account_lists:
                    print(i.get_account())
            elif select == '3':
                edit_name = input('성함을 입력해주세요')
                edit_info = Account(input('예금주를 입력하세요'), input('초기잔액을 입력하세요'))
                for i, j in enumerate(account_lists):
                    if j.customer == edit_name:
                        del account_lists[i]
                        account_lists.append(edit_info)
            elif select == '4':
                del_name = input('성함을 입력해주세요')
                for i, j in enumerate(account_lists):
                    if j.customer == del_name:
                        del account_lists[i]
                        print('삭제가 완료되었습니다.')
            else:
                print('다시입력하세요')
                continue


Account.main()
