class Rotation:
    value: int

    def __init__(self, literal: str):
        if  len(literal) < 2:
            raise ValueError("Invalid rotation literal")
        sign: int = 1 if literal[0] == 'R' else -1
        self.value = sign * int(literal[1:])

    def dump(self):
        print(f"Rotation: {self.value}")