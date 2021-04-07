from flask import Flask, jsonify, render_template, request
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface, DoesNotExist
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
        "errors": [],
    }), 200

@app.route('/api/v1.0/codings/', methods=['GET'])
def codings():
    codings = Coding.objects().all()
    return jsonify({
        "status": 200,
        "data": codings,
        "errors": [],
    }), 200

@app.route('/api/v1.0/codings/<string:listing_id>', methods=['POST'])
def coding_create(listing_id):
    content = request.get_json(silent=True)
    value = content['value']

    try:
        existing = Coding.objects.get(listing_id=listing_id)
        return jsonify({
            "status": 500,
            "data": None,
            "errors": ["Coding already exists for listing"],
        }), 500
    except DoesNotExist:
        pass

    coding = Coding(listing_id=listing_id, value=value)
    coding.save()

    return jsonify({
        "status": 200,
        "data": {
            "listing_id": listing_id,
            "value": value,
        },
        "errors": [],
    }), 200

@app.route('/api/v1.0/codings/<string:listing_id>', methods=['GET'])
def coding_read(listing_id):
    try:
        coding = Coding.objects.get(listing_id=listing_id)
        return jsonify({
            "status": 200,
            "data": coding,
            "errors": [],
        }), 200
    except DoesNotExist:
        return jsonify({
            "status": 404,
            "data": None,
            "errors": ["Coding not found for listing"],
        }), 404

@app.route('/api/v1.0/codings/<string:listing_id>', methods=['PUT'])
def coding_update(listing_id):
    content = request.get_json(silent=True)
    value = content['value']

    try:
        coding = Coding.objects.get(listing_id=listing_id)
        coding.update(
            set__value = value,
        )

        return jsonify({
            "status": 200,
            "data": coding,
            "errors": [],
        }), 200

    except DoesNotExist:
        return jsonify({
            "status": 404,
            "data": None,
            "errors": ["Coding not found for listing"],
        }), 404

if __name__ == '__main__':
    app.run(debug=True)

