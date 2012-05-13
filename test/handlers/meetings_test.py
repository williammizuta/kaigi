from handlers.meetings import MeetingsHandler
from daos.meeting_dao import MeetingDAO
from daos.user_dao import UserDAO
from models.meeting import Meeting
from datetime import datetime
from mockito import mock, when, verify


class meetings_handler_test:

    def setup(self):
        self.handler = object.__new__(MeetingsHandler)
        self.user_dao = mock(UserDAO)
        self.meeting_dao = mock(MeetingDAO)
        self.handler.initialize(self.user_dao, self.meeting_dao)
        when(self.handler).redirect().thenReturn(None)
        when(self.handler).render().thenReturn(None)

        logged_user = mock()
        approved_user = mock()
        when(self.handler).get_current_user().thenReturn(logged_user)
        when(self.user_dao).load(logged_user).thenReturn(approved_user)
        when(approved_user).is_approved().thenReturn(True)

    def should_render_the_page_for_a_meeting(self):
        meeting = Meeting(day=datetime.today())
        meeting_key = 'abc123'
        when(self.meeting_dao).get_by_key(meeting_key).thenReturn(meeting)

        self.handler.get(meeting_key)

        verify(self.handler).render('meeting.html', meeting=meeting)
