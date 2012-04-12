import functools
import tornado.web

from daos.user_dao import UserDAO

def user(method):
    @functools.wraps(method)
    def wrapper(self, *args, **kargs):

        def put_next_url(url):
            if "?" not in url:
                if urlparse.urlsplit(url).scheme:
                    next_url = self.request.full_url()
                else:
                    next_url = self.request.uri
                url += "?" + urllib.urlencode(dict(next=next_url))
            return url

        google_user = self.get_current_user()
        if not google_user:
            if self.request.method in ("GET", "HEAD"):
                complete_url = put_next_url(self.get_login_url())
                return self.redirect(complete_url)
            raise HTTPError(403)
            return 

        user = UserDAO().load(google_user)

        if user is None:
            return self.redirect(self.get_subscribe_url())

        if not user.is_approved():
            return self.redirect(self.get_approve_pending_url())

        return method(self, *args, **kargs)
    return wrapper
