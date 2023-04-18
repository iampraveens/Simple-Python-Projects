
"""
Requirements :
   1. Fetch JSON data from a live URL/endpoint that updates with each refresh.
   2. Upload the fetched JSON data to your MongoDB.
   3. Maintain the upload for approximately 3 hours, which is around 10,800 seconds. # (3 * 60 * 60) = 10,800
    
"""


from pymongo import MongoClient
import requests
import time


connection = "mongodb+srv://iampraveens:yourpassword@iampraveens.pdv2nqk.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection)

def fetch_upload_to_mongodb():
    
    database = client.Fetch_Data
    collections = database.Json
    
    for i in range(10800):
        try:
            response = requests.get('http://api.open-notify.org/iss-now.json')
            data = response.json()
            collections.insert_one(data)
            print(data)
        except:
            print("Fetching error")
        
        time.sleep(1)
        
fetch_upload_to_mongodb()
