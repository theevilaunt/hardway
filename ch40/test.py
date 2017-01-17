import random
#import urllib
from urllib import request
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

for word in request.urlopen(WORD_URL).readlines():
	print(word.strip())
	WORDS.append(word.strip())

#print(WORDS)