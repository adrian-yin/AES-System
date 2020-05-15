# coding=utf-8
import re
import json
import requests
import stanza
import time
# import LDA_final
from stanfordcorenlp import StanfordCoreNLP
import pandas as pd
import codecs
import math

juFa_Score = 0
corrected_wenzhang = []


class wenmind_score:
    def __init__(self, stanfordPath, dict_word_level_path):

        t1 = time.time()

        self.stanfordPath = stanfordPath
        self.dict_word_level_path = dict_word_level_path

        print("Building a Chinese pipeline...")
        self.zh_nlp = stanza.Pipeline(
            'zh', processors='tokenize, pos, lemma, depparse', verbose=False, use_gpu=False)
        print("Chinese pipeline is OK...")

        print("运行时间")
        print(time.time()-t1)

        self.nlp = StanfordCoreNLP(self.stanfordPath, lang="zh")
        print("Building a StanfordCoreNLP")

        print(self.nlp.parse("我来自北京语言大学。"))

        print("运行时间")
        print(time.time()-t1)

    def ssplit_tokenize(self, essay):
        essay_array = []
        essay = essay.split("\n")

        for paragraph in essay:
            if(paragraph.strip() != ""):
                essay_array.append(
                    self.ssplit_tokenize_paragraph(paragraph))

        return essay_array

    def ssplit_tokenize_paragraph(self, paragraph):
        paragraph_array = []
        zh_doc = self.zh_nlp(paragraph)

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

    def openFile(self, path):
        blank = ''
        with open(path, 'r') as f:
            essay = blank.join(f.readlines())

        return essay

    def averagenum(self, num):
        nsum = 0
        for i in range(len(num)):
            nsum += num[i]
        return nsum / len(num)

    def juFa(self, fenJu_WenZhang):
        juFa_WenZhang = []
        conjunction_WenZhang = []
        len_WenZhang = []
        kuoHao_Stack = []

        for para in fenJu_WenZhang:
            for sent in para:
                len_WenZhang.append(len(sent))

                sent = "".join(sent)
                shuGao = 0
                kuoHao_Stack = []
                tree = self.nlp.parse(sent)
                print(sent)
                # print(tree)

                tree = tree.replace("PU )", '').replace("PU (", '')
                # 删除本身文段里的括号，避免干扰

                for character in tree:
                    # print(character)
                    if(character == '('):
                        if(len(kuoHao_Stack) == shuGao):
                            shuGao += 1
                        kuoHao_Stack.append("1")
                    elif(character == ')'):
                        kuoHao_Stack.pop()

                lianJie = len(tree.split("CC"))

                # print("树高："+str(shuGao))
                # print("连接词密度："+str(lianJie / len_WenZhang[-1]))
                # print("句长："+str(len_WenZhang[-1]))

                juFa_WenZhang.append(shuGao)
                conjunction_WenZhang.append(lianJie)

        juFa_Score = self.averagenum(juFa_WenZhang)
        conjunction_score = self.averagenum(conjunction_WenZhang)
        avg_len = self.averagenum(len_WenZhang)
        return juFa_Score, conjunction_score, avg_len

    def word(self, fenCi_WenZhang):
        with open(self.dict_word_level_path, 'rb') as f:
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

        return self.averagenum(score), number_sixlevel, len(ci)

    def correct_byWenXin(self, essay):
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


def getTitle(set):
    titles = [
        "一封辞职信",
        "学习汉语的苦与乐",
        "记我的父亲",
        "记对我影晌最大的一个人",
        "如何看待安乐死",
        "由“三个和尚没水喝”想到的",
        "如何解决代沟问题",
        "我的城市/乡村生活",
        "我选择朋友的标准",
        "如何看待妻子回家",
        "如何面对挫折",
        "我的童年",
        "关于用自然之声取代噪声的建议",
        "我对离婚的看法",
        "我第一次",
        "一封与给父母的信",
        "我的一个假期",
        "我学汉语是为了",
        "静音环境对人体的危害",
        "我最喜欢读的一本书",
        "口香糖与坏境卫生",
        "我对男女分班的看法",
        "绿色食品与饥饿",
        "谈有效阅读",
        "运动员收入",
        "吸烟对个人健康和公众利益的影响",
        "最理想的结交方式",
        "父母是孩子的第一任老师",
        "我看流行曲"
    ]
    return titles[set - 1]


if __name__ == "__main__":
    stanfordPath = r"C:\Users\dvzhang\Desktop\原\standfordCoreNlp\stanford-corenlp-full-2018-10-05\stanford-corenlp-full-2018-10-05"
    dict_word_level_path = r"dict_word_level.json"
    wenmind = wenmind_score(stanfordPath, dict_word_level_path)

    print("重新计时")

    t1 = time.time()
    fenJu_WenZhang = []
    fenCi_WenZhang = []
    paragragh_WenZhang = []

    # juFa_WenZhang=[]
    corrected_wenzhang = []

    # filePath = "作文_卢.txt"
    # filePath = "essay.txt"

    df = pd.read_csv(r'dev.tsv', delimiter="\t")
    essay_list = []
    essay_set_list = []
    score_list = []
    for line in df['essay']:
        essay = line.strip()
        essay_list.append(essay)
    for line in df['essay_set']:
        # essay = line.strip()
        essay_set_list.append(line)
    for line in df['domain1_score']:
        # essay = line.strip()
        score_list.append(line)

    results = []

    # for tem in range(len(essay)):
    for tem1 in range(200):
        tem = tem1 + 1500

        try:
            essay = essay_list[tem]
            # 对文章进行分句
            fenCi_WenZhang = wenmind.ssplit_tokenize(essay)

            print("运行时间")
            print(time.time()-t1)

            word_score, fenbu, totalWord_num = wenmind.word(
                fenCi_WenZhang)
            # # 求词汇水平的打分，是对这篇文章之中不重复的词，找出其hsk难度，求平均
            # # 并给出词汇难度的分布
            print("词汇裸分："+str(word_score))
            word_trueScore = math.pow(word_score / 6, 0.24) * 5
            print("词汇真实分："+str(word_trueScore))

            print("运行时间")
            print(time.time() - t1)

            # 获得改错
            paragragh = "|"
            origin, corrected, problem_detail, origin_html = wenmind.correct_byWenXin(
                paragragh.join(essay.split("\n")))
            huanhang = "\n"
            print(origin_html)
            print("错误个数")
            # corrected = str(huanhang.join(corrected_wenzhang))
            incorrect_num = len(origin_html.split("</span>")) - 1
            print("错误个数" + str(incorrect_num))
            incorrect_possibility = incorrect_num / totalWord_num
            print("错词率：" + str(incorrect_possibility))

            incorrect_trueScore = (
                1 - math.pow(incorrect_possibility, 0.33)) * 5
            print("错误真实分：" + str(incorrect_trueScore))

            print("运行时间")
            print(time.time() - t1)

            # 获得句法打分
            juFaTree_Score, conjunction_score, avg_len = wenmind.juFa(
                fenCi_WenZhang)
            print("句法树裸分："+str(juFaTree_Score))
            conjunction_score = conjunction_score / avg_len
            print("连接裸分："+str(conjunction_score))
            print("句长裸分："+str(avg_len))

            if(juFaTree_Score > 20):
                juFaTree_Score = 20
            if(avg_len > 28):
                avg_len = 28

            juFaTree_trueScore = math.pow(juFaTree_Score / 20, 0.42) * 5
            conjunction_trueScore = math.pow(conjunction_score, 0.17) * 5
            avg_truelen = math.pow(avg_len / 28, 0.73) * 5

            print("句法树真实分："+str(juFaTree_trueScore))
            print("连接真实分："+str(conjunction_trueScore))
            print("句长真实分："+str(avg_truelen))

            juFa_trueScore = (juFaTree_trueScore +
                              conjunction_trueScore + avg_truelen) / 3
            print("句法真实分："+str(juFa_trueScore))

            print("运行时间")
            print(time.time() - t1)

            title = getTitle(essay_set_list[tem])
            LDA_sim = LDA_final.LDA(title, essay)
            print(LDA_sim)

            print("运行时间")
            print(time.time() - t1)

            result = {
                "essay": essay_list[tem],
                "essay_set": essay_set_list[tem],
                "title": title,
                "score": score_list[tem],
                "word_score": word_score,
                "LDA_sim": LDA_sim,
                "incorrect_possibility": incorrect_possibility,
                "word_trueScore": word_trueScore,
                "juFa_trueScore": juFa_trueScore,
                "incorrect_trueScore": incorrect_trueScore,
                "LDA_trueSim": LDA_sim * 5,
            }

            results.append(result)
        except:
            print(str(tem1)+"出现问题")

    filename = codecs.open("journals1501-1700.json", "w", "utf-8")
    filename.write(json.dumps(results, ensure_ascii=False))
    filename.close()
