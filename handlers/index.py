from google.appengine.ext import db

import tornado.web

from handlers.base import BaseHandler
from models.meeting import Meeting

class IndexHandler(BaseHandler):
    def initialize(self, meetings):
        self.meetings = meetings

    @tornado.web.authenticated
    def get(self):
        self.render('index.html', meetings=self.meetings.all())
