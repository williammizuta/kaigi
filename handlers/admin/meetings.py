import tornado.web

from handlers.base import BaseHandler
from decorators.user import admin
from forms.meeting import new_meeting_form

class NewMeetingHandler(BaseHandler):
    def initialize(self, user_dao, meeting_dao):
        self.user_dao = user_dao
        self.meeting_dao = meeting_dao

    @admin
    def get(self):
        self.render('new_meeting.html', form=new_meeting_form(self))

    def post(self):
        pass
