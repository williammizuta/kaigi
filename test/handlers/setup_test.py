from handlers.setup import SetupHandler
from mockito import mock, when, verify, any
from models.kaigi import Kaigi
import forms.kaigi


class setup_handler_test:

    def setup(self):
        self.handler = object.__new__(SetupHandler)
        self.user_dao = mock()
        self.kaigi_dao = mock()
        self.form = mock()
        self.logged_user = mock()
        self.handler.initialize(self.user_dao, self.kaigi_dao)

        when(self.handler).redirect().thenReturn(None)
        when(self.handler).render().thenReturn(None)
        when(self.handler).get_current_user().thenReturn(self.logged_user)
        when(forms.kaigi).kaigi_form(self.handler).thenReturn(self.form)

    def should_render_setup_form_when_getting_if_authenticated_and_no_kaigi_exists(self):
        when(self.kaigi_dao).get().thenReturn(None)

        self.handler.get()

        verify(self.handler).render('setup.html', form=self.form)

    def should_redirect_to_dashboard_if_there_is_a_kaigi_already(self):
        existing_kaigi = mock()
        when(self.kaigi_dao).get().thenReturn(existing_kaigi)

        self.handler.get()

        verify(self.handler).redirect('/dashboard')

    def should_check_xsrf_cookie(self):
        when(self.handler).check_xsrf_cookie().thenRaise(NotImplementedError("FAIL!"))

        try:
            self.handler.post()
            raise AssertionError("Did not check XSRF cookie!")
        except NotImplementedError:
            pass  # success

    def should_save_a_new_kaigi_and_the_current_user_as_admin_if_form_is_valid(self):
        when(self.handler).check_xsrf_cookie().thenReturn(None)
        when(self.form).validate().thenReturn(True)
        when(self.form).get_data().thenReturn({'name': 'test'})

        self.handler.post()

        verify(self.user_dao).insert_admin(self.logged_user)
        verify(self.kaigi_dao).insert(any(Kaigi))
        verify(self.handler).redirect('/dashboard')

    def should_render_setup_form_again_if_form_is_not_valid(self):
        when(self.handler).check_xsrf_cookie().thenReturn(None)
        when(self.form).validate().thenReturn(False)

        self.handler.post()

        verify(self.handler).render('setup.html', form=self.form)
