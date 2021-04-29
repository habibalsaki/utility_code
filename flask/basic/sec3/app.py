from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'Store 1',
        'items': []
    }
]

@app.route('/store')
def get_stores():
    return jsonify({"stores": stores})

@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({"message": "No store found"})

@app.route('/store', methods=['POST'])
def create_stores():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

@app.route('/store/<string:name>/items')
def get_items(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({"items": store["items"]})
    return jsonify({"message": "No store found"})

@app.route('/store/<string:name>/items', methods=['POST'])
def create_items(name):
    request_data = request.get_json()
    new_item = {
        'name': request_data['name'],
        'price': request_data['price']
    }

    for store in stores:
        if store['name'] == name:
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({"message": "No store found"})

app.run(port=5001)