class CalculatorConstructor:

    # 생성자
    def __init__(self, first, second): # init 메소드라 불린다.
        self.first = first
        self.second = second

    def add(self):
        return c.first + c.second

    def sub(self):
        return c.first - c.second

    def mul(self):
        return c.first * c.second

    def div(self):
        return c.first / c.second

if __name__ == '__main__':    # 메인함수-> 실행포인트
    c = CalculatorConstructor(1, 2)  # c는 인스턴스라는 객체.
    print(c.add())
    print(c.sub())
    print(c.mul())
    print(c.div())





