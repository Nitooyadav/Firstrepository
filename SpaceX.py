# Storing data in MYSQL from spacex api
import requests
import mysql.connector
import json
from datetime import datetime

try:
    # Connect to MySQL database (update with your credentials)
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",     # replace with your MySQL username
        password="nitoo1234", # replace with your MySQL password
        database="spacex"  # replace with your database name
    )

    mycursor = mydb.cursor()

    # Create the table 'launchdata' with id as PRIMARY KEY, name unique, and index on flight_number
    # Using TEXT for payloads instead of JSON for compatibility
    create_table_query = """
    CREATE TABLE IF NOT EXISTS launchdata (
        id VARCHAR(64) PRIMARY KEY,
        flight_number INT,
        name VARCHAR(255) UNIQUE,
        date_utc DATETIME,
        success TINYINT(1),       -- boolean as tinyint
        payloads TEXT,
        INDEX flight_number_idx (flight_number)
    )
    """
    mycursor.execute(create_table_query)

    # Fetch SpaceX launch data
    response = requests.get('https://api.spacexdata.com/v4/launches')
    launches = response.json()

    # Insert query
    insert_query = """
    REPLACE INTO launchdata (id, flight_number, name, date_utc, success, payloads)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    # Insert data with date format conversion and success boolean handling
    for launch in launches:
        dt_str = launch.get('date_utc')
        if dt_str:
            dt = datetime.fromisoformat(dt_str.replace('Z', ''))
            dt_mysql = dt.strftime('%Y-%m-%d %H:%M:%S')
        else:
            dt_mysql = None

        # Convert boolean success to int for MySQL (None treated as NULL)
        success_val = launch.get('success')
        if success_val is None:
            success_val = None
        else:
            success_val = int(success_val)

        values = (
            launch.get('id'),
            launch.get('flight_number'),
            launch.get('name'),
            dt_mysql,
            success_val,
            json.dumps(launch.get('payloads'))
        )
        mycursor.execute(insert_query, values)

    mydb.commit()
except mysql.connector.Error as err:
    print("MySQL Error:", err)
except Exception as e:
    print("Error:", e)
finally:
    if mycursor:
        mycursor.close()
    if mydb:
        mydb.close()
