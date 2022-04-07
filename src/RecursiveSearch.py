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

"""
This class uses the recursion method to find a solution to a binary maze.
"""

class RecursiveSearch:

    def __init__(self, maze):
        self.maze = maze
        self.path = []
        self.data = None
        self.initSearch(0, 0)

    """
    Get the current path on which the algorithm has travelled.
    @return list[tuple]
    """

    def getCurrentPath(self):
        return self.path

    """
    Set the solution data for this maze.
    @param data: object
    @return void
    """

    def setResolutionData(self, data):
        self.data = data

    """
    Init a recursive search from the specified coordinates.
    @param x: int
    @param y: int
    @return bool
    """

    def initSearch(self, x: int, y: int):

        # If the recursion algorithm has reached the end, log the entire path, the path's length,
        # and the ending coordinates. Then, set the resolution data to this and return True for
        # the algorithm to stop.

        if self.maze[x][y] == "E":
            print(f'[DEBUG] End found at {(x, y)}.')
            print(f'[DEBUG] Path: {self.path}')
            print(f'[DEBUG] Path length: {len(self.path)}')
            self.setResolutionData({
                "end": (x, y),
                "path": self.path,
                "pathLength": len(self.path)
            })
            return True

        # If a wall has been found, log it and return False so that the algorithm continues.

        elif self.maze[x][y] == 1:
            print(f'[DEBUG] Found wall at {(x, y)}.')
            return False

        # Once it has visited a position, add the coordinates of that position to the path and log it.
        # Return False so the algorithm can continue.

        elif self.maze[x][y] == "x":
            print(f'[DEBUG] Visited {(x, y)}')
            self.getCurrentPath().append((x, y))
            return False

        # Mark the point as visited.

        self.maze[x][y] = "x"

        # This check is an implementation of the recursion method.
        # Check all points around a particular point (left, right, up, down).
        # If a wall has been found, check the next one, and so on until the end has been found.

        if (
                ((x < len(self.maze) - 1) and self.initSearch(x + 1, y))
                or (y > 0 and self.initSearch(x, y - 1))
                or (x > 0 and self.initSearch(x - 1, y))
                or (y < len(self.maze) - 1 and self.initSearch(x, y + 1))
        ):
            return True

        # Otherwise, the end has not been found. Return False.

        return False