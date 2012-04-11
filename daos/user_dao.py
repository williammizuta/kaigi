from google.appengine.ext import db

from models.user import User

class UserDAO:
	def insert_admin(self, google_user):
		admin = User(user=google_user, status = db.Category('ADMIN'))
		User.put(admin)

	def load(self, google_user):
		users = User.all()
		return users.filter("user = ", google_user).get()
