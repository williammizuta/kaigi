import tornado.web

from handlers.base import BaseHandler
from decorators.user import admin

class ApprovalsHandler(BaseHandler):
    def initialize(self, user_dao):
        self.user_dao = user_dao

    @admin
    def get(self):
        pending = self.user_dao.list_pending_approval()
        self.render('pending_approval.html', users=pending)
