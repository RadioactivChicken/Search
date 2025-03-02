#!/bin/python3.12
import mysql.connector, re

def clean_input(input):
    pattern = re.compile('[\W_]+')
    cleaned_str = pattern.sub('', input)
    return cleaned_str

def log(url):
    mydb = mysql.connector.connect(
            host="localhost",
            user="python",
            password="Passw0rd!",
            database="search"
            )
    cur = mydb.cursor()


    sql = "INSERT INTO log (key_id, searched) VALUES ('%s', 1) ON DUPLICATE KEY UPDATE searched = searched + 1;" % (url)
    cur.execute(sql)

    mydb.commit()
    mydb.close()



def search(url):
    log(url)

    mydb = mysql.connector.connect(
            host="localhost",
            user="python",
            password="Passw0rd!",
            database="search"
            )
    cur = mydb.cursor()

    sql = "SELECT * FROM key_data WHERE key_id = '%s';" % (url)
    cur.execute(sql)
    result = cur.fetchall() 

    mydb.close()

    if result:
        return [ True , result[0][1] ]
    else:
        return [ False , ""]



def add(key, url):
    key = clean_input(key)
    mydb = mysql.connector.connect(
            host="localhost",
            user="python",
            password="Passw0rd!",
            database="search"
            )
    cur = mydb.cursor()
    
    sql = "SELECT * FROM key_data WHERE key_id = '%s'" % (key)
    cur.execute(sql)
    result = cur.fetchall() 

    if len(result) == 0:
        sql = "INSERT INTO key_data (key_id, url) VALUES ('%s', '%s');" % (key, url)
        cur.execute(sql)
        result = cur.fetchall() 
    else: 
        sql = "UPDATE key_data SET url = '%s' WHERE key_id = '%s'" % (url, key)
        cur.execute(sql)
        result = cur.fetchall()

    mydb.commit()
    mydb.close()

    return result 



