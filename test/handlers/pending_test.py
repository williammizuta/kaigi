from handlers.pending import PendingHandler
from models.user import User
from mockito import mock, when, verify, any
from google.appengine.api import mail

class pending_handler_test:

    def setup(self):
        self.handler = object.__new__(PendingHandler)
        self.user_dao = mock()
        self.logged_user = mock()
        self.logged_user_email = "newuser@gmail.com"
        self.admin_user = mock()
        self.admin_email = "email@gmail.com"
        self.handler.initialize(self.user_dao)

        when(self.handler).redirect().thenReturn(None)
        when(self.handler).render().thenReturn(None)
        when(self.handler).get_current_user().thenReturn(self.logged_user)
        when(self.logged_user).get_email().thenReturn(self.logged_user_email)
        when(mail).send_mail().thenReturn(None)

    def should_register_user_and_send_email_and_render_pending_page_when_getting_if_authenticated(self):
        when(self.user_dao).get_admin().thenReturn(self.admin_user)
        when(self.admin_user).get_email().thenReturn(self.admin_email)

        self.handler.get()

        verify(self.handler).render('pending.html')
        verify(mail).send_mail(sender=self.admin_email, subject="New user", to=self.logged_user_email, body="body")

    def should_check_xsrf_cookie(self):
        when(self.handler).check_xsrf_cookie().thenRaise(NotImplementedError("FAIL!"))

        try:
            self.handler.post()
            raise AssertionError("Did not check XSRF cookie!")
        except NotImplementedError, e:
            pass # success

    def should_remove_current_user_from_database_and_redirect_to_home(self):
        when(self.handler).check_xsrf_cookie().thenReturn(None)

        self.handler.post()

        verify(self.user_dao).remove(self.logged_user)
        verify(self.handler).redirect('/')
