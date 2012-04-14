import tornado.web

from handlers.base import BaseHandler
import decorators.user

class DashboardHandler(BaseHandler):
    def initialize(self, user_dao):
        self.user_dao = user_dao

    def get(self):
        @decorators.user.approved(self.user_dao)
        def run(self):
            self.render('dashboard.html')
        run(self)
