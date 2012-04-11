from daos.user_dao import UserDAO
from google.appengine.api import users

class user_dao_test():
    def should_insert_an_user_as_admin(self):
        google_user = users.User(email='teste@gmail.com')
        user_dao = UserDAO()
        user_dao.insert_admin(google_user)

        loaded_user = user_dao.load(google_user)
        assert loaded_user.status == 'ADMIN'