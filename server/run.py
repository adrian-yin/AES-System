#!/usr/bin/env python
#-*- coding:utf8 -*-
# 启动服务器

from app import app

if __name__ == '__main__':
    from werkzeug.contrib.fixers import ProxyFix
    app.wsgi_app = ProxyFix(app.wsgi_app)

    app.run()

