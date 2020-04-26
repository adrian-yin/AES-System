#!/usr/bin/env python
#-*- coding:utf8 -*-
# 用户数据库模型


from . import *


class UserModel(db.Model, UserMixin):
    # 对应表格：users
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(128), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    name = db.Column(db.String(128))

    records = db.relationship('RecordModel', backref='user')

    def __init__(self, username, email, name):
        self.username = username
        self.email = email
        self.name = name

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    # 密码设置
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    # 密码验证
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username

    # 生成token
    def generate_auth_token(self, expiration=3600):
        s = Serializer(app.config['SECRET_KEY'], expiration)
        return s.dumps({'id':self.id}).decode("ascii")

    # 解析token，确认登陆用户的身份
    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None
        except BadSignature:
            return None
        user = UserModel.query.get(data['id'])
        return user

    # 信息打包成json
    def to_json(self):
        return jsonify(
            code=200,
            message="成功",
            id=self.id,
            username=self.username,
            email=self.email,
            name=self.name
        )

    # 通过用户名获取用户
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    # 通过邮箱获取用户
    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    # 新增用户
    def add_user(self):
        db.session.add(self)
        db.session.commit()

