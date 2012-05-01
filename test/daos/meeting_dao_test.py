from google.appengine.ext import testbed
import datetime
from daos.meeting_dao import MeetingDAO
from models.meeting import Meeting

class meeting_dao_test:
    def setup(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.meeting_dao = MeetingDAO()

        self.today = datetime.datetime.now()
        self.yesterday = self.today - datetime.timedelta(days = 1)
        self.next_hour = self.today + datetime.timedelta(hours = 1)
        self.tomorrow = self.today + datetime.timedelta(days = 1)

    def teardown(self):
        self.testbed.deactivate()

    def should_bring_nothing_if_there_is_not_a_meeting(self):
        assert self.meeting_dao.next() == None

    def should_bring_nothing_if_there_are_only_past_meetings(self):
        past_meeting = Meeting(day = self.yesterday)
        self.meeting_dao.insert(past_meeting)

        assert self.meeting_dao.next() is None
        assert self.meeting_dao.all() is not None

    def should_bring_only_the_next_meeting(self):
        assert self.meeting_dao.next() is None

        past_meeting = Meeting(day = self.yesterday)
        next_meeting = Meeting(day = self.next_hour)
        another_meeting = Meeting(day = self.tomorrow)

        self.meeting_dao.insert(past_meeting)
        self.meeting_dao.insert(next_meeting)
        self.meeting_dao.insert(another_meeting)

        assert self.meeting_dao.next() == next_meeting
