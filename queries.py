from dotenv import load_dotenv
from scrape import scrape
import os
import mysql.connector

load_dotenv()

user = os.getenv('DBUSER')
password = os.getenv('DBPASSWORD')
host = os.getenv('DBHOST')
database = os.getenv('DBDATABASE')

def peek():
    cnx = mysql_conn()
    cursor = cnx.cursor()
    query = "SELECT COUNT(*) FROM top_movies"
    cursor.execute(query)
    count = cursor.fetchone()
    cursor.close()
    cnx.close()

    return count


def all():
    cnx = mysql_conn()
    cursor = cnx.cursor()
    query = "SELECT title FROM top_movies"
    cursor.execute(query)
    titles = [row[0] for row in cursor.fetchall()]
    cursor.close()
    cnx.close()

    return titles


def top_ten():
    scrape_and_save()

    cnx = mysql_conn()
    cursor = cnx.cursor()
    query = "SELECT title FROM top_movies LIMIT 10"
    cursor.execute(query)
    titles = [row[0] for row in cursor.fetchall()]
    cursor.close()
    cnx.close()

    return titles


def scrape_and_save():
    if peek()[0] == 0:
        scrape(mysql_conn())


def fetch():
    cnx = mysql_conn()
    cursor = cnx.cursor()
    query = "DELETE FROM top_movies"
    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()


def mysql_conn(user=user, password=password, host=host, database=database):
    return mysql.connector.connect(
        user=user, 
        password=password,
        host=host, 
        database=database
    )
