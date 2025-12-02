from Dial import Dial
from Rotation import Rotation

def Dial_tests(initialValue: int, rotationLiteral: str, expectedFinalValue: int, expectedZeroCount: int):
    dial: Dial = Dial(100, initialValue)
    dial.rotateWithRotation(Rotation(rotationLiteral))
    dial.dump()
    testPass: bool = dial.finalValue == expectedFinalValue and dial.zeroCount == expectedZeroCount
    green: str = "\033[92m"
    red: str = "\033[91m"
    endc: str = "\033[0m"
    color: str = green if testPass else red
    print(f"{color}Pass: {testPass}, Expected final value: {expectedFinalValue}, expected zero count: {expectedZeroCount}{endc}\n")

Dial_tests(50, 'R2', 52, 0)
Dial_tests(50, 'R50', 0, 1)
Dial_tests(50, 'R51', 1, 1)
Dial_tests(50, 'R150', 0, 2)
Dial_tests(50, 'R151', 1, 2)
Dial_tests(1, 'L2', 99, 1)
Dial_tests(1, 'L1', 0, 1)
Dial_tests(2, 'L2', 0, 1)
Dial_tests(51, 'L150', 1, 1)
Dial_tests(50, 'L150', 0, 2)
Dial_tests(1, 'L101', 0, 2)
Dial_tests(99, 'L199', 0, 2)
Dial_tests(49, 'L150', 99, 2)
Dial_tests(50, 'R1000', 50, 10)
Dial_tests(52, 'R48', 0, 1)
Dial_tests(0, 'L5', 95, 0)