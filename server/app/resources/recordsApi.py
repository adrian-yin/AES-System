# !/usr/bin/env python
# -*- coding:utf8 -*-
# 记录接口（post：新增记录，get：获取用户记录信息）

from . import *
import app.resources.algorithm.process as al
# from app.resources.algorithm.process import *
import requests
from app.resources.algorithm.process import *

import json

# 临时使用随机数生成成绩
import random
import _thread
import time
import threading

# import pycorrector
# from stanfordcorenlp import StanfordCoreNLP
import jieba
import re


newjuFa_Score = 0
corrected_wenzhang = []


def juFa(fenJu_WenZhang, stanfordPath):

    juFa_WenZhang = []
    kuoHao_Stack = []

    nlp = StanfordCoreNLP(stanfordPath, lang="zh")
    for juZi in fenJu_WenZhang:
        shuGao = 0
        kuoHao_Stack = []
        # print(nlp.parse(juZi))
        # print(juZi)
        try:
            for character in nlp.parse(juZi):
                # print(character)
                if(character == '('):
                    if(len(kuoHao_Stack) == shuGao):
                        shuGao += 1
                    kuoHao_Stack.append("1")
                elif(character == ')'):
                    kuoHao_Stack.pop()
        except:
            # print(juZi)
            break
        # print(shuGao)
        juFa_WenZhang.append(shuGao)
    # avg(juFa_WenZhang)

    newjuFa_Score = averagenum(juFa_WenZhang)  # ztz


# def correct(fenJu_WenZhang):
#     corrected_wenzhang = []
#     wrong_words = []
#     original_wenzhang = []
# 
#     # zhy
#     for sent in fenJu_WenZhang:
#         corrected_sent, detail = pycorrector.correct(sent)
#         # print(corrected_sent)
#         corrected_wenzhang.append(corrected_sent)
#         temp_list = list(corrected_sent)# 把正确的句子先变成list
#         for wrong_word in detail:
#             wrong_words.append(wrong_word)
#             temp_list[wrong_word[2]:wrong_word[3]] = '*'+wrong_word[0]+'*'# 在错词的两边添加了标记“*”
#         original_sent = "".join(temp_list)
#         original_wenzhang.append(original_sent)
# 
# 
#         # wrong_words.append(detail)# detail 是一个[[], [], []]
#     corrected_wenzhang = corrected_wenzhang, wrong_words, original_wenzhang# ztz


def correct_byWenXin(essay):
    
    headers = {
        "Accept":"pplication/json, text/plain, */*", 
        "Accept-Encoding":"gzip, deflate", 
        "Accept-Language":"zh-CN, zh;q = 0.9", 
        "Content-Type":"application/x-www-form-urlencoded;charset = UTF-8"
    }
    
    data_write = {
        "content":essay
    }
    # print(essay)
    data_write = json.dumps(data_write)
    url_write = "http://202.112.194.61:8091/gec/write"
    r = requests.post(url=url_write, headers=headers, data=data_write)
    # print(re.search('\d+', r.text))
    data_check = {
        "id":re.search('\d+', r.text).group(0)
    }
    data_check = json.dumps(data_check)
    url_check = "http://202.112.194.61:8091/gec/check"
    r = requests.post(url=url_check, headers=headers, data=data_check)
    result = r.json()
    return result, result["essay"]["origin"], result["essay"]["correct"], result["essay"]["problem_detail"], result["essay"]["origin_html"]


class RecordsApi(Resource):

    @auth.login_required
    def post(self):

        req = request.json
        if req is None:
            return jsonify(code=403, message="未接收到参数")

        # TODO： 这里调用计算函数
        articleTitle = req.get("title")
        articleContent = req.get("article")# 拿到数据

# ******************************ztz 添加的代码**************************************************
        # 输入UTF8编码文章，输出词汇难度，句法难度，修改错别字
        fenJu_WenZhang = []
        fenCi_WenZhang = []
        # juFa_WenZhang = []
        corrected_wenzhang = []

        ciBiao_Path = r"app/resources/algorithm/hsk_word.txt"
        filePath = r"app/resources/algorithm/作文_卢.txt"
        # stanfordPath = r"/root/stanfordCoreNlp/stanford-corenlp-full-2018-10-05"
        dict_word_level_path = r"app/resources/algorithm/dict_word_level.json"
        import sys

        # 对文章进行分句
        fenJu_WenZhang, wenzhang, paragragh_WenZhang = al.cut(articleContent)

        fenCi_WenZhang = al.cut_word(fenJu_WenZhang, ciBiao_Path)
        # 对每一句话进行分词
        # 使用jieba，添加hsk词入新增词表
        word_score, fenbu = al.word(fenCi_WenZhang, dict_word_level_path)
        # 求词汇水平的打分，是对这篇文章之中不重复的词，找出其hsk难度，求平均
        # 并给出词汇难度的分布
        # print("词汇打分："+str(word_score))

        # juFa_Score = al.juFa(fenJu_WenZhang, stanfordPath)
        # 根据standfordCoreNlp的parse生成句法树
        # 根据句法树的高度给出打分
        # print("句法打分："+str(juFa_Score))
        juFa_Score = random.random() * 5
        import sys

        # womendewenzhang = al.correct(fenJu_WenZhang)

        paragragh = "|"
        correct_result_json, origin, corrected, problem_detail, origin_html = correct_byWenXin(paragragh.join(paragragh_WenZhang))
        wrong_words = []
        for word in problem_detail:
            origin_text = word['origin_text']
            origin_text_html = word['origin_text_html']
            correct_text = word['correct_text']
            correct_text_html = word['correct_text_html']
            origin_start_index = word['origin_start_index']
            origin_end_index = word['origin_end_index']
            correct_start_index = word['correct_start_index']
            correct_end_index = word['correct_end_index']
            create_time = word['create_time']
            update_time = word['update_time']
            problem_type_zh = word['problem_type_zh']
            problem_type_en = word['problem_type_en']
            paragraph_index = word['paragraph_index']
            sentence_index = word['sentence_index']
            problem_status = word['problem_status']
            corpus_id = word['corpus_id']
            token_array = word['token_array']
            token_str = word['token_str']
            token_strs = word['token_strs']
            wrong_words.append(origin_text)
            # print("3")

# ***************************************************************************************************************
        # 查字典
        file = open("app/resources/xdhydcd_json_data.json", 'r', encoding='UTF-8')
        new_dict = {}  # {"你好"：{"pinyin":"nihao", "main":[{}..]}}
        for data in file.readlines():
            dic = json.loads(data)
            if not new_dict.get(dic['word']):
                new_dict[dic['word']] = {}
                new_dict[dic['word']]['main'] = dic['main']
                new_dict[dic['word']]['pinyin'] = dic['pinyin']
        file.close()
        suggestion = {}  # dict includes dicts
        for wrong_word in wrong_words:
            if not new_dict.get(wrong_word):
                continue
            suggestion[wrong_word] = new_dict[wrong_word]
        suggestion = json.dumps(suggestion)

# *******************************************************************************************************************
        # 计算TWE文本相似度（主题得分）
        # from app.resources.query_doc_sim import query_doc_sim
        # similary = query_doc_sim(articleTitle, articleContent)
        similary = random.random() * 5
        # print("reach")
# *******************************************************************************************************************

        # 输出到页面上
        totalScore = round(random.random() * 50 + 50, 1)
        vocabularyLevel = round(word_score, 1)
        titleRelativity = round(similary, 1)
        sentenceDifficulty =  round(juFa_Score, 1)
        articleComment  = origin_html
        # articleComment = huanhang.join(original_wenzhang)# 带有标记的原文章放到原文点评（zhy）
        # suggestion = "先草率地随意留个提升建议"
        # vocabularyDevelopment = str(ans)
        hsk1 = random.random() * 15
        hsk2 = random.random() * 15
        hsk3 = random.random() * 15
        hsk4 = random.random() * 15
        hsk5 = random.random() * 15
        hsk6 = random.random() * 15
        r = RecordModel(articleTitle, articleContent, totalScore, vocabularyLevel, titleRelativity, sentenceDifficulty, articleComment, suggestion, hsk1, hsk2, hsk3, hsk4, hsk5, hsk6, g.user.id)
        r.add_record()
            
        for word in problem_detail:
            origin_text = word['origin_text']
            origin_text_html = word['origin_text_html']
            correct_text = word['correct_text']
            correct_text_html = word['correct_text_html']
            origin_start_index = word['origin_start_index']
            origin_end_index = word['origin_end_index']
            correct_start_index = word['correct_start_index']
            correct_end_index = word['correct_end_index']
            create_time = word['create_time']
            update_time = word['update_time']
            problem_type_zh = word['problem_type_zh']
            problem_type_en = word['problem_type_en']
            paragraph_index = word['paragraph_index']
            sentence_index = word['sentence_index']
            problem_status = word['problem_status']
            corpus_id = word['corpus_id']
            token_array = word['token_array']
            token_str = word['token_str']
            token_strs = word['token_strs']
            problem_detail_data = WrongCharModel(origin_text, origin_text_html, correct_text, correct_text_html, origin_start_index, origin_end_index, correct_start_index, correct_end_index, create_time, update_time, problem_type_zh, problem_type_en, paragraph_index, sentence_index, problem_status, corpus_id, token_array, token_str, token_strs, r.id)   # 这边要装此次的record id, 但是不知道为什么g.user.id不行（zhy）
            problem_detail_data.add_wrongchar_record()

        # 将correct结果的json存为文件
        # 以 correct_record的id 命名
        with open('app/resources/correct_jsons/correct_' + str(r.id) + '.json', 'w') as f:
            json.dump(correct_result_json, f)
        # print(correct_result_json)

        return jsonify(code = 200, message = "成功", recordId = r.id)

    @auth.login_required
    def get(self):

        records = g.user.records
        if records is None:
            return jsonify(code = 200, message = "该用户无评分记录")

        data = []

        for record in records:
            data.append(
                {
                "recordId": record.id,
                "commitTime": record.commit_time,
                "articleTitle": record.article_title,
                "articleContent": record.article_content,
                "totalScore": record.total_score
                }
            )
        # 返回文章内容
        return jsonify(code = 200, message = "成功", records = data)
