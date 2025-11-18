from flask import Flask, request, Response
import requests

app = Flask(__name__)


@app.route("/")
def index():
    return 'Hello from Gateway!'


@app.route('/items', methods=['GET'])
# route for GET with item id
@app.route('/items/<string:item_id>', methods=['GET'])
def get_devicess(item_id=None):
    return 'Hello from GET'


# route for DELETE
@app.route('/items/<string:item_id>', methods=['DELETE'])
def delete_device(item_id):
    return 'Hello from DELETE'


# route for POST
@app.route('/items', methods=['POST'])
def post_device():
    return 'Hello from POST'


# route for PUT
@app.route('/items/<string:item_id>', methods=['PUT'])
def put_device(item_id):
    return 'Hello from PUT'


if __name__ == "__main__":
    app.run("0.0.0.0", port=5001, debug=True)
