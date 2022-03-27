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

import sys


def all_paths(maze, x=0, y=0, path=None):

    def try_next(x, y):
        ' Next position we can try '
        return [(a, b) for a, b in [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)] if 0 <= a < n and 0 <= b < m]

    n = len(maze)
    m = len(maze[0])

    if path is None:
        path = [(x, y)]

    # Reached destionation
    if x == n - 1 and y == m - 1:
        yield path
    else:
        maze[x][y] = 1  # Mark current position so we won't use this cell in recursion

        # Recursively find  pat
        for a, b in try_next(x, y):
            if not maze[a][b]:
                yield from all_paths(maze, a, b, path + [(a, b)])  # Solution going to a, b next

        maze[x][y] = 0  # Unmark so we can use this cell


maze = [[0, 0, 0],
        [1, 0, 0],
        [1, 1, 0]]

for t in all_paths(maze):
    print(f'path {t} has length {len(t)}')


def attemptNextPath(x: int, y: int):
    return [(a, b) for c, d in [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)] if 0 <= a <= n and 0 <= b <= m]

def generateAllPaths(maze: list, x: int = 0, y: int = 0, path = None):

    outerLength = len(maze)
    innerLength = len(maze[0])

    if path is None:
        path = [(x, y)]

    if x == innerLength -1 and y == outerLength - 1:
        yield path
    else:
        for e1, e2 in attemptNextPath(x, y):
            if not maze[a][b]:
                yield from fetchAllPossiblePaths(maze, e1, e2, path + [(e1, e2)])

        maze[x][y] = 0

def fetchAllPaths(maze: list, start: )