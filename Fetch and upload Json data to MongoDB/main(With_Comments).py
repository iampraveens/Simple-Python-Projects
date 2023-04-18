from pymongo import MongoClient
import requests
import time

# MongoDB connection string with credentials for authentication
connection = "mongodb+srv://iampraveens:yourpassword@iampraveens.pdv2nqk.mongodb.net/?retryWrites=true&w=majority"

# Create a MongoClient object
client = MongoClient(connection)

# Define a function to fetch JSON data and upload it to MongoDB
def fetch_upload_to_mongodb():
    
    # Select database and collection to use
    database = client.Fetch_Data
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

# Call the fetch_upload_to_mongodb function
fetch_upload_to_mongodb()
