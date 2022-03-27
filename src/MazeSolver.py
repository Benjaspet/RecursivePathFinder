from MazeDisplayer import MazeDisplayer

class MazeSolver:

    def __init__(self, maze: list):
        self.maze = maze

    def solve(self) -> None:
        time.sleep(0.3)
        cur = path[-1]
        MazeDisplayer(self.maze)
        possibles = [(cur[0], cur[1] + 1), (cur[0], cur[1] - 1), (cur[0] + 1, cur[1]), (cur[0] - 1, cur[1])]
        random.shuffle(possibles)

        for item in possibles:
            if item[0] < 0 or item[1] < 0 or item[0] > len(maze) or item[1] > len(maze[0]):
                continue
            elif maze[item[0]][item[1]] in ["1", "2"]:
                continue
            elif item in path:
                continue
            elif maze[item[0]][item[1]] == "B":
                path = path + (item,)
                display_maze(maze, path)
                input("Solution found! Press enter to finish")
                os.system('clear')  # windows use 'cls'
                sys.exit()
            else:
                newpath = path + (item,)
                move(newpath)
                maze[item[0]][item[1]] = "2"
                display_maze(maze, path)
                time.sleep(0.3)
