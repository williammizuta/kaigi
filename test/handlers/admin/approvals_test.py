from handlers.admin.approvals import ApprovalsHandler
from daos.user_dao import UserDAO
from models.user import User
from google.appengine.api import users
from mockito import mock, when, verify, any

class approvals_handler_test:

    def setup(self):
        self.handler = object.__new__(ApprovalsHandler)
        self.user_dao = mock(UserDAO)
        self.handler.initialize(self.user_dao)
        when(self.handler).redirect().thenReturn(None)
        when(self.handler).render().thenReturn(None)

        self.google_user = users.User(email='admin@gmail.com')
        self.admin = User(user=self.google_user, status='ADMIN')
        when(self.handler).get_current_user().thenReturn(self.google_user)
        when(self.user_dao).load(self.google_user).thenReturn(self.admin)

    def should_list_users_pending_approval(self):
        pending_user = users.User(email='pending@gmail.com')
        pending = [User(user=pending_user)]
        when(self.user_dao).list_pending_approval().thenReturn(pending)

        self.handler.get()

        verify(self.handler).render('pending_approval.html', users=pending)
