import tornado.web
from models.meeting import Meeting
from google.appengine.ext import db

class IndexHandler(tornado.web.RequestHandler):
    def initialize(self, meetings):
        self.meetings = meetings
        self.meetings.insert(Meeting(tags=[db.Category("test"), db.Category("gae")]))

    def get(self):
        self.render('index.html', meetings=self.meetings.all())
