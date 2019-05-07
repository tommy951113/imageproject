import jieba
import codecs
import jieba.posseg as pseg
from snownlp import SnowNLP

POI_ID = 'B2094650D46EABFE4493'
sentiment_list = []
with codecs.open(POI_ID + '.txt','r','utf-8') as f:
    for line in f:
        s = SnowNLP(line)
        sentiment_list.append(s.sentiments)

print(sentiment_list)
print(sum(sentiment_list)/len(sentiment_list))
        
# 就分析一下这句话，是积极还是消极，然后到这个地方看街景怎么样
# seg_list = jieba.cut("勺湖园，因湖像勺子一样而得名，平静的人湖水让人心中平静，这里是中途纳凉小憩的好去处。", cut_all=False)
# print("Default  Mode " + '/'.join(seg_list))
# words = pseg.cut('勺湖园，因湖像勺子一样而得名，平静的人湖水让人心中平静，这里是中途纳凉小憩的好去处。')
# for word, flag in words:
#     print('%s %s' % (word, flag))