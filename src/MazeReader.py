import csv

class MazeReader:

    def __init__(self, fileName: str):
        self.fileName = fileName
        self.reader = csv.reader(open("../mazes/" + self.fileName, "r"))

    def fetch(self) -> list:
        maze: list = []
        for line in self.reader:
            maze.append(line)
        return maze