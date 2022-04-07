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

import json
from src.BackTracingSearch import obtainSolutions
from src.RecursiveSearch import RecursiveSearch
from flask import Flask, jsonify, request

# Creating a new instance of our REST API.

app = Flask(__name__)

# Defining the first route.
# @route /v1/bktr/solve
# @method POST
# @return JSON response

@app.route("/v1/bktr/solve", methods=["POST"])
def getSampleResponse():

    # Wrapping our clause in a try/catch block to handle errors.

    try:

        # Getting the content type header of the request. If it is of type
        # application/json, we know that there is JSON data in the request body.

        content_type = request.headers.get("Content-Type")
        if content_type == "application/json":

            # Loading this request body data as a JSON object and parsing it accordingly.
            # Finally, we'll return a JSON object with the solution data (if any) to the maze
            # using the back-tracing algorithm.

            parsed = json.loads(json.dumps(dict(request.get_json())))
            return jsonify(
                {
                    "solutions": obtainSolutions(parsed["maze"])
                }
            )
        else:
            return "Content-Type is not supported."

    # Handling all other exceptions.

    except BaseException:
        return jsonify({
            "message": "An internal server error occurred."
        }), 500

# This is our next route using the recursion algorithm.
# @route /v1/recursion/solve
# @method POST
# @return JSON response

@app.route("/v1/recursion/solve", methods=["POST"])
def fetchRecursionResponse():

    # Once again, wrapping everything in a try/catch block.
    # Using similar code to the other block, we'll instead be using
    # recursion and returning the solution data using that algorithm.

    try:
        content_type = request.headers.get("Content-Type")
        if content_type == "application/json":
            parsed = json.loads(json.dumps(dict(request.get_json())))
            return jsonify(
                {
                    "solutions": RecursiveSearch(parsed["maze"]).data
                }
            )
        else:
            return "Content-Type is not supported."

    # Handling all exceptions.

    except BaseException:
        return jsonify({
            "message": "An internal server error occurred."
        }), 500

# This final route is for the homepage.
# TODO: html/css styling (bootstrap lmao)

@app.route("/")
def getHomepage():
    return "<h2><center>Welcome to the API.</center></h2>"

# Running our REST application.

app.run()