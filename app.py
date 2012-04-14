import os

import tornado.wsgi
import tornado.locale

import handlers.setup
import handlers.home
import handlers.dashboard
import handlers.pending

from daos.user_dao import UserDAO
from daos.kaigi_dao import KaigiDAO

# Constants
IS_DEV = os.environ['SERVER_SOFTWARE'].startswith('Dev')  # Development server

settings = dict(
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    template_path=os.path.join(os.path.dirname(__file__), 'templates'),
    xsrf_cookies=True,
    cookie_secret="asjidoh91239jasdasdasdasdasdkja8izxc21312sjdhsa/Vo=",
    )

tornado.locale.load_translations(
    os.path.join(os.path.dirname(__file__), "translations"))

application = tornado.wsgi.WSGIApplication([
    (r'/', handlers.home.HomeHandler, dict(user_dao=UserDAO())),
    (r'/dashboard', handlers.dashboard.DashboardHandler, dict(user_dao=UserDAO())),
    (r'/setup', handlers.setup.SetupHandler, dict(user_dao=UserDAO(), kaigi_dao=KaigiDAO())),
    (r'/pending', handlers.pending.PendingHandler, dict(user_dao=UserDAO())),
    ], **settings)
