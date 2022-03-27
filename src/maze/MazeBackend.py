from src.MazeReader import MazeReader
from src.MazeDisplayer import MazeDisplayer

def move(path: list) -> None:
    maze: list = MazeReader("EasyMazeOne.csv").fetch()
    current: tuple = path[-1]
    possibilities: list[tuple] = [
        (current[0], current[1] + 1),
        (current[0], current[1] - 1),
        (current[0] + 1, current[1]),
        (current[0] - 1, current[1])
    ]

    for coordinate in possibilities:
        if coordinate[0] < 0 or coordinate[1] < 0 or coordinate[0] > len(maze):
            continue
        elif maze[coordinate[0]][coordinate[1]] in ["1", "2"]:
            continue
        elif coordinate in path:
            continue
        elif maze[coordinate[0]][coordinate[1]] == "E":
            path = path + (item)
            display_maze(maze, path)
            input("Solution found! Press enter to finish")
            os.system('clear')
            sys.exit()
        else:
            newpath = path + (item)
            move(newpath)
            maze[item[0]][item[1]] = "2"
            MazeDisplayer(maze, path)
            time.sleep(0.3)