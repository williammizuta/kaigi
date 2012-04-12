import tornado.web
from google.appengine.api import users

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return users.get_current_user()

    def render_string(self, template_name, **kwargs):
        return tornado.web.RequestHandler.render_string(self, template_name, users=users, **kwargs)

    def get_login_url(self):
        return users.create_login_url(self.request.uri)

    def get_approve_pending_url(self):
        return "/pending"

    def get_subscribe_url(self):
        return "/subscribe"
