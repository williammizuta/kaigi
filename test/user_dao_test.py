from google.appengine.ext import testbed
from daos.user_dao import UserDAO
from google.appengine.api import users

class user_dao_test:
    def setup(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()

    def teardown(self):
        self.testbed.deactivate()

    def should_insert_an_user_as_admin(self):
        google_user = users.User(email='teste@gmail.com')
        user_dao = UserDAO()
        user_dao.insert_admin(google_user)

        loaded_user = user_dao.load(google_user)
        assert loaded_user.status == 'ADMIN'

    def should_verify_if_there_is_an_user(self):
        user_dao = UserDAO()
        assert user_dao.has_no_user() == True

        new_user = users.User(email='test@gmail.com')
        user_dao.insert_admin(new_user)
        assert user_dao.has_no_user() == False
