#!/usr/bin/env python
#-*- coding:utf8 -*-

#用户还没登录那么这个验证码怎么放在用户表里面呢

from . import *
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
import random

class ConfirmApi(Resource):

    def post(self):

        req = request.json
        if req is None:
            return jsonify(code=403, message="未收到参数")
        
        email = req.get('email')
        # 检查邮箱是否已注册
        user = UserModel.find_by_email(email)
        if user:
            return jsonify(code=403, wrongType="email", message="邮箱已被注册")

        confirm_num = random.randint(1000,9999)
        # 保存验证码到数据库
        vc = VerificationCodeModel.find_by_email(email)
        # 如果已存在清空原记录
        if vc:
            db.session.delete(vc)
            db.session.commit()
        vc = VerificationCodeModel(email, confirm_num)
        vc.add_verification_code()

        username = req.get('username')

        def _format_addr(s):  # 配置收件人和发件人在邮箱界面的表现形式
            name, addr = parseaddr(s)  # 解析分解出name和addr
            return formataddr((Header(name, 'utf-8').encode(), addr))  # 因为有中文，所以用header拜尼马乐意一下name再encode

        # 发送的用户名和第三方授权密码
        from_addr = "zwzdpfxt@163.com"
        password = "123zwzdpfxt"
        # 收件人邮箱
        to_addr = email
        # SMTP服务器的地址
        smtp_server = "smtp.163.com"

        # 配置在收件人邮箱界面的显示
        msg = MIMEText('hello, 验证码是：' + str(confirm_num), 'plain', 'utf-8')  # 配置发送邮件的信息和格式
        msg['From'] = _format_addr('作文自动评分系统 <%s>' % from_addr)  # 新增发件人信息到msg
        msg['To'] = _format_addr('%s <%s>' % (username, to_addr))  # 新增收件人信息到msg
        msg['Subject'] = Header('您的验证码', 'utf-8').encode()  # 新增主题信息

        # 配置stmp服务器
        server = smtplib.SMTP(smtp_server, 25)  # 新建了一个STMP服务器(自己的)，功能应该是STMP（MTA）上25号端口的功能（用来发送邮件 ）
        # 并连接的是163的STMP
        server.set_debuglevel(1)  # 所有的交互记录写到服务器
        server.login(from_addr, password)  # 登录服务器（校对一下是不是都是163）
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()
        return jsonify(code=200, message="验证码已发送！")
