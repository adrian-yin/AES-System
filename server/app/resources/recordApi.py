#!/usr/bin/env python
#-*- coding:utf8 -*-
# 单条记录接口（get：获取单条记录信息）

from . import *

class RecordApi(Resource):

    @auth.login_required
    def get(self, record_id):

        r = RecordModel.find_by_id(record_id)
        if r is None:
            return jsonify(code=403, message='参数无效')
        
        return r.to_json()
        