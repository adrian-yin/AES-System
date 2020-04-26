#!/usr/bin/env python
#-*- coding:utf8 -*-

from app.models import WrongCharModel

wc1 = WrongCharModel('王', 1)
wc1.add_wrongchar_record()
wc2 = WrongCharModel('王', 1)
wc2.add_wrongchar_record()
wc3 = WrongCharModel('李', 1)
wc3.add_wrongchar_record()
wc4 = WrongCharModel('王', 2)
wc4.add_wrongchar_record()
wc5 = WrongCharModel('王', 3)
wc5.add_wrongchar_record()
wc6 = WrongCharModel('赵', 3)
wc6.add_wrongchar_record()
wc7 = WrongCharModel('李', 2)
wc7.add_wrongchar_record()
wc8 = WrongCharModel('李', 2)
wc8.add_wrongchar_record()
wc9 = WrongCharModel('王', 5)
wc9.add_wrongchar_record()

