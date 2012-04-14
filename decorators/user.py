import functools
import tornado.web

from daos.user_dao import UserDAO

def approved(method):
    @tornado.web.authenticated
    @functools.wraps(method)
    def wrapper(self, *args, **kargs):
        google_user = self.get_current_user()
        user = UserDAO().load(google_user)

        if user is None or not user.is_approved():
            return self.redirect(self.get_approve_pending_url())

        return method(self, *args, **kargs)
    return wrapper
