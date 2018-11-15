# This script pulls from a job website and stores positions into a database.
# If there is a new posting it notifies the user.
# CNA 330
# Zachary Rubin, zrubin@rtc.edu
import mysql.connector
import sys
import json
import urllib.request
import os
import time


def load_config_file(filename):
    argument_dictionary = 0
    # Code from https://github.com/RTCedu/CNA336/blob/master/Spring2018/FileIO.py
    rel_path = os.path.abspath(os.path.dirname(__file__))
    file = 0
    file_contents = 0
    try:
        file = open(filename, "r")
        file_contents = file.read()
    except FileNotFoundError:
        print("File not found, it will be created.")
        file = open(filename, "w")
        file.write("")
        file.close()

    # Add in information for argument dictionary
    return argument_dictionary


# conn = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='cna330')
# cursor = conn.cursor()

# Connect to database
# You should not need to edit anything in this function


#def connect_to_sql():
conn = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='CNA330')
    #return conn
c = conn.cursor()
# Create the table structure


#def create_tables(cursor, jobs):

    # Add your code here. Starter code below
    # cursor.execute('''CREATE TABLE IF NOT EXISTS ''' + table + ''' (id INT PRIMARY KEY, title TEXT, company TEXT,
    # location TEXT, pay INT, description TEXT); ''')

    # cursor.execute("CREATE TABLE IF NOT EXISTS hosts(id INTEGER, hostname TEXT, "
    #               "url TEXT, ip TEXT, local_remote TEXT, description TEXT) ;")

c.execute('''CREATE TABLE Jobs (id INTEGER PRIMARY KEY, title TEXT, company TEXT,
location TEXT, pay INTEGER, date TEXT, description TEXT);''')

c.execute("INSERT INTO Jobs VALUES(0,'sys admin','self','home','20','10 31 18','test') ;")

    # cursor.execute('''CREATE TABLE IF NOT EXISTS ''' + table + ''' (id INT PRIMARY KEY); ''')

c.close()
    #return cursor

# Query the database.
# You should not need to edit anything in this function


#def query_sql(cursor, query):
c.execute(query)
#    return cursor

# Add a new job


def add_new_job(cursor, jobdetails):
    # Add your code here
    data = ()
    query = "INSERT INTO jobs (%s, %s, %s, %s, %s, %s, %s)" % data
    return query_sql(cursor, query)

# Check if new job


def check_if_job_exists(cursor, jobdetails):
    # Add your code here
    query = "SELECT"
    return query_sql(cursor, query)


def delete_job(cursor, jobdetails):
    # Add your code here
    query = "UPDATE"
    return query_sql(cursor, query)

# Grab new jobs from a website


def fetch_new_jobs(arg_dict):
    # Code from https://github.com/RTCedu/CNA336/blob/master/Spring2018/Sql.py
    query = "https://jobs.github.com/positions.json?" + "location=seattle"# Add arguments here
    jsonpage = 0
    try:
        contents = urllib.request.urlopen(query)
        response = contents.read()
        jsonpage = json.loads(response)
    except:
        pass
        time.sleep(1)
    data = json.dumps(jsonpage['data'])
    return jsonpage

# Load a text-based configuration file


# Main area of the code.


def jobhunt(arg_dict):
    # Fetch jobs from website
    return fetch_new_jobs(arg_dict)
    print(jobpage)
    # Add your code here to parse the job page

    # Add in your code here to check if the job already exists in the DB

    # Add in your code here to notify the user of a new posting

    # EXTRA CREDIT: Add your code to delete old entries

# Setup portion of the program. Take arguments and set up the script
# You should not need to edit anything here.





def main():
    # Connect to SQL and get cursor
    conn = connect_to_sql()
    cursor = conn.cursor()
    create_tables(cursor, jobs)
    # Load text file and store arguments into dictionary
    arg_dict = load_config_file(sys.argv[1])
    while(1):
        jobhunt(arg_dict)
        time.sleep(3600)
    # Sleep for 1h

    # if __name__ == '__main__':main()
