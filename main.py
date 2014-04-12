# -*- encoding: utf-8 -*-

import sqlite3
from DBInterface import createDB
import nltk
from nltk.tokenize import RegexpTokenizer
from unidecode import unidecode
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import FreqDist

todo={}
abstr={}

inst=createDB("TITLE")
todo=inst.itera()
inst=createDB("ABSTRACT")
abstr=inst.itera()
inst.conn.close()
#print len(todo.keys())
#print len(abstr.keys())


def getStopPepe(filename):
	d={}
	f = open(filename,"r")
	line = f.readline()
	while line:
		ID=line.replace("\n","")
		ID=ID.replace("\r","")
		d[ID]=1
		line = f.readline()
	return d


lmtzr = WordNetLemmatizer()

stopwords={}

nltkstopwords = nltk.corpus.stopwords.words('english')
for i in nltkstopwords:
	stopwords[i]=1

pepeStahp=getStopPepe("stopwordsProfe.txt")
for i in pepeStahp:
	stopwords[i]=1

stopwords=stopwords.keys()




FrecArray={}
for i in todo:
#	print i
	conc=todo[i]#titulo a conc
	if abstr.has_key(i):#si E abst, lo concatena
		conc=todo[i]+" "+abstr[i].replace("\n"," ")

	raw=nltk.clean_html(conc)
	raw=unidecode(raw)
	raw=raw.replace("e.g.","")
	raw=raw.replace("i.e.","")
	tokenizer = RegexpTokenizer(r'\w+')
	tokens=tokenizer.tokenize(raw)
	try: text=nltk.Text(tokens)
	except: print i+": fail in nltk.Text(tokens)"
	words=[w.lower() for w in text]
	words = [token for token in words if token not in stopwords]
	
	
	if len(words)>0: 
#		print i

#		# < monograms > #
#		words=[lmtzr.lemmatize(word) for word in words]
#		word_frequencies = FreqDist(words)
#		most_frequent = [word[0] for word in word_frequencies.items()]#[:10]]
#		for w in most_frequent:
#			if not FrecArray.has_key(w):
#				FrecArray[w]=[]
#			idpub_occs=i+"*"+`word_frequencies[w]`
#			FrecArray[w].append(idpub_occs)
##			print `word_frequencies[w]`+"\t: "+w
#		# < / monograms > #

		# < bigrams > #
		bgs = nltk.bigrams(words)
		word_frequencies = FreqDist(bgs)
		most_frequent = [word[0] for word in word_frequencies.items() if word_frequencies[word[0]]>1]
		for w in most_frequent:
			W=" ".join(w)
			if not FrecArray.has_key(W):
				FrecArray[W]=[]
			idpub_occs=i+"*"+`word_frequencies[w]`
			FrecArray[W].append(idpub_occs)
#			print `word_frequencies[w]`+"\t: "+" ".join(w)
		# < / bigrams > #

#		# < trigrams > # no, maybe not :c
#		trigs = nltk.trigrams(words)
#		word_frequencies = FreqDist(trigs)
#		most_frequent = [word[0] for word in word_frequencies.items()[:10] if word_frequencies[word[0]]>1]
#		if len(most_frequent)==0: print "rien"
#		for w in most_frequent:
#			print `word_frequencies[w]`+"\t: "+" ".join(w)
#		# < / trigrams > #

	else: 
		print "rien: "+i


import codecs
f = codecs.open("InvDict_.txt","w","utf-8")
for i in FrecArray:
	try: f.write(i+"("+";".join(FrecArray[i])+")\n")
	except: print "in FrecArray!!: "+i

f.close()
print "-------------------------------------------------"
