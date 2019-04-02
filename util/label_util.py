from util import conf_util

conf = conf_util.get_default_config()

def get_label():
    with open(conf["corpus_path"], "r", encoding="utf-8") as f1:
        with open(conf["label_path"], "a", encoding="utf-8") as f2:
            content = f1.readlines()
            for line in content:
                line = line.split('\t')[1].strip()
                if line == 'False':
                    f2.write('0'+'\n')
                else:
                    f2.write('1'+'\n')
        print('label saved!')
                