from google.appengine.ext import testbed
from daos.user_dao import UserDAO
from google.appengine.api import users
from models.user import User

class user_dao_test:
    def setup(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.user_dao = UserDAO()
        self.created_users = 0

    def teardown(self):
        self.testbed.deactivate()

    def generate_custom_email(self):
        custom_email = 'myemail'
        custom_email += str(self.created_users)
        self.created_users += 1
        custom_email += '@gmail.com'
        return custom_email

    def insert_user_with_status(self, status):
        google_user = users.User(email=self.generate_custom_email())
        self.user_dao.insert(google_user)
        my_user = self.user_dao.load(google_user)
        my_user.status = status
        my_user.put()
        return my_user

    def should_insert_an_user_as_admin(self):
        google_user = users.User(email='test@gmail.com')
        self.user_dao.insert_admin(google_user)

        loaded_user = self.user_dao.load(google_user)
        assert loaded_user.status == 'ADMIN'

    def should_verify_if_there_is_an_user(self):
        assert self.user_dao.has_no_user() == True

        new_user = users.User(email='test@gmail.com')
        self.user_dao.insert_admin(new_user)
        assert self.user_dao.has_no_user() == False

    def should_retrieve_users_pending_approval(self):
        self.insert_user_with_status('ADMIN')
        self.insert_user_with_status('APPROVED')
        self.insert_user_with_status('DECLINED')
        pending_approval = self.insert_user_with_status('PENDING')

        users_pending_approval = [u.user.email() for u in self.user_dao.list_pending_approval()]

        assert pending_approval.user.email() in users_pending_approval
