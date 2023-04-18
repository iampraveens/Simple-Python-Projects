from pymongo import MongoClient
from threading import Thread
import requests
import time

# MongoDB connection string with credentials for authentication
connection = "mongodb+srv://iampraveens:yourpassword@iampraveens.pdv2nqk.mongodb.net/?retryWrites=true&w=majority"

# Create a MongoClient object
client = MongoClient(connection)

# Define a function to fetch JSON data and upload it to MongoDB
def fetch_upload_to_mongodb():
    
    # Select database and collection to use
    database = client.Threading_Fetch_Data
    collections = database.Json
    
    # Loop for a duration of approximately 3 hours, fetching and uploading data
    for i in range(10800):
        
        # Try to fetch data from a live URL
        try:
            response = requests.get('http://api.open-notify.org/iss-now.json')
            data = response.json()
            
            # Upload fetched data to MongoDB
            collections.insert_one(data)
            
            # Print fetched data
            print(data)
        
        # If there is an error fetching data, print error message
        except:
            print("Fetching error")
        
        # Wait for 1 second before fetching next set of data
        time.sleep(1)
        
# Define another function to fetch JSON data and upload it to MongoDB
def new_fetch_upload_to_mongodb():
    
    # Select database and collection to use
    database = client.Threading_Fetch_Data
    collections = database.JsonPlus
    
    # Loop for a duration of approximately 3 hours, fetching and uploading data
    for i in range(10800):
        
        # Try to fetch data from a live URL
        try:
            response = requests.get('https://www.bitstamp.net/api/v2/ticker/btcusd/')
            data = response.json()
            
            # Upload fetched data to MongoDB
            collections.insert_one(data)
            
            # Print fetched data
            print(data)
        
        # If there is an error fetching data, print error message
        except:
            print("Fetching error")
        
        # Wait for 1 second before fetching next set of data
        time.sleep(1)

# Main function that initializes and starts two threads
if __name__ == '__main__':
    
    threads = []

    # Create two threads, one for each function
    thread1 = Thread(target=fetch_upload_to_mongodb)
    thread2 = Thread(target=new_fetch_upload_to_mongodb)
    
    # Start both threads
    thread1.start()
    thread2.start()
    
    # Wait for both threads to finish
    for i in threads:
        i.join()
        
    # Print completion message
    print("Uploading!")
