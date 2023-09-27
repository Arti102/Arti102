from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.shortcuts import HttpResponse
# from models import Property


from pymongo import MongoClient
from datetime import datetime
import pymongo

def scrape_and_save_to_mongodb(url, database_name, collection_name):
    response = requests.get(url)

   
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Initialize a MongoDB client
        client = pymongo.MongoClient('localhost', 27017)  
        db = client['admin']


        collection = db['housing']

        # Find all property listings on the page
        property_listings = soup.find_all('div', class_='info css-poh5ib')

        print(property_listings)
        for listing in property_listings:
            # Extract property details
            name = listing.find('div', class_='name css-1kop8ej').text.strip()
            print('name is :: ', name)
            cost = listing.find('div', class_='price css-zskpky').text.strip()
            print('cost is :: ', cost)
            property_type = listing.find('div', class_='title css-4rw15f').text.strip()
            print('Property type  is :: ', property_type)

            city = listing.find('div', class_='address css-19lhbwg').text.strip()
            print('City is :: ', city)

            # Create a dictionary to represent the property data
            property_data = {
                'Property Name': name,
                'Property Cost': cost,
                'Property Type': property_type,
                'propertyCity': city,
            }
            print(property_data)
        
            collection.insert_one(property_data)

        client.close()

        print("Property data scraped and saved to MongoDB successfully.")
    else:
        print("Failed to fetch data from the website.")


url = 'https://housing.com/'
database_name = 'admin'  
collection_name = 'housing'  
scrape_and_save_to_mongodb(url,"admin", "housing")
cd