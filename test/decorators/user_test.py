from daos.user_dao import UserDAO
from google.appengine.api import users
from mockito import mock, when, verify, any
from decorators.user import *
from models.user import User

class user_approved_test:

    def setup(self):
        def mock_method():
            pass
        self.handler = mock()
        self.user_dao = mock(UserDAO)
        self.current_user = users.User(email='user@gmail.com')
        self.decorated_method = approved(self.user_dao)(mock_method)

        when(self.handler).get_current_user().thenReturn(self.current_user)

    def should_redirect_to_home_if_current_user_is_not_registered(self):
        when(self.user_dao).load(self.current_user).thenReturn(None)

        self.decorated_method(self.handler)

        verify(self.handler).redirect("/")

    def should_redirect_to_approve_pending_url_if_current_user_is_registered_but_pending_approval(self):
        user_pending_approval = User(user=self.current_user, status='PENDING')
        approve_pending_url = '/123'

        when(self.user_dao).load(self.current_user).thenReturn(user_pending_approval)
        when(self.handler).get_approve_pending_url().thenReturn(approve_pending_url)

        self.decorated_method(self.handler)

        verify(self.handler).redirect(approve_pending_url)
