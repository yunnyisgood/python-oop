class Fruit(object):
    def __init__(self, color, fruit):
        self.color = color
        self.fruit = fruit


    def get_fruits(self):
        return f'색깔: {self.color}, 과일이름: {self.fruit}'


    @staticmethod
    def main():

        while True:
            select = input('1. apple 2. cherry 3. watermelon')
            if select == '1':
                f = Fruit(input('색깔을 입력하세요'), input('과일이름을 입력하세요'))
                print(f.get_fruits())
            elif select == '2':
                f = Fruit(input('색깔을 입력하세요'), input('과일이름을 입력하세요'))
                print(f.get_fruits())
            elif select == '3':
                f = Fruit(input('색깔을 입력하세요'), input('과일이름을 입력하세요'))
                print(f.get_fruits())
            else:
                print('다시 입력하세요')


Fruit.main()