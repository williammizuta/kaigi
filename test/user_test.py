from models.user import User
from google.appengine.api import users

class user_test:
    def should_verify_if_an_user_is_approved_or_not(self):
        google_user = users.User(email='test@gmail.com')

        pending = User(user=google_user, status='PENDING')
        admin = User(user=google_user, status='ADMIN')
        approved = User(user=google_user, status='APPROVED')
        declined = User(user=google_user, status='DECLINED')
        default = User(user=google_user)

        assert pending.is_approved() == False
        assert admin.is_approved() == True
        assert approved.is_approved() == True
        assert declined.is_approved() == False
        assert default.is_approved() == False
