"""
Copyright © 2022 Ben Petrillo. All rights reserved.

Project licensed under the MIT License: https://www.mit.edu/~amini/LICENSE.md

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
OR OTHER DEALINGS IN THE SOFTWARE.

All portions of this software are available for public use, provided that
credit is given to the original author(s).
"""

import csv
import os
import random
import sys
import time

class MazeDisplayer:

    def __init__(self, path: str):
        self.path = path
        self.maze = []

    def fetchMaze(self):
        file: IO = open(self.path, "r")
        array: _reader = csv.reader(file)
        for line in array:
            self.maze.append(line)
        return maze












def display_maze(m, path):
    m2 = m[:]
    print("\033c")

    for item in path:
        m2[item[0]][item[1]] = "."
    m2[path[-1][0]][path[-1][1]] = "M"

    draw = ""

    for row in m2:
        for item in row:
            item = str(item).replace("1", "#")
            item = str(item).replace("2", " ")
            item = str(item).replace("0", " ")

            draw += item
        draw += "\n"
    print(draw)


def move(path):
    cur = path[-1]
    display_maze(maze, path)
    possibles = [(cur[0], cur[1] + 1), (cur[0], cur[1] - 1), (cur[0] + 1, cur[1]), (cur[0] - 1, cur[1])]
    random.shuffle(possibles)

    for item in possibles:
        if item[0] < 0 or item[1] < 0 or item[0] > len(maze) or item[1] > len(maze[0]):
            continue
        elif maze[item[0]][item[1]] in ["1", "2"]:
            continue
        elif item in path:
            continue
        elif maze[item[0]][item[1]] == "E":
            path = path + (item,)
            display_maze(maze, path)
            input("Solution found! Press enter to finish")
            print("\033c")
            sys.exit()
        else:
            newpath = path + (item,)
            move(newpath)
            maze[item[0]][item[1]] = "2"
            display_maze(maze, path)


maze = get_maze('../mazes/EasyMazeOne.csv')

move(((1, 0),))