from handlers.pending import PendingHandler
from mockito import mock, when, verify
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
        when(mail).send_mail().thenReturn(None)

    def should_register_user_and_send_email_and_render_pending_page_when_getting_if_authenticated_and_user_not_registered(self):
        when(self.user_dao).get_admin().thenReturn(self.admin_user)
        when(self.admin_user).get_email().thenReturn(self.admin_email)
        when(self.user_dao).load(self.logged_user).thenReturn(None)

        self.handler.get()

        verify(self.handler).render('pending.html')
        verify(mail).send_mail(sender=self.admin_email, subject="New user", to=self.admin_email, body="body")
        verify(self.user_dao).insert(self.logged_user)

    def should_render_pending_page_when_getting_if_authenticated_and_user_registered(self):
        registered_user = mock()
        when(self.user_dao).load(self.logged_user).thenReturn(registered_user)
        when(registered_user).is_approved().thenReturn(False)

        self.handler.get()

        verify(self.handler).render('pending.html')

    def should_redirect_to_dashboard_if_authenticated_user_is_registered_and_approved(self):
        registered_user = mock()
        when(self.user_dao).load(self.logged_user).thenReturn(registered_user)
        when(registered_user).is_approved().thenReturn(True)

        self.handler.get()

        verify(self.handler).redirect('/dashboard')

    def should_check_xsrf_cookie(self):
        when(self.handler).check_xsrf_cookie().thenRaise(NotImplementedError("FAIL!"))

        try:
            self.handler.post()
            raise AssertionError("Did not check XSRF cookie!")
        except NotImplementedError:
            pass  # success

    def should_remove_current_user_from_database_and_redirect_to_home(self):
        when(self.handler).check_xsrf_cookie().thenReturn(None)

        self.handler.post()

        verify(self.user_dao).remove(self.logged_user)
        verify(self.handler).redirect('/')
