import tornado.web

from handlers.base import BaseHandler
import decorators.user

class DashboardHandler(BaseHandler):
    def initialize(self, user_dao):
        self.user_dao = user_dao

    @decorators.user.approved
    def get(self):
        self.render('dashboard.html')
