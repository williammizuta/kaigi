from google.appengine.ext import db

import tornado.web

from handlers.base import BaseHandler
from models.meeting import Meeting

class IndexHandler(BaseHandler):
    def initialize(self, user_dao):
        self.user_dao = user_dao

    @tornado.web.authenticated
    def get(self):
        if (user_dao.has_no_user()):
            self.render('setup.html')
