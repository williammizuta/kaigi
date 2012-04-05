from google.appengine.ext import db

class Meeting(db.Model):
    day = db.DateProperty(auto_now_add=True)
    minute = db.TextProperty()
    tags = db.ListProperty(db.Category)
    owner = db.UserProperty(auto_current_user_add=True)
