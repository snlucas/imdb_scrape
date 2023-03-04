from flask import Flask, render_template, redirect
import queries


app = Flask(__name__)

@app.route('/')
def show_titles():    
    queries.scrape_and_save()
    return render_template('titles.html', titles=queries.all(), top_ten_link='/top-ten', fetch='/fetch')


@app.route('/top-ten')
def show_top_ten_titles():
    queries.scrape_and_save()
    return render_template('top-ten-titles.html', titles=queries.top_ten(), home='/', fetch='/fetch')


@app.route('/fetch')
def fetch():
    queries.fetch()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=False)
