from pymongo import MongoClient

client = MongoClient()

db = client.homehabit

locations = db.locations
devices = db.devices

kitchen = 	{
				"name":"kitchen"
			}



kitchen_id = locations.insert_one(kitchen).inserted_id


L1	=	{
				"id":"L1",
				"name":"Light 1",
				"driver":"light",
				"location": kitchen_id
}


devices.insert_one(L1)
