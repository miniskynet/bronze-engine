#import modules
import mysql.connector
from prettytable import from_db_cursor

#create a dictionary to store the data of localhost
Dict = {"host":"localhost",
        "database":"game_db",
        "user":"root",
        "password":""}

#store the connection to local host in a variable called 'db'
db = mysql.connector.connect(**Dict)

#create a cursor object for traversal through the database
cursor = db.cursor()

#selecting the correct table from the database
cursor.execute("SELECT * FROM quickgame")

#importing the data into a variable
data = from_db_cursor(cursor)

#printing the table
print(data)

#closing the database

db.close()
