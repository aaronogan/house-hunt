from flask import Flask, jsonify, render_template, request
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'house-hunt',
}
app.config['DEBUG_TB_PANELS'] = {
    "flask_debugtoolbar.panels.versions.VersionDebugPanel",
    "flask_debugtoolbar.panels.timer.TimerDebugPanel",
    "flask_debugtoolbar.panels.headers.HeaderDebugPanel",
    "flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel",
    "flask_debugtoolbar.panels.template.TemplateDebugPanel",
    "flask_debugtoolbar.panels.logger.LoggingPanel",
    "flask_mongoengine.panels.MongoDebugPanel",
}

db = MongoEngine(app)
app.session_interface = MongoEngineSessionInterface(db)
toolbar = DebugToolbarExtension(app)

class ForSale(db.Document):
    baths = db.FloatField()
    beds = db.IntField()
    city = db.StringField()
    created = db.DateField()
    garage = db.FloatField()
    href = db.StringField()
    last_update_date = db.DateField()
    lat = db.LongField()
    line = db.StringField()
    list_date = db.DateField()
    listing_id = db.StringField()
    list_price = db.LongField()
    lon = db.LongField()
    name = db.StringField()
    permalink = db.StringField()
    postal_code = db.StringField()
    property_id = db.StringField()
    sold_price = db.LongField()
    sqft = db.IntField()
    state_code = db.StringField()
    status = db.StringField()
    stories = db.IntField()
    sub_type = db.StringField()
    type = db.StringField()
    year_built = db.IntField()

class Coding(db.Document):
    listing_id = db.StringField()
    value = db.StringField()

@app.route('/', methods=['GET'])
def list():
    return render_template('list.html')

@app.route('/api/v1.0/listings/', methods=['GET'])
def listings():
    listings = ForSale.objects().all()
    return jsonify({
        "status": 200,
        "data": listings,
    }), 200

@app.route('/api/v1.0/codings/', methods=['GET'])
def codings():
    codings = Coding.objects().all()
    return jsonify({
        "status": 200,
        "data": codings,
    }), 200

@app.route('/api/v1.0/codings/<string:listing_id>', methods=['GET', 'POST'])
def codings_item(listing_id):
    if (request.method == 'GET'):
        return jsonify({
            "status": 200,
            "data": None,
        }), 200

    content = request.get_json(silent=True)
    value = content['value']

    coding = Coding(listing_id=listing_id, value=value)
    coding.save()

    return jsonify({
        "status": 200,
        "data": {
            "listing_id": listing_id,
            "value": value,
        },
    }), 200

if __name__ == '__main__':
    app.run(debug=True)

