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

    def should_get_user_email(self):
        email = "test@gmail.com"
        google_user = users.User(email=email)
        user = User(user=google_user)

        assert user.get_email() == email

    def should_verify_if_the_user_is_admin(self):
        google_user = users.User(email='test@gmail.com')

        pending = User(user=google_user, status='PENDING')
        admin = User(user=google_user, status='ADMIN')
        approved = User(user=google_user, status='APPROVED')
        declined = User(user=google_user, status='DECLINED')
        default = User(user=google_user)

        assert pending.is_admin() == False
        assert approved.is_admin() == False
        assert admin.is_admin() == True
        assert declined.is_admin() == False
        assert default.is_admin() == False
