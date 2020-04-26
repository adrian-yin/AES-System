#!/usr/bin/env python
#-*- coding:utf8 -*-
# 验证码模型

from . import *
import datetime

class VerificationCodeModel(db.Model, UserMixin):
    # 对应表格：users
    __tablename__ = 'verification_codes'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, index=True)
    code = db.Column(db.String(10))
    # 验证码有效时间一天
    effective_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now() + datetime.timedelta(days=1))

    def __init__(self, email, code):
        self.email = email
        self.code = code

    # 通过邮箱获取记录
    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    # 新增记录
    def add_verification_code(self):
        db.session.add(self)
        db.session.commit()
