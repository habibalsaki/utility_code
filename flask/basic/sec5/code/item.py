from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "price", type=float, help="Price field is required", required=True
    )

    @jwt_required()
    def get(self, name):
        item = Item.find_by_name(name)
        if item:
            return item
        return {"message": "item not found"}, 404

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name = ?"

        result = cursor.execute(query, (name,))

        row = result.fetchone()
        connection.close()
        
        if row:
            return {"item": {"name": row[0], "price": row[1]}}
        
    @classmethod
    def insert(cls, item):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES (?,?)"

        result = cursor.execute(query, (item["name"], item["price"]))
        connection.commit()
        connection.close()

    def post(self, name):
        print(name)
        if Item.find_by_name(name):
            return {
                "message": 'an item with name  "{}" is already available'.format(name)
            }, 400

        data = Item.parser.parse_args()
        new_item = {"name": name, "price": data["price"]}

        Item.insert(new_item)
        return new_item, 201

    def delete(self, name):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "DELETE FROM items where NAME = ?"

        result = cursor.execute(query, (name,))
        connection.commit()
        connection.close()

        return {"message": "Item deleted"}

    @classmethod
    def update(cls, item):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "UPDATE items SET price=? WHERE name = ?"

        result = cursor.execute(query, (item["price"], item["name"]))
        connection.commit()
        connection.close()

    def put(self, name):
        data = Item.parser.parse_args()
        item = Item.find_by_name(name)
        updated_item = {"name": name, "price": data["price"]}
        if item is None:
            Item.insert(updated_item)
        else:
            Item.update(updated_item)
        return updated_item


class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "SELECT * FROM items"

        result = cursor.execute(query)
        items = []
        
        for row in result:
            items.append({"name": row[0], "price": row[1]})
        connection.close()
        return {"items": items}
