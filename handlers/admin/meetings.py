import tornado.web

from handlers.base import BaseHandler
from decorators.user import admin
from models.meeting import Meeting
import forms.meeting

class NewMeetingHandler(BaseHandler):
    def initialize(self, user_dao, meeting_dao):
        self.user_dao = user_dao
        self.meeting_dao = meeting_dao

    def go_to_form(self, form=None):
        if form is None:
            form = forms.meeting.new_meeting_form(self)
        self.render('new_meeting.html', form=form)

    @admin
    def get(self):
        self.go_to_form()

    @admin
    def post(self):
        self.check_xsrf_cookie()
        form = forms.meeting.new_meeting_form(self)
        if form.validate():
            meeting = Meeting(**form.get_data())
            self.meeting_dao.insert(meeting)
            self.redirect('/dashboard')
        else:
            self.go_to_form(form)
