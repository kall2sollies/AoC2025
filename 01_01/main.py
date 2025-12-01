from DataParser import DataParser
from Rotation import Rotation
from Dial import Dial

def main():
    dataParser: DataParser = DataParser('data/data.txt')
    rotations: list[Rotation] = [Rotation(line) for line in dataParser.lines]
    dial: Dial = Dial(50)

    zeroCount: int = 0

    for rotation in rotations:
        dial.rotate(rotation.value)
        if dial.currentValue == 0:
            zeroCount += 1

    print(f"Password: {zeroCount}")

main()