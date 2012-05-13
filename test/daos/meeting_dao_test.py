from google.appengine.ext import testbed
import datetime
from daos.meeting_dao import MeetingDAO
from models.meeting import Meeting
from nose.tools import eq_


class meeting_dao_test:
    def setup(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.meeting_dao = MeetingDAO()

        self.today = datetime.datetime.now()
        self.past_week = self.today - datetime.timedelta(days=7)
        self.yesterday = self.today - datetime.timedelta(days=1)
        self.next_hour = self.today + datetime.timedelta(hours=1)
        self.tomorrow = self.today + datetime.timedelta(days=1)

    def teardown(self):
        self.testbed.deactivate()

    def should_bring_nothing_if_there_is_not_a_meeting(self):
        assert self.meeting_dao.next() == None

    def should_bring_nothing_if_there_are_only_past_meetings(self):
        past_meeting = Meeting(day=self.yesterday)
        self.meeting_dao.insert(past_meeting)

        assert self.meeting_dao.next() is None
        assert self.meeting_dao.all() is not None

    def should_bring_only_the_next_meeting(self):
        assert self.meeting_dao.next() is None

        past_meeting = Meeting(day=self.yesterday)
        next_meeting = Meeting(day=self.next_hour)
        another_meeting = Meeting(day=self.tomorrow)

        self.meeting_dao.insert(past_meeting)
        self.meeting_dao.insert(next_meeting)
        self.meeting_dao.insert(another_meeting)

        assert self.meeting_dao.next() == next_meeting

    def should_bring_all_the_past_meetings(self):
        first_meeting = Meeting(day=self.past_week)
        second_meeting = Meeting(day=self.yesterday)
        next_meeting = Meeting(day=self.next_hour)
        another_meeting = Meeting(day=self.tomorrow)

        self.meeting_dao.insert(first_meeting)
        self.meeting_dao.insert(second_meeting)
        self.meeting_dao.insert(next_meeting)
        self.meeting_dao.insert(another_meeting)

        past_meetings = [first_meeting, second_meeting]
        result = [m for m in self.meeting_dao.previous_meetings()]

        eq_(past_meetings, result)

    def should_get_a_meeting_by_key(self):
        meeting = Meeting(day=self.yesterday)
        saved_meeting_key = self.meeting_dao.insert(meeting)
        loaded_meeting = self.meeting_dao.get_by_key(str(saved_meeting_key))

        eq_(loaded_meeting, meeting)
