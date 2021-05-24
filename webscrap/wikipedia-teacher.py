class Wikipedia(object):

    url = ''   # 인공지능을 위해서는 최대한 간결한 코딩이 중요 -> 생성자에 표기하지 않고 클래스 변수로

    def __str__(self):
        return f'Input url: {self.url}'

    @staticmethod
    def main():
        wikipedia = Wikipedia()  # 생성자는 표기하지 않았어도 바로 호출 가능.
        # menu = int(input('0. Exit\n 1.Input URL\n 2. Print URL '))
        # 이렇게 하면 아래 메뉴를 선택하고 나서 다시 menu가 실행되지 않는다.
        while 1:
            menu = int(input('0. Exit\n 1.Input URL\n 2. Print URL ')) # 여기에 위치해야 함
            if menu == 0:
                break
            elif menu == 1:
                wikipedia.url = input('url을 입력하세요')
            elif menu == 2:
                print(wikipedia.__str__())
            else:
                print('다시 입력하세요')
                continue

Wikipedia.main()




