#!/usr/bin/env python
#-*- coding:utf8 -*-
# 一定时间段内历史记录接口

from . import *

class HistoryApi(Resource):

    @auth.login_required
    def post(self):

        req = request.json
        if req is None:
            return jsonify(code=403, message="未接收到参数")

        records = RecordModel.find_by_time(req.get('startTime'), req.get('endTime'))

        if records == []:
            return jsonify(code=200, message="时间范围内无记录")

        wrongchars = {}

        records_data = []

        num = 1
        for record in records:
            
            records_data.append(
                {
                    'num': num,
                    'totalScore': record.total_score,
                    'vocabularyLevel': record.vocabulary_level
                }
            )
            num = num + 1

            # 将时间范围内每条记录对应的错别字计算入wrongchars中
            for wc in record.wrongchars:
                if wc.correct_text in wrongchars.keys():
                    wrongchars[wc.correct_text] = wrongchars[wc.correct_text] + 1
                else:
                    wrongchars[wc.correct_text] = 1

        # TODO: 这里生成建议、词汇量、词汇量建议
        suggestion = '随意的一些建议'
        vocabulary = 1250
        vocabulary_suggestion = '随意的一些词汇量建议'

        return jsonify(
            code=200,
            message="成功",
            records=records_data,
            wrongchars=wrongchars,
            suggestion=suggestion,
            vocabulary=vocabulary,
            vocabularySuggestion=vocabulary_suggestion
        )


    @auth.login_required
    def get(self):

        records = g.user.records

        if not records:
            return jsonify(code=200, message="该用户无评分记录")

        wrongchars = {}

        records_data = []

        num = 1
        for record in records:
            
            records_data.append(
                {
                    'num': num,
                    'totalScore': record.total_score,
                    'vocabularyLevel': record.vocabulary_level
                }
            )
            num = num + 1

            # 将时间范围内每条记录对应的错别字计算入wrongchars中
            for wc in record.wrongchars:
                if wc.correct_text in wrongchars.keys():
                    wrongchars[wc.correct_text] = wrongchars[wc.correct_text] + 1
                else:
                    wrongchars[wc.correct_text] = 1

        # TODO: 这里生成建议、词汇量、词汇量建议
        suggestion = '随意的一些建议'
        vocabulary = 1250
        vocabulary_suggestion = '随意的一些词汇量建议'

        return jsonify(
            code=200,
            message="成功",
            records=records_data,
            wrongchars=wrongchars,
            suggestion=suggestion,
            vocabulary=vocabulary,
            vocabularySuggestion=vocabulary_suggestion
        )
