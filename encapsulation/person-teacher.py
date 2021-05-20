'''
이름, 출생년도, 주소를 입력받아서
회원가입한 사람의 이름, 나이, 주소를 출력하시오
'''

class Person(object):
    def __init__(self, name, birth, add):
        self.name = name
        self.birth = birth
        self.add = add

    def join(self):
        name = self.name
        add = self.add
        birth = int(2021 - self.birth)
        user = ['홍길동', 'abc', '마바사']
        info = ''

        if name in user:
            print(name, add, birth)
        else:
            print('다시 입력하세요')


    @staticmethod
    def main():
        userInfo = Person(input('이름을 입력하세요'), int(input('출생년도를 입력하세요')), input('주소를 입력하세요'))
        print(f'조회결과:{userInfo.join()}')

Person.main()

'''
만약에 입력을 받으면


'''