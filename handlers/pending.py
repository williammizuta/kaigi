import tornado.web

from handlers.base import BaseHandler

class PendingHandler(BaseHandler):
    def initialize(self, user_dao):
        self.user_dao = user_dao

    @tornado.web.authenticated
    def get(self):
        user = self.get_current_user()
        self.render('pending.html', user=user)

    @tornado.web.authenticated
    def post(self):
        self.check_xsrf_cookie()
        self.user_dao.remove(self.get_current_user())
        self.redirect('/')
