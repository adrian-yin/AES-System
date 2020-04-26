#!/usr/bin/env python
#-*- coding:utf8 -*-

from flask_restful import Resource
from app import auth
from app import db

from ..models.userModel import UserModel
from ..models.recordModel import RecordModel
from ..models.wrongCharModel import WrongCharModel
from ..models.verificationCodeModel import VerificationCodeModel

from flask import json, jsonify, request, abort, g

@auth.verify_token
def verify_token(token):
    user = UserModel.verify_auth_token(token)
    if not user:
        return False
    g.user = user
    return True

