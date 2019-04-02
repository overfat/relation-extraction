import os

from gensim.models import FastText

from util import conf_util

conf = conf_util.get_default_config()
model_path = conf["model_path"]


def convert_to_vector():
    if not os.path.exists(model_path):
        # 将语料库转化为fasttext需要的格式
        package = list()
        with open(conf["shorten_corpus_path"], "r",encoding="utf-8") as f:
            content = f.readlines()
            for sentence in content:
                # package相当于二维数组
                package.append(sentence.split())
        model = FastText(package,size=20,window=3,min_count=1,iter=10)
        model.save(model_path)

    print("fasttext saved")
        
    


