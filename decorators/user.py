import functools
import tornado.web

from daos.user_dao import UserDAO

def approved(user_dao):
    def wrap(method):
        @tornado.web.authenticated
        @functools.wraps(method)
        def wrapper(self, *args, **kargs):
            google_user = self.get_current_user()
            user = user_dao.load(google_user)

            if user is None:
                return self.redirect("/")

            if not user.is_approved():
                return self.redirect(self.get_approve_pending_url())

            return method(self, *args, **kargs)
        return wrapper
    return wrap
