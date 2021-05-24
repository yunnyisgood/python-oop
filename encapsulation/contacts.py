class Contacts(object):
    def __init__(self, name, phone_num):
        self.name = name
        self.phone_num = phone_num

    def to_string(self):
        return f'이름: {self.name}, 전화번호: {self.phone_num}'


    def main():
        contacts = Contacts(input('이름을 입력하세요'), input('전화번호를 입력하세요'))
        print(contacts.to_string())

Contacts.main()


