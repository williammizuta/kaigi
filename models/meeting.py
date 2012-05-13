from google.appengine.ext import db


class Meeting(db.Model):
    day = db.DateTimeProperty(required=True)
    minute = db.TextProperty()
    tags = db.ListProperty(db.Category)
    owner = db.UserProperty(auto_current_user_add=True)

    def __eq__(self, other):
        if isinstance(other, Meeting):
            return self.day == other.day
        return NotImplemented
