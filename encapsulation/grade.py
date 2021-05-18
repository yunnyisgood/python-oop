class Grade:

    def __init__(self, kor, math, eng):
        self.kor = kor
        self.math = math
        self.eng = eng


    def sum(self):
        return self.kor + self.math + self.eng

    def avg(self):
        return self.sum()/3

    def get_grade(self):
        score = int(self.avg())
        grade = ''
        if score >= 90:
            grade = 'A학점'
        elif score >= 80:
            grade = 'B학점'
        elif score >= 70:
            grade = 'C학점'
        elif score >= 60:
            grade = 'D학점'
        elif score >= 50:
            grade = 'E학점'
        else:
            grade = 'F학점'

        return grade


    @staticmethod
    def main():
        g = Grade(int(input('국어점수 입력')), int(input('수학점수 입력')), int(input('영어점수 입력')))
        print(f'총점:{g.sum()}')
        print(f'평균:{g.avg()}')
        print(f'총점:{g.get_grade()}')

        # print(f'{g.kor}+{g.math}+{g.eng}={g.sum()}')
        # print(f'({g.kor}+{g.math}+{g.eng})/3={g.avg()}')


Grade.main()
