#!/usr/bin/env python
#-*- coding:utf8 -*-

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_httpauth import HTTPTokenAuth
# 导入配置文件
from config import DevelopConfig
from config import ProductConfig
 
# 初始化应用实例
app = Flask(__name__)
 
# 添加配置信息
app.config.from_object(ProductConfig)

# 使应用支持跨域资源访问
CORS(app, supports_credentials=True)

# 创建api实例
api = Api(app)
 
# 初始化数据库
db = SQLAlchemy(app)

# 初始化auth认证
auth = HTTPTokenAuth(scheme="JWT")

# 导入各资源类
from .resources.userApi import UserApi
from .resources.loginApi import LoginApi
from .resources.registerApi import RegisterApi
from .resources.recordsApi import RecordsApi
from .resources.recordApi import RecordApi
from .resources.historyApi import HistoryApi
from .resources.confirmApi import ConfirmApi
 
# 绑定资源和URI
api.add_resource(UserApi, '/api/users', endpoint='user')
api.add_resource(LoginApi, '/api/login', endpoint='login')
api.add_resource(RegisterApi, '/api/register', endpoint='register')
api.add_resource(RecordsApi, '/api/records', endpoint='records')
api.add_resource(RecordApi, '/api/record/<int:record_id>', endpoint='record')
api.add_resource(HistoryApi, '/api/history', endpoint='history')
api.add_resource(ConfirmApi,'/api/confirm',endpoint='confirm')
