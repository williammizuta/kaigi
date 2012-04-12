from google.appengine.ext import db

class User(db.Model):
    user = db.UserProperty(auto_current_user_add=True, required=True)
    status = db.CategoryProperty(default='PENDING', choices=['ADMIN', 'PENDING', 'APPROVED', 'DECLINED'], required=True)

    def is_approved(self):
        return self.status == 'APPROVED' or self.status == 'ADMIN'
