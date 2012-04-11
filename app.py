import os
import tornado.wsgi
import handlers.index

from daos.meeting_dao import MeetingDAO

# Constants
IS_DEV = os.environ['SERVER_SOFTWARE'].startswith('Dev')  # Development server

settings = dict(
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    template_path=os.path.join(os.path.dirname(__file__), 'templates'),
    xsrf_cookies=True,
    cookie_secret="asjidoh91239jasdasdasdasdasdkja8izxc21312sjdhsa/Vo=",
    )

application = tornado.wsgi.WSGIApplication([
    (r'/', handlers.index.IndexHandler, dict(meetings=MeetingDAO())),
    ], **settings)
