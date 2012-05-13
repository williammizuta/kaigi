import tornado.web
from google.appengine.api import users
from daos.kaigi_dao import KaigiDAO


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return users.get_current_user()

    def render_string(self, template_name, **kwargs):
        kaigi = KaigiDAO().get()
        return tornado.web.RequestHandler.render_string(self, template_name, kaigi=kaigi, **kwargs)

    def get_login_url(self):
        return users.create_login_url(self.request.uri)

    def get_approve_pending_url(self):
        return "/pending"
