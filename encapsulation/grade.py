class Grade:
    def setGrade(self, kor, math, eng):
        self.kor = kor
        self.math = math
        self.eng = eng

    def sum(self):
        return self.kor + self.math + self.eng


    def avg(self):
        return g.sum()/3

if __name__ == '__main__':
    g = Grade()
    g.setGrade(100, 90, 80)
    print(g.sum())
    print(g.avg())
