import requests
import mysql.connector

# fetching weather data using api.
api_key = '54a57bc234ad752a4f59e59cd372201d'  #api key
location = 'gujarat'  #location
url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'

# Sending API request 
response = requests.get(url)
data = response.json()

#Extracting weather data using API response 
temperature = data['main']['temp']
humidity = data['main']['humidity']
wind_speed = data['wind']['speed']

# Database connection
conn = mysql.connector.connect(
    host='localhost',
    user='root',  #MySQL username
    password='1234',  #MySQL password
    database='weather'  #database name
)
cursor = conn.cursor()

# SQL query to insert data into database
insert_query = """
INSERT INTO weather_data (location, temperature, humidity, wind_speed)
VALUES (%s, %s, %s, %s)
"""

# Data to insert
data_to_insert = (location, temperature, humidity, wind_speed)

# Execute the query
cursor.execute(insert_query, data_to_insert)

# Commit the transaction
conn.commit()

# Close the connection
cursor.close()
conn.close()
