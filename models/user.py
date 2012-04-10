from google.appengine.ext import db

class User(db.Model):
    user = db.UserProperty(required=True)
    status = db.CategoryProperty(default='PENDING', choices=['ADMIN', 'PENDING', 'APPROVED', 'DECLINED'], required=True)
