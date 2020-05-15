import jieba.posseg as psg
import jieba
import functools
import numpy as np
import math
from gensim import corpora, models
from gensim.models import KeyedVectors
tfidf_model = models.TfidfModel.load("tfidf.model")
LDA_model = models.LdaModel.load("LDA.model")
dictionary = corpora.Dictionary.load('dictionary.dict')
wordtopic_dic = np.load('wordtopic_dic.npy', allow_pickle=True).item()
#  排序函数，用于topK关键词的按值排序


def cmp(e1, e2):
    res = np.sign(e1[1] - e2[1])
    if res != 0:
        return res
    else:
        a = e1[0] + e2[0]
        b = e2[0] + e1[0]
        if a > b:
            return 1
        elif a == b:
            return 0
        else:
            return -1


def get_simword(word_list):
    sentcorpus = tfidf_model[dictionary.doc2bow(word_list)]
    senttopic = LDA_model[sentcorpus]
    # 余弦相似度计算

    def calsim(l1, l2):
        a, b, c = 0.0, 0.0, 0.0
        for t1, t2 in zip(l1, l2):
            x1 = t1[1]
            x2 = t2[1]
            a += x1 * x1
            b += x1 * x1
            c += x2 * x2
        sim = a / math.sqrt(b * c) if not (b * c) == 0.0 else 0.0
        return sim
    # 计算输入文本和每个词的主题分布相似度
    sim_dic = {}
    for k, v in wordtopic_dic.items():
        if k[:-2] not in word_list:
            continue
        sim = calsim(v, senttopic)
        sim_dic[k[:-2]] = sim
    topic_words = []
    for k, v in sorted(sim_dic.items(), key=functools.cmp_to_key(cmp), reverse=True)[:10]:
        topic_words.append(k)
        print(k + "/ ", end='')

    print()
    return topic_words


def similarity(vector1, vector2):
    up = 0.0
    for k, t1 in enumerate(vector1):
        for j, t2 in enumerate(vector2):
            if k == j:
                up = up + t1*t2
    sum1 = 0.0
    for t1 in vector1:
        sum1 = sum1+t1*t1
    sum2 = 0.0
    for t2 in vector2:
        sum2 = sum2+t2*t2
    down = math.sqrt(sum1)*math.sqrt(sum2)
    if down < 1e-9:
        return 0.0
    else:
        return up/down


def get_stopword_list():
    # 停用词表存储路径，每一行为一个词，按行读取进行加载
    # 进行编码转换确保匹配准确率
    stop_word_path = 'china_stop_word.txt'
    stopword_list = [sw.replace('\n', '')
                     for sw in open(stop_word_path).readlines()]
    return stopword_list

# 分词方法，调用结巴接口


def seg_to_list(sentence, pos=False):
    if not pos:
        # 不进行词性标注的分词方法
        seg_list = jieba.cut(sentence)
    else:
        # 进行词性标注的分词方法
        seg_list = psg.cut(sentence)
    return seg_list
# 去除干扰词


def word_filter(seg_list, pos=False):
    stopword_list = get_stopword_list()
    filter_list = []
    # 根据POS参数选择是否词性过滤
    # 不进行词性过滤，则将词性都标记为n，表示全部保留
    for seg in seg_list:
        if not pos:
            word = seg
            flag = 'n'
        else:
            word = seg.word
            flag = seg.flag
        if not flag.startswith('n'):
            continue
        # 过滤停用词表中的词，以及长度为<2的词
        if not word in stopword_list and len(word) > 1:
            filter_list.append(word)
    return filter_list


# if __name__ == '__main__':

def LDA(title, text):
    # title = "食品与饥饿"
    # text = '''人活在这世界上肯定要吃食物。跟别的生物一样只有吸收足够的营养，才
    # 能生活下去。现在我们面临着这样的一个难题，吃“绿色食品”和不挨饿哪个是第一位？
    # 我对此的观点不挨饿才是第一位。当然，吃受到化学污染的农作物对我们人体有害。可是
    # 我们想一想在非洲或在贫穷的国家挨饿的人们。如果我们走到那种地步的话，我们肯定会想
    # ，吃什么都行，只要有能吃的东西就行。吃食物是人能生活的基本要素。所以我们只顾自己
    # 的健康不顾别人的生命是不对的。最好的办法是，更多人不挨饿的基础上，我们要想尽一切办
    # 法去少用化肥和农药多生产农作物。比如，我们能用自然的顺理去实现这些办法。害虫或昆虫
    # 能影响农业的话，我们也能用一些以害虫或昆虫的生物来影响它们。这样的话，我们可以不挨饿
    # 也可以保护我们的健康。还有一个办法就是研究怎样才能在相等的土地上收更多的农作品。因为现
    # 在科学很发达，这样的办法，总有一天会实现的。最后，到实现上述的那些办法为止，我们只能维
    # 持现在的情况。可是我们一定要抱着希望，会有更好的
    # 未来，坚持研究，达到谁都不挨饿，谁都不用因为污染的农作物担心自己的健康的目标'''
    pos = True
    seg_list = seg_to_list(text, pos)
    filter_list = word_filter(seg_list, pos)
    topic_words = get_simword(filter_list)
    print(topic_words)
    FASTTEXTFILE = "selected.vecs"  # 把这个换成另外一个比较大的vecs
    FASTTEXT = KeyedVectors.load_word2vec_format(FASTTEXTFILE, limit=500000)
    title_words = word_filter(list(jieba.cut(title)))
    print(title_words)
    topic_words_sum = np.array(list(0 for i in range(300)), dtype="float64")
    title_words_sum = np.array(list(0 for i in range(300)), dtype="float64")
    for word in topic_words:
        try:
            topic_words_sum += np.array(FASTTEXT[word])
        except KeyError:
            # FASTTEXT = KeyedVectors.load_word2vec_format(
            #     FASTTEXTFILE, limit=500000)
            # title_words_sum += np.array(FASTTEXT[word])
            topic_words_sum += np.array(list(0 for i in range(300)),
                                        dtype="float64")
    for word in title_words:
        try:
            title_words_sum += np.array(FASTTEXT[word])
        except KeyError:  # 如果词不存在
            # FASTTEXTFILE=这边用来放那个更大的词向量集
            # FASTTEXT = KeyedVectors.load_word2vec_format(
            #     FASTTEXTFILE, limit=500000)
            # title_words_sum += np.array(FASTTEXT[word])
            title_words_sum += np.array(list(0 for i in range(300)),
                                        dtype="float64")
    LDA_similarity = similarity(topic_words_sum.tolist(), title_words_sum.tolist())
    print(LDA_similarity)
    return LDA_similarity
    
    # title_bow = dictionary.doc2bow(list(jieba.cut(title)))
    # title_lda = LDA_model[tfidf_model[title_bow]]  # title的主题分布,要先把它变成idf的值
    # print(title_lda)
    # print("\n")
    # topic_bow = dictionary.doc2bow(topic_words)
    # topic_lda = LDA_model[tfidf_model[topic_bow]]  # 文章主题词的主题分布
    # print(topic_lda)
    # print("\n")
    # print(similarity(topic_lda, title_lda))
