## Call a REST API and pull back a JSON document
import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'
stuff = requests.get(url)
stuff.json()["title"]

## Call a REST API and pull back a collection of JSON documents
import requests

url = 'https://jsonplaceholder.typicode.com/posts/'
stuff = requests.get(url)
for thing in stuff.json():
    print(thing["title"])

## Call a REST API, retrieve a JSON document, and format it
import json
import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'
stuff = requests.get(url)
parsed = json.loads(stuff.json()[1])
print json.dumps(parsed, indent=4, sort_keys=True)

## Connect to the local SQL Server database and retrieve data
import pyodbc
db_connection_string = r'Driver={SQL Server};Server=(local);Database=coffee;Trusted_Connection=yes'
db_connection = pyodbc.connect(db_connection_string)

command = db_connection.cursor()
command.execute("SELECT name FROM sys.databases")

while 1:
    row = command.fetchone()
    if not row:
        break
    print(row.name)

db_connection.close()