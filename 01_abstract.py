# -*- encoding: utf-8 -*-

import sqlite3
from DBInterface import createDB
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem.wordnet import WordNetLemmatizer
from unidecode import unidecode

todo={}
abstr={}


def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		pass
	try:
		import unicodedata
		unicodedata.numeric(s)
		return True
	except (TypeError, ValueError):
		pass

## ===== < EXTRACCION > ===== ##
#inst=createDB("TITLE")
#todo=inst.itera()
inst=createDB("ABSTRACT")
abstr=inst.itera()
inst.conn.close()
#print len(todo.keys())
#print len(abstr.keys())
## ===== < / EXTRACCION > ===== ##


## ===== < STOPWORDS > ===== ##
from SemanticProc import StopWords
make=StopWords()
make.DefaultStopwords("english")
make.CustomStopwords("stopwordsProfe.txt")
stopwords=make.stopwords.keys()
## ===== < / STOPWORDS > ===== ##

def isAbstract(txt):
	if len(txt)>700:
		lang=build.get_language(txt)
		if lang!="english":
			return None
	if "No abstract available" in txt:
		return None
	if len(txt)<9:
		return None
	if "No abstract provided" in txt:
		return None
	if is_number(txt):
		return None
	return True

#import csv
#c = csv.writer(open("abstracts.csv", "wb"),delimiter='\t')
#c.writerow(["id","semantic"])

## ===== < N-GRAMS > ===== ##
from SemanticProc import SemanticProcessing
build=SemanticProcessing()
for i in abstr:
#	print i
	conc=abstr[i]#abstract a conc
	if isAbstract(conc):
		raw=nltk.clean_html(conc)
		raw=unidecode(raw)
		tokenizer = RegexpTokenizer(r'\w+')
		tokens=tokenizer.tokenize(raw)
		try: text=nltk.Text(tokens)
		except: print i+": fail in nltk.Text(tokens)"
		words=[w.lower() for w in text]
		words = [token for token in words if token not in stopwords]
		if len(words)>0: 
#			c.writerow([i," ".join(words)])
#			if len(words)==10: break
			build.Monograms(i,words)
			build.Bigrams(i,words)
		else: 
			print "rien: "+i
	else: print "rien: "+i
### ===== < / N-GRAMS > ===== ##


## ===== < GUARDAR > ===== ##
A=build.FrecArray_monograms
build.save(A,"monograms")
B=build.FrecArray_bigrams
build.save(B,"bigrams")
## ===== < / GUARDAR > ===== ##

print "-------------------------------------------------"
