from handlers.admin.approvals import ApprovalsHandler
from daos.user_dao import UserDAO
from models.user import User
from google.appengine.api import users, mail
from mockito import mock, when, verify


class approvals_handler_test:

    def setup(self):
        self.handler = object.__new__(ApprovalsHandler)
        self.user_dao = mock(UserDAO)
        self.handler.initialize(self.user_dao)
        when(self.handler).redirect().thenReturn(None)
        when(self.handler).render().thenReturn(None)
        when(mail).send_mail().thenReturn(None)

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

    def should_mark_an_user_as_approved_and_send_him_an_email_and_redirect_to_the_list(self):
        to_be_approved_mail = 'pending@gmail.com'
        to_be_approved_key = 'abc123'
        to_be_approved = User(user=users.User(email=to_be_approved_mail))

        when(self.handler).get_argument('key').thenReturn(to_be_approved_key)
        when(self.user_dao).get_admin().thenReturn(self.admin)
        when(self.user_dao).get_by_key(to_be_approved_key).thenReturn(to_be_approved)

        self.handler.post()

        verify(self.user_dao).approve(to_be_approved_key)
        verify(self.handler).redirect('/admin/approvals')
        verify(mail).send_mail(sender=self.admin.get_email(),
                    subject="Welcome to Kaigi!",
                    to=to_be_approved_mail,
                    body="body")
