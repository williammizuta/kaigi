from handlers.admin.meetings import NewMeetingHandler
from mockito import mock, when, verify, any
from models.meeting import Meeting
import forms.meeting
import datetime


class new_meeting_handler_test:

    def setup(self):
        self.handler = object.__new__(NewMeetingHandler)
        self.user_dao = mock()
        self.meeting_dao = mock()
        self.form = mock()
        self.logged_user = mock()
        self.handler.initialize(self.user_dao, self.meeting_dao)

        when(self.handler).redirect().thenReturn(None)
        when(self.handler).render().thenReturn(None)

        when(self.handler).get_current_user().thenReturn(self.logged_user)
        when(self.user_dao).load(self.logged_user).thenReturn(self.logged_user)
        when(self.logged_user).is_admin().thenReturn(True)

        when(forms.meeting).new_meeting_form(self.handler).thenReturn(self.form)

    def should_check_xsrf_cookie(self):
        when(self.handler).check_xsrf_cookie().thenRaise(NotImplementedError("FAIL!"))

        try:
            self.handler.post()
            raise AssertionError("Did not check XSRF cookie!")
        except NotImplementedError:
            pass  # success

    def should_save_a_new_meeting_and_redirect_to_dashboard_if_form_is_valid(self):
        when(self.handler).check_xsrf_cookie().thenReturn(None)
        when(self.form).validate().thenReturn(True)
        when(self.form).get_data().thenReturn({'day': datetime.datetime.today()})

        self.handler.post()

        verify(self.meeting_dao).insert(any(Meeting))
        verify(self.handler).redirect('/dashboard')

    def should_render_form_again_if_form_is_not_valid(self):
        when(self.handler).check_xsrf_cookie().thenReturn(None)
        when(self.form).validate().thenReturn(False)

        self.handler.post()

        verify(self.handler).render('new_meeting.html', form=self.form)
