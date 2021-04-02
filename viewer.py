from flask import Flask, render_template
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'house-hunt',
}

db = MongoEngine()
db.init_app(app)

@app.route('/')
def list():
    listings = [{
        "listing_id": "1234",
        "list_price": 500000,
        "baths": 2,
        "beds": 3,
        "permalink": "abcd",
    }, {
        "listing_id": "1234",
        "list_price": 500000,
        "baths": 2,
        "beds": 3,
        "permalink": "abcd",
    }]
    return render_template('list.html', listings=listings)

if __name__ == '__main__':
    app.run(debug=True)

