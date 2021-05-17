class bmiCalculation:
    def setdataBMI(self, weight, meter):
        self.weight = weight
        self.meter = meter

    def BMI(self):
        return self.weight / (self.meter ** 2)


if __name__ == '__main__':
    b = bmiCalculation()
    b.setdataBMI(60, 1.6)
    print(round(b.BMI(),1))
