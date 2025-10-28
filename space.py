import mysql.connector

# Connect to the spacex database
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="nitoo1234",
    database="spacex"
)

mycursor = mydb.cursor()

# Query all rows from your table (replace 'your_table_name' with the actual table name)
mycursor.execute("SELECT * FROM launchdata")

results = mycursor.fetchall()

for row in results:
    print(row)
