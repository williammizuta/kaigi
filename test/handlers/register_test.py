from handlers.register import RegisterHandler
from daos.user_dao import UserDAO
from mockito import mock, when, verify, any

class register_handler_test:

    def setup(self):
        self.handler = object.__new__(RegisterHandler)
        self.user_dao = mock(UserDAO)
        self.handler.initialize(self.user_dao)
        when(self.handler).redirect().thenReturn(None)
        when(self.handler).render().thenReturn(None)

        self.wanting_to_register = mock()
        when(self.handler).get_current_user().thenReturn(self.wanting_to_register)

    def should_render_register_page_if_current_user_is_wanting_to_register_yet(self):
        when(self.user_dao).load(self.wanting_to_register).thenReturn(None)

        self.handler.get()

        verify(self.handler).render('register.html')

    def should_redirect_to_dashboard_if_already_registered(self):
        when(self.user_dao).load(self.wanting_to_register).thenReturn(self.wanting_to_register)

        self.handler.get()

        verify(self.handler).redirect('/dashboard')

    def should_check_xsrf_cookie_when_registering(self):
        when(self.handler).check_xsrf_cookie().thenRaise(NotImplementedError("FAIL!"))

        try:
            self.handler.post()
            raise AssertionError("Did not check XSRF cookie!")
        except NotImplementedError, e:
            pass # success

    def should_register_the_logged_user_and_redirect_to_pending_approval(self):
        when(self.handler).check_xsrf_cookie().thenReturn(None)

        self.handler.post()

        verify(self.user_dao).insert(self.wanting_to_register)
        verify(self.handler).redirect(self.handler.get_approve_pending_url())
