import sqlite3
from flask import Flask, request, jsonify
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required


class Item(Resource):
	@jwt_required()
	def get(self,name):
		item = self.find_by_name(name)
		if item:
			return item
		else:
			return {'message':"item not found"}, 404

	@classmethod
	def find_by_name(cls,name):
		connection=sqlite3.connect('data.db')
		cursor = connection.cursor()

		query = "SELECT * from items WHERE name=?"
		result = cursor.execute(query,(name,))

		row=result.fetchone()
		connection.close()

		if row:
			return {'item':{'name':row[0] , 'price':row[1]}}, 200


	def post(self,name):
		if self.find_by_name(name):
			return {'message':"An item with name '{}' already exists".format(name)}, 400

		data=request.get_json()  

		item={'name': name,'price':data['price']}

		connection=sqlite3.connect('data.db')
		cursor = connection.cursor()

		query = "INSERT INTO items VALUES(?,?)"
		cursor.execute(query,(item['name'],item['price']))

		connection.commit()
		connection.close()

		return item, 201

	def delete(self,name):
		global items
		items1=[]
		for item in items:
			if item['name']!=name:
				items1.append(item)
		items=items1
		return {'message':"iteam deleted"}

	def put(self,name):
		parser = reqparse.RequestParser()
		parser.add_argument('price',
                   type=float,
                   required=True,
                   help="This field cannot be empty"
			)
		flag=0
		data=parser.parse_args()
		for item in items:
			if item['name']==name:
				item.update(data)
				flag=1
		if flag==0:
			item={'name':name, 'price': data['price']}
			items.append(item)
		return {'message':"iteam updated"}



class Itemlist(Resource):
	def get(self):
		return {'items':items}