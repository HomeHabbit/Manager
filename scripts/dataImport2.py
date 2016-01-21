from pymongo import MongoClient

client = MongoClient()

db = client.homehabit

drivers = db.drivers
locations = db.locations
devices = db.devices


drivers =	{
	[{
		"_id":"IR",
		"names":["TV","projector","television","screen"],
		"actions":[{
				"name":"volume",
				"type":"int"
			},
			{
				"name":"channel",
				"type":"int"
			},
			{
				"name":"power",
				"type":"enum",
				"values":["on","off"]
			}]
	},
	{
		"_id":"power",
		"names":["plug","power"],
		"actions":[{
				"name":"turn",
				"type":"enum",
				"values":["on", "off"]
			},
			{
				"name":"switch",
				"type":"enum",
				"values":["on", "off"]
			}]
	},
	{
		"_id":"light",
		"names":["light","lamp","LED"],
		"actions":[{
				"name":"turn",
				"type":"enum",
				"values":["on", "off"]
			},
			{
				"name":"switch",
				"type":"enum",
				"values":["on", "off"]
			},
			{
				"name":"light",
				"type":"enum",
				"values":["on", "off"]
			}]
	}]
}

kitchen = 	{
				"_id":"kitchen",
				"devices": [{
						"_id":"L1",
						"name":"light 1",
						"driver":"light",
						"device_id":""
					},{
						"_id":"TV1",
						"name": "TV1",
						"driver":"IR",
						"device_id":""
					},{
						"_id":"VP1",
						"name": "projector 1",
						"driver":"IR",
						"device_id":""
					},{
						"_id":"P2",
						"name":"power 2",
						"driver":"power",
						"device_id":"17613"
					}]
			}

bedroom =	{
				"_id":"bedroom",
				"devices": [{
						"_id":"L2",
						"name":"light 2",
						"driver":"light",
						"device_id":""
					},{
						"_id":"L3",
						"name":"light 3",
						"driver":"light",
						"device_id":""
					},{
						"_id":"P1",
						"name":"power 1",
						"driver":"power",
						"device_id":"1"
					},{
						"_id":"VP2",
						"name": "projector 2",
						"driver":"IR",
						"device_id":""
					}]
			}

