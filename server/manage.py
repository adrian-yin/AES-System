#!/usr/bin/env python
#-*- coding:utf8 -*-
# 数据库命令行管理应用

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app, db
from app.models import *

# 初始化 migrate
migrate = Migrate(app, db)

# 初始化管理器
manager = Manager(app)

# 添加 db 命令，并与 MigrateCommand 绑定
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
