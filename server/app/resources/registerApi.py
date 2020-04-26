#!/usr/bin/env python
#-*- coding:utf8 -*-
# 注册接口

from . import *


class RegisterApi(Resource):

    def post(self):

        req = request.json
        if req is None:
            return jsonify(code=403, message="未收到参数")

        # 检查邮箱是否已注册
        user = UserModel.find_by_email(req.get("email"))
        if user:
            return jsonify(code=403, wrongType="email", message="邮箱已被注册")

        # 检查用户名是否已注册
        user = UserModel.find_by_username(req.get("username"))
        if user:
            return jsonify(code=403, wrongType="username", message="用户名已被注册")

        # 检查验证码是否正确
        vc = VerificationCodeModel.find_by_email(req.get("email"))
        if vc:
            if vc.code != req.get("verificationCode"):
                return jsonify(code=403, wrongType="verificationCode", message="验证码不正确")
        else:
            return jsonify(code=403, wrongType="verificationCode", message="验证码不存在")

        username = req.get('username')
        email = req.get('email')
        password = req.get('password')
        # 如果用户没有设置昵称，将用户名作为昵称
        if not req.get('name'):
            name = username
        else:
            name = req.get('name')
        u = UserModel(username=username, email=email, name=name)
        # 单独设置密码（调用加密函数）
        u.password = password

        u.add_user()

        return jsonify(code=200, message="注册成功！")