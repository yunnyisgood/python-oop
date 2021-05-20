class Stock:
    def __init__(self, name, code, PER, PBR, stock_yield ):
        self.name = name
        self.code = code
        self.PER = PER
        self.PBR = PBR
        self.stock_yield = stock_yield


    def get_stocks(self):
        return f'해당종목: {self.name}, 해당코드: {self.code}, ' \
               f'PER: {self.PER}, PBR: {self.PBR}, 배당수익률: {self.stock_yield}'


    @staticmethod
    def main():
        stock_lists = []
        while True:
            select = input('0. 종료\n 1. 입력\n 2.출력\n 3.삭제')
            if select == '0':
               print('프로그램이 종료됩니다')
               break
            elif select == '1':
                stock_lists.append(Stock(input('종목'), input('종목코드'), float(input('PBR')),
                                         float(input('PER')), float(input('배당수익률'))))
            elif select == '2':   # for문을 이용하여 입력받은 데이터들을 쌓아 출력할 수 있다.
                for i in stock_lists:
                    print(f'생성된 주식의 {i.get_stocks()}')

            elif select == '3':
                del_name = input('삭제할 종목 이름을 입력하세요')
                for i, j in enumerate(stock_lists):
                    if j.name == del_name:
                        del stock_lists[i]  # 이 때 del 변수명은 list의 인덱스를 사용하여 삭제할 때 사용한다

            else:
                print('다시 입력하세요')
                continue  # 없어도 실행은 되지만, 문법적으로 해두도록!


Stock.main()