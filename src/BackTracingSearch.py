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
This class uses the breadth-first search algorithm to find a solution to a binary maze.

Sources

Generator functions: https://stackoverflow.com/questions/1756096/understanding-generators-in-python
Yields, iterables, and generator functions: https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do
"""

# Our generator function to find all possible paths.
# x = starting x position.
# y = starting y position.

def backTracingSearch(maze: list[list[int]], x: int = 0, y: int = 0, path=None) -> list[dict[object]]:

    def attemptNextPath(x: int, y: int):

        """
        This is a generator function that determines the next path that will be checked.
        This is an implementation of the back-tracing algorithm.
        Learn more: Generator functions: https://stackoverflow.com/questions/1756096/understanding-generators-in-python
        """

        xMinus = (x - 1, y)
        yMinus = (x, y - 1)
        xPlus = (x + 1, y)
        yPlus = (x, y + 1)

        # This generator will return only those paths that are able to reach the destination.

        return [
            (pos1, pos2) for pos1, pos2 in [xMinus, yMinus, xPlus, yPlus]
            if 0 <= pos1 < mazeHeight and 0 <= pos2 < mazeWidth]

    # Getting the dimensions of the specified binary maze.

    mazeHeight = len(maze)
    mazeWidth = len(maze[0])

    # If a path was unable to be found from the current coordinates, reset it to the previous and try again.

    if path is None:
        path = [(x, y)]

    # If the current position is at the end destination, the path is finished.

    if x == (mazeHeight - 1) and y == (mazeWidth - 1):
        yield path

    # Otherwise, we're going to recursively find another path.
    # First, mark the current position in order that it will not be used again using recursion.
    # Next, use an implementation of the recursion pathfinding algorithm to find another path.

    else:

        # Setting the spot as occupied, then checking the next using a loop.

        maze[x][y] = 1
        for a, b in attemptNextPath(x, y):
            if not maze[a][b]:
                yield from backTracingSearch(maze, a, b, path + [(a, b)])

        # This visited cell will now be unmarked so that we can use it for the next iteration
        # of the algorithm.

        maze[x][y] = 0

# Below is the method that will return an array of solution data for
# the inputted maze, if any.

def obtainSolutions(maze: list[list[int]]):

    # First, assign an empty array of dictionaries to a variable.

    solutions: list[dict[object]] = [{}]

    # Next, using the aforementioned generator function, fetch a list of all available
    # paths. For each path, add its key and value data to the solutions array. Clean it up
    # by removing the first empty object, then return the updated array of solutions.

    for path in backTracingSearch(maze, 0, 0):
        solutions.append(
            {
                "path": path,
                "pathLength": len(path)
            }
        )

    solutions.pop(0)
    return solutions