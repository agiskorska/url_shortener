from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.get('/')
def index():
    return render_template('search.html', title='Shorten URL' )

@app.route('/shortened', methods=['POST'])
def shortened():
    return render_template('response.html', title= 'Shorten URL | Response', url='http://google.com')

if __name__ == '__main__':
    app.run(debug=True)