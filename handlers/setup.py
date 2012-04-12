from google.appengine.ext import db

import tornado.web

from handlers.base import BaseHandler
from models.kaigi import Kaigi
from forms.kaigi import KaigiForm

class SetupHandler(BaseHandler):
    def initialize(self, user_dao, kaigi_dao):
        self.user_dao = user_dao
        self.kaigi_dao = kaigi_dao

    def go_to_setup_form(self):
        self.render('setup.html', form=KaigiForm())

    @tornado.web.authenticated
    def get(self):
        self.go_to_setup_form()

    @tornado.web.authenticated
    def post(self):
        self.check_xsrf_cookie()
        form = KaigiForm(handler=self)
        if form.validate():
            kaigi = Kaigi(**form.data)
            self.user_dao.insert_admin(self.get_current_user())
            self.kaigi_dao.insert(kaigi)
            self.redirect('/')
        else:
            self.go_to_setup_form()
