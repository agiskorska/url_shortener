from flask import Flask, render_template, request, redirect
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import time
from db.data import Url

home_url = 'http://127.0.0.1:5000/'


app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///url.db'
db  = SQLAlchemy(app)

@app.get('/')
def index():
    return render_template('search.html', title='Shorten URL' )

@app.route('/shortened', methods=['POST'])
def shortened():
    if request.method == 'POST':
        url = request.form['long_url']
        rand_time = str(round(time.time()*100000))[-9:]
        new_url = Url(id=rand_time, long_url=url)
        db.session.add(new_url)
        db.session.commit()
        shortened_url = home_url + rand_time
        print(db)
        return render_template('response.html', title= 'Shorten URL | Response', url=shortened_url)
    else:
        return 'wrong route'

@app.get('/<id>')
def redirect_to_url(id):
    url = Url.query.filter_by(id=id).first()
    print(url)
    return redirect(url, code=302)

@app.get('/thankyou')
def thankyou():
    return '<h1>thank you!</h1>'

if __name__ == '__main__':
    app.run(debug=True)