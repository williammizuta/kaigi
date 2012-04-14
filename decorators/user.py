import functools
import tornado.web

from daos.user_dao import UserDAO

def approved(method):
    @tornado.web.authenticated
    @functools.wraps(method)
    def wrapper(self, *args, **kargs):
        google_user = self.get_current_user()
        user = self.user_dao.get_or_create(google_user)

        if not user.is_approved():
            return self.redirect(self.get_approve_pending_url())

        return method(self, *args, **kargs)
    return wrapper

def admin(method):
    @tornado.web.authenticated
    @functools.wraps(method)
    def wrapper(self, *args, **kargs):
        google_user = self.get_current_user()
        user = self.user_dao.load(google_user)

        if user is None:
            return self.redirect("/")

        if not user.is_admin():
            return self.send_error(404)

        return method(self, *args, **kargs)
    return wrapper
