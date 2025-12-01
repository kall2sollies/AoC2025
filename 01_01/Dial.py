class Dial:

    currentValue: int

    def __init__(self, initialValue: int = 50):
        self.currentValue = initialValue

    def rotate(self, rotationValue: int):
        self.currentValue += rotationValue
        self.currentValue %= 100

    def dump(self):
        print(f"Dial current value: {self.currentValue}")