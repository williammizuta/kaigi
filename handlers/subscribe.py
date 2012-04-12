import tornado.web

from handlers.base import BaseHandler

class SubscribeHandler(BaseHandler):
    def initialize(self, user_dao):
        self.user_dao = user_dao

    @tornado.web.authenticated
    def get(self):
        self.render("subscribe.html", xsrf_field=self.xsrf_form_html())

    @tornado.web.authenticated
    def post(self):
        self.check_xsrf_cookie()
        self.user_dao.insert(self.get_current_user())
        self.redirect(self.get_approve_pending_url())
