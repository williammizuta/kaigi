from google.appengine.ext import db

from models.user import User

class UserDAO:
    def insert(self, google_user):
        user = User(user=google_user)
        User.put(user)

    def insert_admin(self, google_user):
        admin = User(user=google_user, status = db.Category('ADMIN'))
        User.put(admin)

    def remove(self, google_user):
        self.load(google_user=google_user).delete()

    def load(self, google_user):
        users = User.all()
        return users.filter("user = ", google_user).get()

    def has_no_user(self):
        return User.all().count() == 0

    def list_pending_approval(self):
        return User.all().filter("status =", 'PENDING')

    def get_admin(self):
        return User.all().filter("status = ", db.Category('ADMIN')).get()
