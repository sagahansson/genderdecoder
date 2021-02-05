import sys
import os
current_dir = os.getcwd()
sys.path.append(current_dir + "/genderdecoder/genderdecoder")

from assess import assess
from wordlists import feminine_coded_words
from wordlists import masculine_coded_words
