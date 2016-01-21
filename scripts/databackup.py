from pymongo import MongoClient

client = MongoClient()

db = client.homehabit

locations = db.locations
devices = db.devices

kitchen = 	{
				name:"kitchen"
			}

bedroom =	{
				"name":"bedroom"
			}



locations.insert_one(kitchen)
locations.insert_one(bedroom)

L1	=	{
				"id":"L1",
				"name":"Light 1",
				"driver":"light"
}

L2	=	{
				"id":"L2",
				"name":"Light 2",
				"driver":"light"
}

L3	=	{
				"id":"L3",
				"name":"Light 3",
				"driver":"light"
}

P1	=	{
				"id":"P1",
				"name":"Power 1",
				"driver":"power"
}

P2	=	{
				"id":"P2",
				"name":"Power 2",
				"driver":"power"
}

VP1	=	{
				"id":"VP1",
				"name": "Projector 1",
				"driver":"IR"
}

VP2	=	{
				"id":"VP2",
				"name": "Projector 2",
				"driver":"IR"
}

TV1	=	{
				"id":"TV1",
				"name": "TV1",
				"driver":"IR"
}

devices.insert_one(L1)
devices.insert_one(L2)
devices.insert_one(L3)
devices.insert_one(P1)
devices.insert_one(P2)
devices.insert_one(VP1)
devices.insert_one(VP2)
devices.insert_one(TV1)