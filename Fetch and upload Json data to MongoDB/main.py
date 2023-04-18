
"""
Requirements :
    1. Fetch a Json data from a URL/Enpoint, which should need to be live and update on each refresh.
    2. Fetched Json data should have to upload to your MongoDB.
    3. Upload it for about 3hrs which is around 10800 secs. # (3 * 60 * 60 ) = 10800
    
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
