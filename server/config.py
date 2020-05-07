#!/usr/bin/env python
#-*- coding:utf8 -*-
# 配置文件


import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # 调试模式
    DEBUG = False
    # 密钥
    SECRET_KEY = '1jjcd#23_dase1243'
    # 数据库连接
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
    # 每次请求结束后自动追踪数据库变动
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 安全配置
    CSRF_ENABLED = True


# 开发环境下配置
class DevelopConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://adrian:jx9X-HC?@localhost:3306/aesdb?charset=utf8'


# 产品环境下配置
class ProductConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:jx9X-HC?@localhost:3306/aesdb?charset=utf8'
