class CalculatorStatic(object): # object 생략가능하지만,하는것을 추천
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        return self.first / self.second

    @staticmethod   # static 메소드 -> 변경 불가능, self 없음
    def main():
        calc = CalculatorStatic(int(input('첫번째 수 입력')), int(input('두번째 수 입력')))
        print(f'{calc.first}+{calc.second}={calc.add()}')
        print(f'{calc.first}-{calc.second}={calc.sub()}')
        print(f'{calc.first}*{calc.second}={calc.mul()}')
        print(f'{calc.first}/{calc.second}={calc.div()}')

CalculatorStatic.main()
