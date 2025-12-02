from DataParser import DataParser
from Rotation import Rotation
from Dial import Dial


def main():
    dataParser: DataParser = DataParser('data/data.txt')
    rotations: list[Rotation] = [Rotation(line) for line in dataParser.lines]
    initialValue: int = 50
    ringSize: int = 100
    dial: Dial = Dial(ringSize, initialValue)
    dial.dump()

    for rotation in rotations:
        dial.rotateWithRotation(rotation)
        dial.dump()
        print("----")

    print(f"Password: {dial.zeroCount}")

main()