def bmi_function(height, weight):
    return weight / height ** 2 * 10000

class Bmi():

    def __init__(self, weight, height):
        self.weight = weight
        self.height = height  # height는 실체가 아닌, 변수

    '''
    고도 비만 : 35 이상
    중(重)도 비만 (2단계 비만) : 30 - 34.9
    경도 비만 (1단계 비만) : 25 - 29.9
    과체중 : 23 - 24.9
    정상 : 18.5 - 22.9
    저체중 : 18.5 미만   
    '''

    def get_bmi(self):
        standard = ''
        bmiScore = self.weight/self.height ** 2 * 10000

        if bmiScore>= 35:
            standard = '고도비만'
        elif 30 <= bmiScore <35:
            standard = '중도비만'
        elif 25 <= bmiScore <30:
            standard = '경도비만'
        elif 23 <= bmiScore <26:
            standard = '과체중'
        elif 18.5 <= bmiScore <23:
            standard = '정상'
        else:
            standard = '저체중'

        return bmiScore, standard

    @staticmethod
    def main():
        b = Bmi(int(input('몸무게를 입력하세요')), float(input('키를 입력하세요')))  # b에 실제값을 넣기 때문에 이때의 b를 인스턴스라고 한다.
        print(f'BMI 체질량지수 수준:{b.get_bmi()}')

Bmi.main()
