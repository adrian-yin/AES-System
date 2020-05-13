#!/usr/bin/env python
#-*- coding:utf8 -*-
# 用户错别字记录模型

from . import *

class WrongCharModel(db.Model):

    __tablename__ = "wrongchars"
    # 把html里的每个属性都存在数据库里面
    id = db.Column(db.Integer, primary_key = True)
    origin_text = db.Column(db.String(20), nullable = False, index = True)
    origin_text_html = db.Column(db.String(300), nullable = False, index = True)
    correct_text = db.Column(db.String(20), nullable = False, index = True)
    correct_text_html = db.Column(db.String(300), nullable = False, index = True)
    origin_start_index = db.Column(db.String(80), nullable = True, index = True)  # 不知道是什么类型，可以为null
    origin_end_index = db.Column(db.String(80), nullable = True, index = True)
    correct_start_index = db.Column(db.String(80), nullable = True, index = True)
    correct_end_index = db.Column(db.String(80), nullable = True, index = True)
    create_time = db.Column(db.String(50), nullable = False, index = True)
    update_time = db.Column(db.String(50), nullable = False, index = True)
    problem_type_zh = db.Column(db.String(50), nullable = False, index = True)
    problem_type_en = db.Column(db.String(50), nullable = False, index = True)
    paragraph_index = db.Column(db.String(30), nullable = False, index = True)
    sentence_index = db.Column(db.String(30), nullable = False, index = True)
    problem_status = db.Column(db.Integer, nullable = False, index = True)
    corpus_id = db.Column(db.Integer, nullable = False, index = True)
    token_array = db.Column(db.String(50), nullable = True, index = True)  # 不知道什么类型，可以为Null
    token_str = db.Column(db.String(200), nullable = False, index = True)
    token_strs = db.Column(db.String(500), nullable = False, index = True)
    record_id = db.Column(db.Integer, db.ForeignKey("records.id"), nullable = False)

    def __repr__(self):
        return '<WrongChar: %s>' % self.id

    def __init__(self, origin_text, origin_text_html, correct_text, correct_text_html, origin_start_index , origin_end_index , correct_start_index , correct_end_index , create_time
    , update_time , problem_type_zh , problem_type_en , paragraph_index , sentence_index , problem_status , corpus_id , token_array , token_str, token_strs
    , record_id):
        self.origin_text = origin_text
        self.origin_text_html = origin_text_html
        self.correct_text = correct_text
        self.correct_text_html = correct_text_html
        self.origin_start_index = origin_start_index
        self.origin_end_index = origin_end_index
        self.correct_start_index = correct_start_index
        self.correct_end_index = correct_end_index
        self.create_time = create_time
        self.update_time = update_time
        self.problem_type_zh = problem_type_zh
        self.problem_type_en = problem_type_en
        self.paragraph_index = paragraph_index
        self.sentence_index = sentence_index
        self.problem_status = problem_status
        self.corpus_id = corpus_id
        self.token_array = token_array
        self.token_str = token_str
        self.token_strs = token_strs

        self.record_id = record_id

    def add_wrongchar_record(self):
        db.session.add(self)
        db.session.commit()
