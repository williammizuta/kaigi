from handlers.home import HomeHandler
from daos.user_dao import UserDAO
from mockito import mock, when, verify, any

class home_handler_test:

    def setup(self):
        self.handler = object.__new__(HomeHandler)
        self.user_dao = mock(UserDAO)
        self.handler.initialize(self.user_dao)
        when(self.handler).redirect().thenReturn(None)
        when(self.handler).render().thenReturn(None)

    def should_redirect_to_setup_if_no_user_is_registered(self):
        when(self.user_dao).has_no_user().thenReturn(True)
        self.handler.get()
        verify(self.handler).redirect('/setup')

    def should_render_home_page_if_no_user_is_logged_in_but_there_are_registered_users(self):
        when(self.user_dao).has_no_user().thenReturn(False)
        when(self.handler).get_current_user().thenReturn(None)

        self.handler.get()

        verify(self.handler).render('home.html')

    def should_redirect_to_dashboard_if_there_is_a_registered_user_and_there_is_a_logged_user(self):
        logged_user = mock()
        when(self.user_dao).has_no_user().thenReturn(False)
        when(self.user_dao).load(logged_user).thenReturn(logged_user)
        when(self.handler).get_current_user().thenReturn(logged_user)

        self.handler.get()

        verify(self.handler).redirect('/dashboard')
