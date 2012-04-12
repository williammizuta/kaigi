import tornado.web

from handlers.base import BaseHandler

class HomeHandler(BaseHandler):
    def initialize(self, user_dao, kaigi_dao):
        self.user_dao = user_dao
        self.kaigi_dao = kaigi_dao

    def get(self):
        if (self.user_dao.has_no_user()):
            self.redirect('/setup')
        elif (self.get_current_user() is None):
            kaigi = self.kaigi_dao.get()
            self.render('home.html', kaigi=kaigi)
        else:
            self.redirect('/index')
