from os import system

class MazeDisplayer:

    def __init__(self, binaryList: list):
        self.binaryList = binaryList
        copied: list = binaryList[:]
        print("\033c")
        for item in path:
            self.binaryList[item[0]][item[1]] = "."
        self.binaryList[path[-1][0]][path[-1][1]] = "M"
        maze: str = ""
        for row in copied:
            for item in row:
                item = str(item).replace("1", "#").replace("0", " ")
                maze += item
            maze += "\n"
        print(maze)