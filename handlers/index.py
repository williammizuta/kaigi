import tornado.web

from handlers.base import BaseHandler
from decorators.user import user

class IndexHandler(BaseHandler):
    def initialize(self, user_dao):
        self.user_dao = user_dao

    @user
    def get(self):
        pass