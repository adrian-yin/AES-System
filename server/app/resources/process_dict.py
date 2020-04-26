from . import *
import json
file = open("xdhydcd_json_data.json", 'r', encoding='UTF-8')
datas = []
for data in file.readlines():  # read;ines是读取所有行并以列表的形式返回,读进来的时候是字符串，loads完变为字典
    dic = json.loads(data)
    datas.append(dic)
wrong_words = g.user.records.wrongchars
ans = []
for wrong_word in wrong_words:
    for data in datas:
        if wrong_word == data['word']:
            ans.append(data)
# 所有的错词及其解释都在ans数组里面
file.close()
