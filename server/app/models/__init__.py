#!/usr/bin/env python
#-*- coding:utf8 -*-

from werkzeug.security import generate_password_hash, check_password_hash
# 生成令牌函数
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired
from flask_login import UserMixin
from .. import db, app
from flask import json, jsonify, request, abort, g

from .userModel import UserModel
from .recordModel import RecordModel
from .wrongCharModel import WrongCharModel
from .verificationCodeModel import VerificationCodeModel
