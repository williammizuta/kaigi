from daos.user_dao import UserDAO
from google.appengine.api import users
from mockito import mock, when, verify, any
from decorators.user import *
from models.user import User

class user_approved_test:

    def setup(self):
        self.user_dao = mock(UserDAO)
        self.current_user = users.User(email='user@gmail.com')
        self.handler = mock_handler(self.current_user, self.user_dao)

        when(self.handler).get_current_user().thenReturn(self.current_user)
        when(self.handler).redirect().thenReturn(None)

    def should_redirect_to_home_if_current_user_is_not_registered(self):
        when(self.user_dao).load(self.current_user).thenReturn(None)

        self.handler.mock_method()

        verify(self.handler).redirect("/")

    def should_redirect_to_approve_pending_url_if_current_user_is_registered_but_pending_approval(self):
        user_pending_approval = User(user=self.current_user, status='PENDING')
        approve_pending_url = '/123'

        when(self.user_dao).load(self.current_user).thenReturn(user_pending_approval)
        when(self.handler).get_approve_pending_url().thenReturn(approve_pending_url)

        self.handler.mock_method()

        verify(self.handler).redirect(approve_pending_url)

class mock_handler:
    def __init__(self, current_user, user_dao):
        self.current_user = current_user
        self.user_dao = user_dao

    @approved
    def mock_method(self):
        pass

    def get_current_user(self):
        pass

    def redirect(self, url):
        pass

    def get_approve_pending_url(self):
        pass
