# coding=utf-8
import re
import json
import requests
import stanza
import time
import LDA_final
from stanfordcorenlp import StanfordCoreNLP

juFa_Score = 0
corrected_wenzhang = []


def ssplit_tokenize(essay):
    print("Building a Chinese pipeline...")
    zh_nlp = stanza.Pipeline(
        'zh', processors='tokenize, pos, lemma, depparse', verbose=False, use_gpu=False)
    print("Chinese pipeline is OK...")

    essay_array = []
    essay = essay.split("\n")

    for paragraph in essay:
        if(paragraph.strip() != ""):
            essay_array.append(ssplit_tokenize_paragraph(zh_nlp, paragraph))

    return essay_array


def ssplit_tokenize_paragraph(zh_nlp, paragraph):
    paragraph_array = []
    zh_doc = zh_nlp(paragraph)

    for i, sent in enumerate(zh_doc.sentences):
        sentenceArray = []
        # print("[Sentence {}]".format(i+1))
        for word in sent.words:
            # print("{:12s}\t{:12s}\t{:6s}\t{:d}\t{:12s}".format(
            #     word.text, word.lemma, word.pos, word.head, word.deprel))
            sentenceArray.append(word.text)
        # print("")
        paragraph_array.append(sentenceArray)
    return paragraph_array


def openFile(path):
    blank = ''
    with open(path, 'r') as f:
        essay = blank.join(f.readlines())

    return essay


def averagenum(num):
    nsum = 0
    for i in range(len(num)):
        nsum += num[i]
    return nsum / len(num)


def juFa(fenJu_WenZhang, stanfordPath):
    juFa_WenZhang = []
    kuoHao_Stack = []

    nlp = StanfordCoreNLP(stanfordPath, lang="zh")
    print("Building a StanfordCoreNLP")

    for para in fenJu_WenZhang:
        for sent in para:
            sent = "".join(sent)
            shuGao = 0
            kuoHao_Stack = []
            tree = nlp.parse(sent)
            print(sent)
            # print(tree)

            for character in tree:
                # print(character)
                if(character == '('):
                    if(len(kuoHao_Stack) == shuGao):
                        shuGao += 1
                    kuoHao_Stack.append("1")
                elif(character == ')'):
                    kuoHao_Stack.pop()

            # print("树高为"+str(shuGao))
            juFa_WenZhang.append(shuGao)
        # avg(juFa_WenZhang)

    juFa_Score = averagenum(juFa_WenZhang)
    return juFa_Score


def word(fenCi_WenZhang, dict_word_level_path):
    with open(dict_word_level_path, 'rb') as f:
        # for journal in f.readlines():
        #     journal=str(journal,'utf8')
        for line in f:
            line = str(line, 'utf-8').strip()
            fi = json.loads(line)

    score = []
    ci = []
    number_sixlevel = {}

    for para in fenCi_WenZhang:
        for sent in para:
            ci = ci + sent

    for vocab in ci:
        if vocab in fi:
            score.append(fi[vocab])
            if(fi[vocab] in number_sixlevel):
                number_sixlevel[fi[vocab]] += 1
            else:
                number_sixlevel[fi[vocab]] = 1

    return averagenum(score), number_sixlevel, len(ci)


def correct_byWenXin(essay):
    headers = {
        "Accept": "pplication/json,text/plain,*/*",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"
    }

    data_write = {
        "content": essay
    }
    # print(essay)
    data_write = json.dumps(data_write)
    url_write = "http://202.112.194.61:8091/gec/write"
    r = requests.post(url=url_write, headers=headers, data=data_write)
    print(re.search('\d+', r.text))
    data_check = {
        "id": re.search('\d+', r.text).group(0)
    }
    data_check = json.dumps(data_check)
    url_check = "http://202.112.194.61:8091/gec/check"
    r = requests.post(url=url_check, headers=headers, data=data_check)
    result = r.json()
    # print(result["essay"]["origin_html"])

    return result["essay"]["origin"], result["essay"]["correct"], result["essay"]["problem_detail"], result["essay"]["origin_html"]


if __name__ == "__main__":
    # 输入UTF8编码文章，输出词汇难度，句法难度，修改错别字

    t1 = time.time()

    fenJu_WenZhang = []
    fenCi_WenZhang = []
    paragragh_WenZhang = []

    # juFa_WenZhang=[]
    corrected_wenzhang = []

    # filePath = "作文_卢.txt"
    filePath = "essay.txt"

    stanfordPath = r"C:\Users\dvzhang\Desktop\原\standfordCoreNlp\stanford-corenlp-full-2018-10-05\stanford-corenlp-full-2018-10-05"
    dict_word_level_path = r"dict_word_level.json"

    essay = openFile(filePath)
    essay = '''某市公布的有关在公共场所抽烟的罚款条例，无论是对个人健康还是对市容整洁都是一个福音
    。首先，正如众所周知，吸烟严重危害健康。在公众场所吸烟，不仅对吸烟者个人，而且对周围的公众的健
    康构成了危害。从法律角度讲，也可以说是一种对他人的侵权行为。其次，在公众场所吸烟，也会对城市美
    观和卫生造成恶劣的影响。有些人将烟蒂乱扔，特别是行走时的吸烟还有可能烫伤他人，严重时引起火灾。香
    烟并不是违禁商品，但是抽烟人的生活习惯、道德基准和世界观在某种程度上决定了吸烟行为对社会和公众的危
    害程度。如果把香烟作为个人解除疲劳的手段，在不影响他人的情况下，有节度地享用的话，本来这也是无可非
    议的人权。但是，很遗憾的是很多烟民没有这样的自制能力。既然如此，原本应用个人的公德心来控制的事情，就
    非得用罚款等强制性手段来解决。除了中国之外，也有很多国家采取罚款措施。虽然我们主观上不愿看到此等情形
    ，但从广义的结论上来看，强制手段
    能给社会公众带来一个健康和美观的环境的话，也算是一个迫不得已的措施吧。'''

    # 对文章进行分句
    fenCi_WenZhang = ssplit_tokenize(essay)

    print("运行时间")
    print(time.time()-t1)

    word_score, fenbu, totalWord_num = word(fenCi_WenZhang, dict_word_level_path)
    # # 求词汇水平的打分，是对这篇文章之中不重复的词，找出其hsk难度，求平均
    # # 并给出词汇难度的分布
    print("词汇打分："+str(word_score))

    print("运行时间")
    print(time.time()-t1)

    # # 获得改错
    # paragragh = "|"
    # origin, corrected, problem_detail, origin_html = correct_byWenXin(
    #     paragragh.join(essay.split("\n")))
    # huanhang = "\n"
    # print(origin_html)

    # print("错误个数")

    # # corrected = str(huanhang.join(corrected_wenzhang))
    # incorrect_num = len(origin_html.split("</span>")) - 1
    # print("错误个数" + str(incorrect_num))
    # print("错词率：" + str(incorrect_num / totalWord_num))

    # print("运行时间")
    # print(time.time()-t1)

    # 获得句法打分
    juFa_Score = juFa(fenCi_WenZhang, stanfordPath)
    print("句法打分："+str(juFa_Score))

    print("运行时间")
    print(time.time()-t1)

    title = "吸烟对个人健康和公众利益的影响"
    print(LDA_final.LDA(title, essay))

    print("运行时间")
    print(time.time()-t1)