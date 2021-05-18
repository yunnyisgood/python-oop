class bmiCalculation:

    def __init__(self, weight, meter):
        self.weight = weight
        self.meter = meter

    def BMI(self):
        return self.weight / (self.meter ** 2)


if __name__ == '__main__':
    b = bmiCalculation(60, 1.6)
    print(round(b.BMI(),1))
