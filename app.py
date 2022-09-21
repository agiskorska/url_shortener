from flask import Flask, render_template, request, redirect
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

@app.get('/<id>')
def redirect_to_url(id):
    url = next((i['long_url'] for i in data if i['id'] == id), None)
    print(url)
    return redirect('https://google.com', code=302)

if __name__ == '__main__':
    app.run(debug=True)