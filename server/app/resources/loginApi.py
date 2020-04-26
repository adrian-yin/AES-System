#!/usr/bin/env python
#-*- coding:utf8 -*-
# 登陆接口

from . import *


class LoginApi(Resource):

    def post(self):

        req = request.json
        if req is None:
            return jsonify(code=403, message="未接收到参数")

        user = UserModel.find_by_username(req.get("userid"))
        if not user:
            user = UserModel.find_by_email(req.get("userid"))

        if not user or not user.verify_password(req.get("password")):
            return jsonify(code=403, message="错误的用户名或密码")

        token = user.generate_auth_token()
        return jsonify(code=200, message="成功", token=token)

