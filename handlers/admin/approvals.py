import tornado.web

from handlers.base import BaseHandler

class ApprovalsHandler(BaseHandler):
    def initialize(self, user_dao):
        self.user_dao = user_dao

    def get(self):
        self.render('pending_approval.html', users=self.user_dao.list_pending_approval())
