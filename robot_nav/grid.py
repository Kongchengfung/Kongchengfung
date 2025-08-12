class Grid:
    def __init__(self, filename):
        self.filename = filename
        self.width = 0
        self.height = 0
        self.start = ()
        self.goals = set()
        self.walls = set()
        self.load_file()

    def load_file(self):
        with open(self.filename, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
            self.width, self.height = map(int, lines[0].lower().split('x'))
            self.start = tuple(map(int, lines[1].split(',')))
            self.goals = {tuple(map(int, coord.split(','))) for coord in lines[2].split(';')}
            self.walls = {tuple(map(int, line.split(','))) for line in lines[3:]}

    def is_valid(self, pos):
        x, y = pos
        return 0 <= x < self.width and 0 <= y < self.height and pos not in self.walls
