from google.appengine.ext import db

import tornado.web

from handlers.base import BaseHandler
from models.meeting import Meeting
from models.kaigi import Kaigi
from forms.kaigi import KaigiForm

class IndexHandler(BaseHandler):
    def initialize(self, user_dao, kaigi_dao):
        self.user_dao = user_dao
        self.kaigi_dao = kaigi_dao

    def go_to_setup_form(self):
        self.render('setup.html', form=KaigiForm(), xsrf_field=self.xsrf_form_html())

    @tornado.web.authenticated
    def get(self):
        if (self.user_dao.has_no_user()):
            self.go_to_setup_form()

    @tornado.web.authenticated
    def post(self):
        self.check_xsrf_cookie()
        form = KaigiForm(handler=self)
        if form.validate():
            self.user_dao.insert_admin(self.get_current_user())
            kaigi = Kaigi(name = form.name.data, description = form.description.data)
            self.kaigi_dao.insert(kaigi)
            return self.redirect('/')
        self.go_to_setup_form()
