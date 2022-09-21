from turtle import home
from flask import Flask, render_template, request
from flask_cors import CORS
import time
from db import data

home_url = 'http://127.0.0.1:5000/'


app = Flask(__name__)
CORS(app)

@app.get('/')
def index():
    return render_template('search.html', title='Shorten URL' )

@app.route('/shortened', methods=['POST'])
def shortened():
    if request.method == 'POST':
        url = request.form['long_url']
        rand_time = str(round(time.time()*100000))[-9:]
        data.append({'long_url': url, 'id': rand_time})
        shortened_url = home_url + rand_time
        print(data)
        return render_template('response.html', title= 'Shorten URL | Response', url=shortened_url)
    else:
        return 'wrong route'


if __name__ == '__main__':
    app.run(debug=True)