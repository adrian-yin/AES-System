#!/usr/bin/env python
#-*- coding:utf8 -*-
# 作文评分记录模型

from . import *
from datetime import datetime

class RecordModel(db.Model):

    # 对应表格records
    __tablename__ = 'records'

    id = db.Column(db.Integer, primary_key=True)
    commit_time = db.Column(db.DateTime, nullable=False, default=datetime.now, index=True)
    article_title = db.Column(db.String(100), nullable=False, default='')
    article_content = db.Column(db.String(5000), nullable=False, default='')
    total_score = db.Column(db.Float, nullable=False, default=0)
    vocabulary_level = db.Column(db.Float, nullable=False, default=0)
    title_relativity = db.Column(db.Float, nullable=False, default=0)
    sentence_difficulty = db.Column(db.Float, nullable=False, default=0)
    article_comment = db.Column(db.String(8000), default='')
    suggestion = db.Column(db.String(500), default='')
    # vocabulary_development = db.Column(db.String(500), default='')
    hsk1 = db.Column(db.Integer, nullable=False, default=0)
    hsk2 = db.Column(db.Integer, nullable=False, default=0)
    hsk3 = db.Column(db.Integer, nullable=False, default=0)
    hsk4 = db.Column(db.Integer, nullable=False, default=0)
    hsk5 = db.Column(db.Integer, nullable=False, default=0)
    hsk6 = db.Column(db.Integer, nullable=False, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    wrongchars = db.relationship('WrongCharModel', backref='record')

    def __repr__(self):
        return '<Record %s>' % self.id

    def __init__(self, article_title, article_content, total_score, vocabulary_level, title_relativity, sentence_difficulty, article_comment, suggestion, hsk1, hsk2, hsk3, hsk4, hsk5, hsk6, user_id):
        self.article_title = article_title
        self.article_content = article_content
        self.total_score = total_score
        self.vocabulary_level = vocabulary_level
        self.title_relativity = title_relativity
        self.sentence_difficulty = sentence_difficulty
        self.article_comment = article_comment
        self.suggestion = suggestion
        # self.vocabulary_development = vocabulary_development
        self.hsk1 = hsk1
        self.hsk2 = hsk2
        self.hsk3 = hsk3
        self.hsk4 = hsk4
        self.hsk5 = hsk5
        self.hsk6 = hsk6
        self.user_id = user_id

    def add_record(self):
        db.session.add(self)
        db.session.commit()

    def to_json(self):
        return jsonify(
            code=200,
            message="成功",
            recordId=self.id,
            commitTime=self.commit_time,
            articleTitle=self.article_title,
            articleContent=self.article_content,
            totalScore=self.total_score,
            vocabularyLevel=self.vocabulary_level,
            titleRelativity = self.title_relativity,
            sentenceDifficulty=self.sentence_difficulty,
            articleComment=self.article_comment,
            suggestion=self.suggestion,
            # vocabularyDevelopment=self.vocabulary_development,
            hsk1=self.hsk1,
            hsk2=self.hsk2,
            hsk3=self.hsk3,
            hsk4=self.hsk4,
            hsk5=self.hsk5,
            hsk6=self.hsk6
        )

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    # 找到当前用户时间范围内记录
    @classmethod
    def find_by_time(cls, start_time, end_time):
        return db.session.query(cls).filter(cls.user_id==g.user.id).filter(cls.commit_time.between(start_time, end_time)).all()

