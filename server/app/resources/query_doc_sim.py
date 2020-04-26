#!/usr/bin/env python
#-*- coding:utf8 -*-

# Copyright (c) 2017, Baidu.com, Inc. All Rights Reserved
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import sys
sys.path.append('/var/www/aes/server/app/resources/Familia/python')
from familia_wrapper import InferenceEngineWrapper

def query_doc_sim(query, document):
    if sys.version_info < (3,0):
        input = raw_input

    model_dir = '/var/www/aes/server/app/resources/Familia/model/novel'
    conf_file = 'lda.conf'
    emb_file = 'novel_twe_lda.model'
    # 创建InferenceEngineWrapper对象
    inference_engine_wrapper = InferenceEngineWrapper(model_dir, conf_file, emb_file)
    # 输入短文本和长文本
    query = query.strip()
    doc = document.strip()
    query_seg = inference_engine_wrapper.tokenize(query)
    doc_seg = inference_engine_wrapper.tokenize(doc)
    distances = inference_engine_wrapper.cal_query_doc_similarity(query_seg, doc_seg)

    # LDA文本相似度
    # print(distances[0])
    # TWE文本相似度
    return distances[1]

