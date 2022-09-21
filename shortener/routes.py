from shortener import app
from flask import render_template, request, redirect
import time
from shortener.data import Url
from shortener import db 
from werkzeug import exceptions

home_url = 'http://127.0.0.1:5000/'

db.create_all()

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
    url = Url.query.filter_by(id=id).first_or_404()
    print(url)
    return redirect(url, code=302)

@app.get('/thankyou')
def thankyou():
    return '<h1>thank you!</h1>'

@app.errorhandler(404)
def page_not_found(_):
    print('hit')
    return render_template('errors/404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
