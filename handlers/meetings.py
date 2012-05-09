import tornado.web

from handlers.base import BaseHandler
import decorators.user

class MeetingsHandler(BaseHandler):
    def initialize(self, user_dao, meeting_dao):
        self.user_dao = user_dao
        self.meeting_dao = meeting_dao

    @decorators.user.approved
    def get(self, meeting_key):
        self.render('meeting.html',
                meeting=self.meeting_dao.get_by_key(meeting_key))
