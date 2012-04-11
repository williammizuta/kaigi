from google.appengine.ext import db

class Kaigi(db.Model):
    name = db.StringProperty(required=True)
    description = db.TextProperty()
