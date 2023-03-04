# imdb_scrape
Scrape and save IMDB top movies into MySQL database.

Use a .env file to mysql connector variables.

## Flask Routes
- The "/" list all movies. If mysql database table is empty, it does a request and save the movies into database.
- The "/top-ten" list the ten first movies.
- "/fetch" delete all database records and redirect to "/".

### Preview
[![Video Preview](https://user-images.githubusercontent.com/30248076/222923779-d1aef948-b11d-4452-bdf9-d02b99b60586.png)](https://user-images.githubusercontent.com/30248076/222920750-f67a4982-c525-4f1c-b707-93f656891592.mp4)
