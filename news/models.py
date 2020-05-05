from news import db, login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    profile_image = db.Column(
        db.String(20), nullable=False, default='default_profile.png')
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    news_group = db.relationship('News', backref='author', lazy=True)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"UserName: {self.username}"


class News(db.Model):

    __tablename__ = 'news'

    users = db.relationship(User)
    comments = db.relationship(
        'Comment', backref='news', lazy=True, cascade="all,delete")
    users_likes = db.relationship(
        'Likes', backref='news', lazy=True, cascade="all,delete")

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    picture_link = db.Column(db.String(), nullable=False)
    link = db.Column(db.String(), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(140), nullable=False)
    text = db.Column(db.Text, nullable=False)
    likes = db.Column(db.Integer, nullable=False, default=0)

    def __init__(self, title, text, user_id, link, picture_link):
        self.title = title
        self.text = text
        self.user_id = user_id
        self.link = link
        self.picture_link = picture_link

    def __repr__(self):
        return f"News Id: {self.id} --- Date: {self.date} --- Title: {self.title}"


class Comment(db.Model):
    news_group = db.relationship(News)

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.Text, nullable=False)
    news_id = db.Column(db.Integer, db.ForeignKey('news.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    text = db.Column(db.Text, nullable=False)

    def __init__(self, text, news_id, user_name):
        self.text = text
        self.news_id = news_id
        self.user_name = user_name

    def __repr__(self):
        return f"Comment Id: {self.id} --- Date: {self.date} --- Text: {self.text}"


class Likes(db.Model):

    __tablename__ = 'likes'

    users = db.relationship(User)
    news_group = db.relationship(News)

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    news_id = db.Column(db.Integer, db.ForeignKey('news.id'), nullable=False)

    def __init__(self, news_id, user_id):
        self.news_id = news_id
        self.user_id = user_id
