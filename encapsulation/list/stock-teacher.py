class Stock:
    def __init__(self, name, code, PER, PBR, stock_yield):
        self.name = name
        self.code = code
        self.PER = PER
        self.PBR = PBR
        self.stock_yield = stock_yield


    def to_string(self):
        return f'해당종목: {self.name}, 해당코드: {self.code}, ' \
               f'PER: {self.PER}, PBR: {self.PBR}, 배당수익률: {self.stock_yield}'

    @staticmethod
    def del_element(stock_lists, code):  # => Refactoring method
        for i, j in enumerate(stock_lists):
            if j.code == code:
                del stock_lists[i]


    @staticmethod
    def main():
        stock_lists = []
        while True:
            select = input('0. 종료\n 1. 입력\n 2.출력\n 3.수정\n 4.삭제')
            if select == '0':
               print('프로그램이 종료됩니다')
               break

            elif select == '1':
                stock_lists.append(Stock(input('종목'), input('종목코드'), float(input('PER')),
                                         float(input('PBR')), float(input('배당수익률'))))
            elif select == '2':   # for문을 이용하여 입력받은 데이터들을 쌓아 출력할 수 있다.
                for i in stock_lists:
                    print(f'생성된 주식의 {i.to_string()}')

            elif select == '3':
                code = input('수정할 종목 코드를 입력하세요')
                stock = Stock(input('종목이름'), code, float(input('PER')), float(input('PBR')), float(input('배당수익률')))
                stock.del_element(stock_lists, code)
                stock_lists.append(stock)

            elif select == '4':
                stock = Stock(None, input('종목코드'), None, None, None)
                # 생성자에 맞게 input 하지 않더라도 None으로 채워놓아야 한다.
                stock.del_element(stock_lists, stock.code)

                #  stock.del_element(stock_lists, input('삭제할 종목 코드를 입력하세요'))
                #  위의 처럼만 할 경우, stock이 없기 때문에 오류 발생

            else:
                print('다시 입력하세요')
                continue  # 없어도 실행은 되지만, 문법적으로 해두도록!


Stock.main()