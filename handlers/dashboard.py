import tornado.web

from handlers.base import BaseHandler
import decorators.user

class DashboardHandler(BaseHandler):
    def initialize(self, user_dao, meeting_dao):
        self.user_dao = user_dao
        self.meeting_dao = meeting_dao

    @decorators.user.approved
    def get(self):
        self.render('dashboard.html',
                next_meeting = self.meeting_dao.next(),
                previous_meetings = self.meeting_dao.previous_meetings())
