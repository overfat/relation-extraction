from util import conf_util

conf = conf_util.get_default_config()

# count the number of the words in the txt, including drop the same words
L = []
with open(conf["shorten_corpus_path"], encoding='utf-8') as f:
    text = f.read()
    L = L + text.split()
print('一共有{}个词'.format(len(L)))
del_same_list = list(set(L))
print('去重后有{}个词'.format(len(del_same_list))) 

# 一共有63462个词
# 去重后有2573个词