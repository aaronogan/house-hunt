from flask import Flask, render_template
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

@app.route('/')
def list():
    listings = ForSale.objects().all()
    return render_template('list.html', listings=listings)

if __name__ == '__main__':
    app.run(debug=True)

