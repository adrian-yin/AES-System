#!/usr/bin/env python
#-*- coding:utf8 -*-
# 单条记录接口（get：获取单条记录信息）

from . import *

class RecordApi(Resource):

    @auth.login_required
    def get(self, record_id):

        record = RecordModel.find_by_id(record_id)
        if record is None:
            return jsonify(code=403, message='参数无效')

        with open('app/resources/correct_jsons/correct_' + str(record_id) + '.json', 'r') as f:
            articleComment = json.load(f)

        # problem_details_list  = WrongCharModel.query.filter_by(record_id = record.id).all()  # 每一行信息都作为List的一个元素
        # problem_detail_dict_list = []  # 当前record id 的所有 错词的dict 序列
        # for single in problem_details_list:
        #     problem_detail_dict = {}
        #     problem_detail_dict['id'] = single.id
        #     problem_detail_dict['origin_text'] = single.origin_text
        #     problem_detail_dict['origin_text_html'] = single.origin_start_index
        #     problem_detail_dict['correct_text'] = single.correct_text
        #     problem_detail_dict['correct_text_html'] = single.correct_text_html
        #     problem_detail_dict['origin_start_index'] = single.origin_start_index
        #     problem_detail_dict['origin_end_index'] = single.origin_end_index
        #     problem_detail_dict['correct_start_index'] = single.correct_start_index
        #     problem_detail_dict['correct_end_index'] = single.correct_end_index
        #     problem_detail_dict['create_time'] = single.create_time
        #     problem_detail_dict['update_time'] = single.update_time
        #     problem_detail_dict['problem_type_zh'] = single.problem_type_zh
        #     problem_detail_dict['problem_type_en'] = single.problem_type_en
        #     problem_detail_dict['paragraph_index'] = single.paragraph_index
        #     problem_detail_dict['sentence_index'] = single.sentence_index
        #     problem_detail_dict['problem_status'] = single.problem_status
        #     problem_detail_dict['corpus_id'] = single.corpus_id
        #     problem_detail_dict['token_array'] = single.token_array
        #     problem_detail_dict['token_str'] = single.token_str
        #     problem_detail_dict['token_strs'] = single.token_strs
        #     problem_detail_dict_list.append(problem_detail_dict)

        data = {
            "recordId": record.id,
            "commitTime": record.commit_time,
            "articleTitle": record.article_title,
            "articleContent": record.article_content,
            "totalScore": record.total_score,
            "vocabularyLevel": record.vocabulary_level,
            "titleRelativity": record.title_relativity,
            "sentenceDifficulty": record.sentence_difficulty,
            "hsk1": record.hsk1,
            "hsk2": record.hsk2,
            "hsk3": record.hsk3,
            "hsk4": record.hsk4,
            "hsk5": record.hsk5,
            "hsk6": record.hsk6,
            # "articleComment": record.article_comment, # origin_html
            # "problem_detail": problem_detail_dict_list
            "suggestion": json.loads(record.suggestion),
            "articleComment": articleComment
        }

        # 返回文章内容
        return jsonify(code = 200, message = "成功", data = data)
