"""
Requirements:
  1. Fetch JSON data from a Multiple live URL/endpoint that updates with each refresh.
  2. Upload the fetched JSON data to your MongoDB.
  3. Maintain the upload for approximately 3 hours for multiple URL's, which is around 10,800 seconds. # (3 * 60 * 60) = 10,800
  
  Note: - If your fetching data from multiple URL's, it will take much time to upload to your MongoDB. So, here I've used 'Threading' to maintain the upload for about 
          3 hours.
          
          For Example: - 2 URL's = ( 3hrs + 3hrs ) = 6hrs
                         (6hrs * 60minutes * 60seconds) = 32, 400 seconds

"""



from pymongo import MongoClient
from threading import Thread
import requests
import time


connection = "mongodb+srv://iampraveens:yourpassword@iampraveens.pdv2nqk.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection)

def fetch_upload_to_mongodb():
    
    database = client.Threading_Fetch_Data
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
        
def new_fetch_upload_to_mongodb():
    
    database = client.Threading_Fetch_Data
    collections = database.JsonPlus
    
    for i in range(10800):
        try:
            response = requests.get('https://www.bitstamp.net/api/v2/ticker/btcusd/')
            data = response.json()
            collections.insert_one(data)
            print(data)
        except:
            print("Fetching error")
        
        time.sleep(1)
        
        
if __name__ == '__main__':
    
    threads = []

    thread1 = Thread(target=fetch_upload_to_mongodb)
    thread2 = Thread(target=new_fetch_upload_to_mongodb)
    
    thread1.start()
    thread2.start()
    
    for i in threads:
        i.join()
        
    print("Uploading!")
    
