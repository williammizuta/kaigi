import tornado.web

from handlers.base import BaseHandler

class HomeHandler(BaseHandler):
    def initialize(self, user_dao):
        self.user_dao = user_dao

    def get(self):
        if (self.user_dao.has_no_user()):
            self.redirect('/setup')
        elif (self.get_current_user() is None):
            self.render('home.html')
        else:
            self.redirect('/dashboard')
