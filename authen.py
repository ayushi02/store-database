from flask import Flask, request, jsonify
from flask_restful import Resource,Api
from flask_jwt import JWT
from security import *
from user import UserRegister
from item import Item,Itemlist

app = Flask(__name__)
app.secret_key= "ayushi"
api=Api(app)         #api works with resouces and uses classes

jwt=JWT(app,authenticate,identity)

"""items=[]

class Item(Resource):
	@jwt_required()
	def get(self,name):
		for item in items:
			if item['name']==name:
				return item
		#item = next(filter(lambda x: x['name']==name, items), None)
		#return {'item':item}, 200 if item else 404		


	def post(self,name):
		data=request.get_json()   #can put force=True then it will not see header type or if we put silent=True it will return none if not json
		#item1 = next(filter(lambda x: x['name']==name, items), None)
		#if item1:
			#return {'message':"An item with name '{}' already exists".format(name)}, 400

		item={'name': name,'price':data['price']}
		items.append(item)
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



class Items(Resource):
	def get(self):
		return {'items':items}"""

api.add_resource(Item,'/item/<string:name>')
api.add_resource(Itemlist,'/items')
api.add_resource(UserRegister,'/register')

if __name__ =='__main__':
	app.run(port=5000,debug=True)