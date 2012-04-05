import logging
import os

import tornado.web
import tornado.wsgi
from tornado.web import url

from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

import forms
import handlers.index

from daos.meeting_dao import MeetingDAO

# Constants
IS_DEV = os.environ['SERVER_SOFTWARE'].startswith('Dev')  # Development server

class Application(tornado.wsgi.WSGIApplication):
    def __init__(self):
        routes = [
                (r'/', handlers.index.IndexHandler, dict(meetings=MeetingDAO())),
                # TODO Put your handlers here
                ]
        settings = dict(
                static_path=os.path.join(os.path.dirname(__file__), "static"),
                template_path=os.path.join(os.path.dirname(__file__), 'templates'),
                xsrf_cookies=True,
                # TODO Change this cookie secret
                cookie_secret="asjidoh91239jasdasdasdasdasdkja8izxc21312sjdhsa/Vo=",
                )
        tornado.wsgi.WSGIApplication.__init__(self, routes, **settings)


def main():
    run_wsgi_app(Application())

if __name__ == '__main__':
    main()
