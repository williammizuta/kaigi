from google.appengine.api import mail
from handlers.base import BaseHandler
from decorators.user import admin


class ApprovalsHandler(BaseHandler):
    def initialize(self, user_dao):
        self.user_dao = user_dao

    # TODO create the email
    def send_email(self, user_key):
        admin_email = self.user_dao.get_admin().get_email()
        user_email = self.user_dao.get_by_key(user_key).get_email()
        mail.send_mail(sender=admin_email,
                    subject="Welcome to Kaigi!",
                    to=user_email,
                    body="body")

    @admin
    def get(self):
        pending = self.user_dao.list_pending_approval()
        self.render('pending_approval.html', users=pending)

    @admin
    def post(self):
        user_key = self.get_argument('key')
        self.user_dao.approve(user_key)
        self.send_email(user_key)
        self.redirect('/admin/approvals')
