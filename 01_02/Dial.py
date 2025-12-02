from Rotation import Rotation

class Dial:

    initialValue: int
    ringSize: int
    finalValue: int
    zeroCount: int = 0

    def __init__(self, ringSize: int, initialValue: int):
        self.initialValue = initialValue
        self.ringSize = ringSize
        self.currentValue = initialValue
        self.finalValue = initialValue

    def rotateWithRotation(self, rotation: Rotation):
        print(f"Applying rotation: {rotation.literal} to {self.initialValue} (ring size: {self.ringSize})")
        self.rotate(rotation.value)

    def rotate(self, rotationValue: int):

        moduloAndCycles: tuple[int, int] = Dial.modulo(self.initialValue + rotationValue, self.ringSize, self.initialValue)

        self.finalValue = moduloAndCycles[0]
        self.zeroCount += moduloAndCycles[1]
        self.initialValue = self.finalValue

    def modulo(value: int, ringSize: int, initialValue: int) -> tuple[int, int]:

        if (value >= 0 and value < ringSize):
            return value, 0 if value != 0 else 1

        direction: int = 1 if value <= 0 else -1
        currentValue: int = value
        iterationCount: int = 0

        while (currentValue < 0 or currentValue >= ringSize):
            currentValue += direction * ringSize
            iterationCount += 1

        if (direction > 0 and currentValue == 0):
            iterationCount += 1
        
        if (initialValue == 0 and direction > 0):
            iterationCount -= 1

        return currentValue, iterationCount
    
    def dump(self):
        print(f"Dial current value: {self.finalValue}, zero count: {self.zeroCount}")