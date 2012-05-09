from google.appengine.ext import db
from datetime import datetime
from models.meeting import Meeting

class MeetingDAO:
    def all(self):
        return Meeting.all()

    def insert(self, meeting):
        return meeting.put()

    def next(self):
        meetings = Meeting.all()
        meetings.filter("day >=", datetime.now())
        meetings.order("day")
        return meetings.get()

    def previous_meetings(self):
        meetings = Meeting.all()
        meetings.filter("day <", datetime.now())
        meetings.order("day")
        return meetings

    def get_by_key(self, key):
        return Meeting.all().filter("__key__ = ", db.Key(key)).get()
