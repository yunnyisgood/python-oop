class Wikipedia(object):
    def __init__(self, url):
        self.url = url

    def __str__(self):
        return f'Input url: {self.url}'

    @staticmethod
    def main():
        # menu = int(input('0. Exit\n 1.Input URL\n 2. Print URL '))
        # 이렇게 하면 아래 메뉴를 선택하고 나서 다시 menu가 실행되지 않는다.
        while 1:
            menu = int(input('0. Exit\n 1.Input URL\n 2. Print URL ')) # 여기에 위치해야 함
            if menu == 0:
                break
            elif menu == 1:
                wikipedia = Wikipedia(input('url을 입력하세요'))
            elif menu == 2:
                print(wikipedia.__str__())
            else:
                print('다시 입력하세요')
                continue

Wikipedia.main()




