class PuzzleReader():
    def __init__(self, filename):
        self.filename = filename
        self.puzzle = []
        self.read_puzzle()