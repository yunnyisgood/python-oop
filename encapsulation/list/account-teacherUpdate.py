import random


class Account(object):
    def __init__(self, acc_number, customer, balance):
        self.customer = customer
        self.balance = balance
        self.BANK_NAME = 'SC은행'  # 상수는 대문자로 선언한다.
        self.acc_number = acc_number

    def to_string(self):
        return f'<생성된 계좌정보>\n 은행이름: {self.BANK_NAME}\n 계좌번호: {self.acc_number}\n' \
               f'예금주: {self.customer}, 초기잔액: {self.balance}'

    '''
    계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성됩니다.
    '''
# 방법 1
    @staticmethod
    def create_acc_number():
        account_lists = [str(random.randint(0, 9)) for i in range(3)]
        account_lists.append('-')
        for i in range(2):
            account_lists.append(str(random.randint(0, 9)))
        account_lists.append('-')  # for문과 상관없이 무조건 수행해야하는 자리
        for i in range(6):
            account_lists.append(str(random.randint(0, 9)))
        return"".join(account_lists)  # 리턴되는 값들에 공백없이

# 방법 2
#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)
#
#         num1 = str(num1).zfill(3)
#         num2 = str(num2).zfill(2)
#         num3 = str(num3).zfill(6)
#         self.account_number = num1 + '-' + num2 + '-' + num3



    @staticmethod
    def del_accounts(account_lists, acc_number):
        for i, j in enumerate(account_lists):
            if j.acc_number == acc_number:
                del account_lists[i]


    @staticmethod
    def account_update(account_lists, balance, acc_number, select):
        for i, j in enumerate(account_lists):
            if j.acc_number == acc_number:  # 입금한 계좌번호가 리스트에 있다면
                if select == '3':
                    replace = Account(j.acc_number, j.customer, int(j.balance) + int(balance))
                    Account.del_accounts(account_lists, acc_number)
                    account_lists.append(replace)
                elif select == '4':
                    replace = Account(j.acc_number, j.customer, int(j.balance) - int(balance))
                    Account.del_accounts(account_lists, acc_number)
                    account_lists.append(replace)
                else:
                    print('Wrong Number')
                    continue


    @staticmethod
    def main():
        account_lists = []
        # account = Account()
        while True:
            select = input('0. 종료\n 1. 계좌개설\n 2. 계좌정보\n 3.입금\n 4.출금\n 5.계좌탈퇴 ')
            if select == '0':
                print('프로그램 종료됩니다')
                break

            elif select == '1':
                account_lists.append(Account(Account.create_acc_number(),
                                             input('예금주를 입력하세요'), input('초기잔액을 입력하세요')))

            elif select == '2':
                for i in account_lists:
                    print(i.to_string())

            elif select == '3':
                acc_number = input('입금할 계좌번호를 입력하세요')
                balance = input('입금액 입력하세요')
                Account.account_update(account_lists, balance, acc_number, select)

            elif select == '4':
                acc_number = input('출금할 계좌번호를 입력하세요')
                balance = input('출금액 입력하세요')
                Account.account_update(account_lists, balance, acc_number, select)

            elif select == '5':
                Account.del_accounts(account_lists, input('삭제할 계좌번호를 입력하세요'))
                print('삭제가 완료되었습니다.')

            else:
                print('다시입력하세요')
                continue


Account.main()
