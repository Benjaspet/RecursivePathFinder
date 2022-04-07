# RecursivePathFinder
An introduction to path-finding algorithms.

## Using the REST API

All endpoints take in POST requests with the response body being a JSON object with one key `maze` that is paired with a value which contains the binary maze itself.

### /v1/recursion/solve

- Find the path out of the maze using recursion.
- Example request body, where `maze[0][0]` is the starting position, and `"E"` is the end:

`Content-Type: application/json`
```json
{
  "maze": [
    [0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0, 1],
    [0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, "E"]
  ]
}
```

Postman is probably the easiest way to do this, although you could do a curl from your terminal (you'd just have to stringify the JSON above).

A sample response object (based on the response body sample above):

```json
{
    "solutions": {
        "end": [5, 5],
        "path": [
            [0, 0],
            [4, 0],
            [3, 0],
            [2, 0],
            [2, 1],
            [2, 2],
            [1, 2],
            [0, 2],
            [1, 2],
            [1, 3],
            [0, 2],
            [5, 2],
            [4, 3],
            [5, 3],
            [4, 3],
            [5, 3]
        ],
        "pathLength": 16
    }
}
```

### /v1/bktr/solve
- Find all paths (and the shortest one) in a binary maze using the back-tracing algorithm.
- Sample request body:

`Content-Type: application/json`
```json
{
  "maze": [
    [0, 0, 0],
    [1, 0, 0],
    [1, 1, 0]
  ]
}
```

Sample response (using the request body above):

```json
{
    "solutions": [
        {
            "path": [
                [0, 0],
                [0, 1],
                [1, 1],
                [1, 2],
                [2, 2]
            ],
            "pathLength": 5
        },
        {
            "path": [
                [0, 0],
                [0, 1],
                [0, 2],
                [1, 2],
                [2, 2]
            ],
            "pathLength": 5
        }
    ]
}
```

### Important Note
If you'd prefer not to use the API and want to run the algorithms directly from the project, you can do so as follows.

Enter either `BackTracingSearch.py` or `RecursiveSearch.py` and call the method (or create a new class instance) with all required parameters. It's pretty self-explanatory. For example, at the bottom of `RecursiveSearch.py`, add:

```python
obj = RecursiveSearch(maze)
print(obj.data)
```

This will give you, in the terminal:
```text
[DEBUG] Found wall at (1, 0).
[DEBUG] Found wall at (1, 1).
[DEBUG] Visited (0, 0)
[DEBUG] Found wall at (3, 2).
[DEBUG] Found wall at (3, 1).
[DEBUG] Visited (4, 0)
[DEBUG] Found wall at (5, 1).
[DEBUG] Visited (3, 0)
[DEBUG] Found wall at (4, 1).
[DEBUG] Visited (2, 0)
[DEBUG] Found wall at (3, 1).
[DEBUG] Found wall at (1, 0).
[DEBUG] Visited (2, 1)
[DEBUG] Found wall at (1, 1).
[DEBUG] Visited (2, 2)
[DEBUG] Visited (1, 2)
[DEBUG] Found wall at (2, 3).
[DEBUG] Found wall at (1, 1).
[DEBUG] Visited (0, 2)
[DEBUG] Found wall at (2, 3).
[DEBUG] Visited (1, 2)
[DEBUG] Visited (1, 3)
[DEBUG] Visited (0, 2)
[DEBUG] Found wall at (4, 4).
[DEBUG] Found wall at (5, 1).
[DEBUG] Visited (5, 2)
[DEBUG] Found wall at (4, 1).
[DEBUG] Found wall at (3, 2).
[DEBUG] Visited (4, 3)
[DEBUG] Visited (5, 3)
[DEBUG] Visited (4, 3)
[DEBUG] Visited (5, 3)
[DEBUG] Found wall at (4, 4).
[DEBUG] End found at (5, 5).
[DEBUG] Path: [(0, 0), (4, 0), (3, 0), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2), (1, 2), (1, 3), (0, 2), (5, 2), (4, 3), (5, 3), (4, 3), (5, 3)]
[DEBUG] Path length: 16
{'end': (5, 5), 'path': [(0, 0), (4, 0), (3, 0), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2), (1, 2), (1, 3), (0, 2), (5, 2), (4, 3), (5, 3), (4, 3), (5, 3)], 'pathLength': 16}
```


### License

This project is licensed under the MIT License, and may be modified provided that 
credit is given to the original author(s).