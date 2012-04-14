from handlers.pending import PendingHandler
from models.user import User
from mockito import mock, when, verify, any

class pending_handler_test:

    def setup(self):
        self.handler = object.__new__(PendingHandler)
        self.user_dao = mock()
        self.logged_user = mock()
        self.user = mock()
        self.email = "email@gmail.com"
        self.handler.initialize(self.user_dao)

        when(self.handler).redirect().thenReturn(None)
        when(self.handler).render().thenReturn(None)
        when(self.handler).get_current_user().thenReturn(self.logged_user)

    #TODO: discover how to test e-mail

    def should_render_pending_page_when_getting_if_authenticated(self):
        when(self.user_dao).get_admin().thenReturn(self.user)
        when(self.user).get_email().thenReturn(self.email)
        self.handler.get()

        verify(self.handler).render('pending.html')

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