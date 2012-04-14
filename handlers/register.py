import tornado.web

from handlers.base import BaseHandler

class RegisterHandler(BaseHandler):
    def initialize(self, user_dao):
        self.user_dao = user_dao

    @tornado.web.authenticated
    def get(self):
        if self.user_dao.load(self.get_current_user()) is None:
            return self.render('register.html')
        self.redirect('/dashboard')

    @tornado.web.authenticated
    def post(self):
        self.check_xsrf_cookie()
        self.user_dao.insert(self.get_current_user())
        self.redirect(self.get_approve_pending_url())
