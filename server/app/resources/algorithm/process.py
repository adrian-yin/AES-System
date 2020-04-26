import re
import jieba
# from stanfordcorenlp import StanfordCoreNLP
import json
# import pycorrector

#ztz将correct，jufa的函数定义挪到了recordsApi文件之中

def cut_sent(para):
    para = re.sub('([。！？\!\?])([^”’\'\"])', r"\1\n\2", para)  # 单字符断句符
    para = re.sub('(\.{6})([^”’\'\"])', r"\1\n\2", para)  # 英文省略号
    para = re.sub('(\…{2})([^”’\'\"])', r"\1\n\2", para)  # 中文省略号
    para = re.sub('([。！？\.\!\?][”’\'\"])([^，。！？\.\!\,\?])', r'\1\n\2', para)
    # 如果双引号前有终止符，那么双引号才是句子的终点，把分句符\n放到双引号后，注意前面的几句都小心保留了双引号
    para = para.rstrip()  # 段尾如果有多余的\n就去掉它
    # 很多规则中会考虑分号;，但是这里我把它忽略不计，破折号、英文双引号等同样忽略，需要的再做些简单调整即可。
    return para.split('\n')

def cut_word(fenJu_WenZhang,ciBiao_Path):
    fenCi_WenZhang=[]
    jieba.load_userdict(ciBiao_Path)
    for juzi in fenJu_WenZhang:
        fenCi_JuZi=jieba.cut(juzi)
        fenCi_WenZhang.append(fenCi_JuZi)
        # for ci in fenCi_JuZi:
            # print(ci)
    return fenCi_WenZhang


# cut函数被改动了
def cut(articleContent):
    
    fenJu_WenZhang=[]
    paragragh_WenZhang=[]
    blank=''
    paragragh_WenZhang=[]

    paragragh_WenZhang=articleContent.split("\n")
    for juzi in cut_sent(articleContent):
        if(juzi.strip()==''):
            continue
        # print(juzi)
        fenJu_WenZhang.append(juzi)

    return fenJu_WenZhang,blank.join(fenJu_WenZhang),paragragh_WenZhang




def averagenum(num):
    nsum = 0
    for i in range(len(num)):
        nsum += num[i]
    if len(num) != 0:
        return nsum / len(num)
    else:
        return -1


def word(fenCi_WenZhang,dict_word_level_path):
    with open(dict_word_level_path, 'rb') as f:
        # for journal in f.readlines():
        #     journal=str(journal,'utf8')
        for line in f:
            line=str(line,'utf-8').strip()
            fi=json.loads(line)
    
    score=[]
    ci=[]
    number_sixlevel={}
    for sent in fenCi_WenZhang:
        for vocab in sent:
            ci.append(vocab)

            # if(vocab in fi):
            #     print(vocab+":"+str(fi[vocab])+";")
            # else:
            #     pass
            
    ci=set(ci)
    # blank=''
    # print(blank.join(ci))

    for vocab in ci:
        if vocab in fi:
            score.append(fi[vocab])
            if(fi[vocab] in number_sixlevel):
                number_sixlevel[fi[vocab]]+=1
            else:
                number_sixlevel[fi[vocab]]=1
    
    # if(score==[]):
    #     blank=''
    #     print(blank.join(sent))

    return averagenum(score),number_sixlevel


if __name__ == "__main__":
    #输入UTF8编码文章，输出词汇难度，句法难度，修改错别字
    fenJu_WenZhang=[]
    fenCi_WenZhang=[]
    # juFa_WenZhang=[]
    corrected_wenzhang=[]

    filePath="作文_卢.txt"
    stanfordPath=r"/root/standfordCoreNlp/stanford-corenlp-full-2018-10-05"
    dict_word_level_path=r"dict_word_level.json"
    ciBiao_Path=r"./扩充词表.txt"

    fenJu_WenZhang,wenzhang=cut(filePath)
    # 对文章进行分句

    fenCi_WenZhang=cut_word(fenJu_WenZhang,ciBiao_Path)
    # 对每一句话进行分词
    # 使用jieba，添加hsk词入新增词表

    word_score,fenbu=word(fenCi_WenZhang,dict_word_level_path)
    # 求词汇水平的打分，是对这篇文章之中不重复的词，找出其hsk难度，求平均
    # 并给出词汇难度的分布
    print("词汇打分："+str(word_score))

    juFa_Score=juFa(fenJu_WenZhang,stanfordPath)
    # 根据standfordCoreNlp的parse生成句法树
    # 根据句法树的高度给出打分
    print("句法打分："+str(juFa_Score))


    corrected_wenzhang=correct(fenJu_WenZhang)[0]
    huanhang="\n"
    print(huanhang.join(corrected_wenzhang))

    # corrected_sent, detail = pycorrector.correct(wenzhang)
    # print(corrected_sent)
    # print(detail)

