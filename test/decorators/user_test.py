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

    def should_get_or_register_current_user_and_redirect_to_approve_pending_url_if_not_registered(self):
        new_or_existing_user = User(user=self.current_user)
        approve_pending_url = '/123'

        when(self.handler).get_approve_pending_url().thenReturn(approve_pending_url)
        when(self.user_dao).get_or_create(self.current_user).thenReturn(new_or_existing_user)

        self.handler.method_for_approved_users()

        verify(self.handler).redirect(approve_pending_url)

    def should_call_handler_method_if_user_is_approved(self):
        approved_user = User(user=self.current_user, status='APPROVED')
        when(self.user_dao).get_or_create(self.current_user).thenReturn(approved_user)

        self.handler.method_for_approved_users()

        assert self.handler.called == True

class user_admin_test:

    def setup(self):
        self.user_dao = mock(UserDAO)
        self.current_user = users.User(email='user@gmail.com')
        self.handler = mock_handler(self.current_user, self.user_dao)

        when(self.handler).get_current_user().thenReturn(self.current_user)
        when(self.handler).redirect().thenReturn(None)
        when(self.handler).send_error().thenReturn(None)

    def should_redirect_to_home_if_unregistered_user_tries_to_access_admin_area(self):
        when(self.user_dao).load(self.current_user).thenReturn(None)

        self.handler.method_for_admins()

        verify(self.handler).redirect('/')

    def should_show_404_page_if_non_admin_tries_to_access_admin_area(self):
        not_admin = User(user=self.current_user, status='APPROVED')
        when(self.user_dao).load(self.current_user).thenReturn(not_admin)

        self.handler.method_for_admins()

        verify(self.handler).send_error(404)

    def should_call_handler_method_if_user_is_admin(self):
        admin = User(user=self.current_user, status='ADMIN')

        when(self.user_dao).load(self.current_user).thenReturn(admin)

        self.handler.method_for_admins()

        assert self.handler.called == True

class mock_handler:
    def __init__(self, current_user, user_dao):
        self.current_user = current_user
        self.user_dao = user_dao
        self.called = False

    @approved
    def method_for_approved_users(self):
        self.called = True

    @admin
    def method_for_admins(self):
        self.called = True

    def get_current_user(self):
        pass

    def redirect(self, url):
        pass

    def get_approve_pending_url(self):
        pass

    def send_error(self, error_code):
        pass
