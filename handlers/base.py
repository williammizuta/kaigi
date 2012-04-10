import tornado.web
from google.appengine.api import users

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return users.get_current_user()

    def get_login_url(self):
        return users.create_login_url(self.request.uri)

    def render_string(self, template_name, **kwargs):
        return tornado.web.RequestHandler.render_string(self, template_name, users=users, **kwargs)
