import requests
from bs4 import BeautifulSoup


def scrape(sql_connector):
    cnx = sql_connector
    cursor = cnx.cursor()

    # scrape top movie titles from IMDb
    url = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc&count=100"
    headers = {
        "Accept-Language": "en-US,en;q=0.5"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    title_selector = "h3.lister-item-header a"
    titles = [title.get_text() for title in soup.select(title_selector)]

    # insert titles into MySQL database
    insert_query = "INSERT INTO top_movies (title) VALUES (%s)"
    for title in titles:
        cursor.execute(insert_query, (title,))
    cnx.commit()

    # close database connection
    cursor.close()
    cnx.close()
