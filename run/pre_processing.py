from util import xml_util
from util import shorten_util
from util import fasttext_util
from util import label_util


if __name__ == "__main__":
    xml_util.get_info()
    shorten_util.shorten()
    fasttext_util.convert_to_vector()
    label_util.get_label()
