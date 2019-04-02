import re

from bs4 import BeautifulSoup

from util import conf_util

conf = conf_util.get_default_config()

entity_dict = {}
sentence_dict = {}
total_entity_list = []

id_pat = re.compile(r'(.*)\.e')
char_offset_pat = re.compile(r'(.*)-(.*)')

def get_info():
    with open(conf["data_path"], "r", encoding="utf-8") as f_aimed:
        lines = f_aimed.readlines()

        with open(conf["corpus_path"], "a", encoding='utf-8') as f_corpus:
            for line in lines:
                soup = BeautifulSoup(line, 'lxml')
                
                if soup.sentence:
                    sentence_dict[soup.sentence['id']] = soup.sentence['text']

                if soup.entity:
                    entity_dict[soup.entity['id']] = soup.entity['charoffset']
                    # first = char_offset_pat.search(offset).group(1)
                    # second = char_offset_pat.search(offset).group(2)
                    # build the list
                    total_entity_list.append(soup.entity['text'])

                if soup.pair:
                    interaction = soup.pair['interaction']
                    e1_offset = entity_dict[soup.pair['e1']]
                    e2_offset = entity_dict[soup.pair['e2']]
                    e1_begin_pos = int(char_offset_pat.search(e1_offset).group(1))
                    e1_end_pos = int(char_offset_pat.search(e1_offset).group(2))
                    e2_begin_pos = int(char_offset_pat.search(e2_offset).group(1))
                    e2_end_pos = int(char_offset_pat.search(e2_offset).group(2))
                    sentenceID = id_pat.search(soup.pair['e1']).group(1)
                    sentence = sentence_dict[sentenceID]
                    #print(e1_begin_pos,e1_end_pos,e2_begin_pos,e2_end_pos)
                    # sentence = sentence.replace(sentence[e1_begin_pos:e1_end_pos+1],'entityone')
                    replace_sentence = sentence[0:e1_begin_pos] + ' entityone ' + sentence[e1_end_pos+1:e2_begin_pos]+' entitytwo '+sentence[e2_end_pos+1:len(sentence)]
                    for item in total_entity_list:
                        if item in replace_sentence and item != sentence[e1_begin_pos:e1_end_pos+1] and item != sentence[e2_begin_pos:e2_end_pos+1]:
                            replace_sentence = replace_sentence.replace(item,' otherprotein ')
        
                    replace_sentence = replace_sentence.replace(',','')
                    replace_sentence = replace_sentence.replace('.','')
                    replace_sentence = replace_sentence.replace('/','')
                    replace_sentence = replace_sentence.replace('-','')
                    replace_sentence = replace_sentence.replace('(','')
                    replace_sentence = replace_sentence.replace(')','')
                    replace_sentence = replace_sentence.replace(':','')
                    f_corpus.write(replace_sentence+'\t'+interaction+'\n')

        print('info file saved!')
