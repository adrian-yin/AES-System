#!/usr/bin/env python
#-*- coding:utf8 -*-
# 用户信息资源文件

from . import *

class UserApi(Resource):
    
    @auth.login_required
    def get(self):
        if g.user:
            return g.user.to_json()
        return jsonify(code=404, message="未找到用户")

