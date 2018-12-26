from datetime import datetime
from stack import db

class User(db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120),  index=True, unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default = "default.jpg")
    password_hash = db.Column(db.String(120), nullable=False)
    posts = db.relationship("Post", backref = "author", lazy="dynamic")

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"

class Post(db.Model):
    __tablename__ = "Posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user_id"), nullable=False)
   
    def __repr__(self):
        return f"User('{self.title}','{self.date_posted}')"
