# 루틴 구조 -> 한 함수가 입출력을 동시에 할 수 있다.
def add_function(first, second): # self 없음 -> 루틴구조는 property가 없다.
    return first + second

def sub_function(first, second):
    return first - second

def mul_function(first, second):
    return first * second

def div_function(first, second):
    return first / second


#  서브 루틴 구조 -> 입력과 출력을 담당하는 함수들을 분리
class Calculator:

    def setdata(self, first, second):
        self.first = first  # 여기서 self는 property -> 서브루틴 구조는 property를 갖는다.
        self.second = second

    def add(self):
        return c.first + c.second

    def sub(self):
        return c.first - c.second

    def mul(self):
        return c.first * c.second

    def div(self):
        return c.first / c.second

if __name__ == '__main__':
    print(add_function(2, 4))
    print(sub_function(2, 4))
    print(mul_function(2, 4))
    print(div_function(2, 4))

    c = Calculator()
    # c.setdata(1, 2)
    # print(c.add())
    # print(c.sub())
    # print(c.mul())
    # print(c.div())
