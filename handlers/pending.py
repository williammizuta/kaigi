import tornado.web
from google.appengine.api import mail

from handlers.base import BaseHandler

class PendingHandler(BaseHandler):
    def initialize(self, user_dao):
        self.user_dao = user_dao

    #TODO: we need to write message body
    def send_email(self):
        admin_email = self.user_dao.get_admin().get_email()
        mail.send_mail(sender=admin_email,
                    subject="New user",
                    to=admin_email,
                    body="body")

    @tornado.web.authenticated
    def get(self):
        self.send_email()
        self.render('pending.html')

    @tornado.web.authenticated
    def post(self):
        self.check_xsrf_cookie()
        self.user_dao.remove(self.get_current_user())
        self.redirect('/')
