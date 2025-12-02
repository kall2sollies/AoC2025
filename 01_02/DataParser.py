class DataParser:
    filename: str
    lines: list[str]

    def __init__(self, filename: str):
        self.filename = filename
        self.parse()
    
    def parse(self):
        with open(self.filename, 'r') as file:
            self.lines = file.read().splitlines()

    def dump(self):
        for line in self.lines:
            print(line)