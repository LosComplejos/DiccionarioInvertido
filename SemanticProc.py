
import nltk
from nltk import FreqDist
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import wordpunct_tokenize
from nltk.corpus import stopwords


class StopWords:
	def __init__(self):
		self.stopwords={}

	def CustomStopwords(self,filename):
		d={}
		f = open(filename,"r")
		line = f.readline()
		while line:
			ID=line.replace("\n","")
			ID=ID.replace("\r","")
			self.stopwords[ID]=1
			line = f.readline()

	def DefaultStopwords(self,language):
		nltkstopwords = nltk.corpus.stopwords.words(language)
		for i in nltkstopwords:
			self.stopwords[i]=1


class SemanticProcessing:

	def __init__(self):
		self.FrecArray_monograms={}
		self.FrecArray_bigrams={}

	from nltk.corpus import stopwords   # stopwords to detect language
	from nltk import wordpunct_tokenize # function to split up our words
	from sys import stdin   # how else should we get our input :)
	 
	def get_language_likelihood(self,input_text):
		"""Return a dictionary of languages and their likelihood of being the 
		natural language of the input text
		""" 
		input_text = input_text.lower()
		input_words = wordpunct_tokenize(input_text)
	 
		language_likelihood = {}
		total_matches = 0
		for language in stopwords._fileids:
			language_likelihood[language] = len(set(input_words) &
					set(stopwords.words(language)))
	 
		return language_likelihood
	 
	def get_language(self,input_text):
		"""Return the most likely language of the given text
		"""
		likelihoods = self.get_language_likelihood(input_text)
		return sorted(likelihoods, key=likelihoods.get, reverse=True)[0]

#	def detect_language(self,text):
#		ratios = self.calculate_languages_ratios(text)
#		most_rated_language = max(ratios, key=ratios.get)
#		return most_rated_language


#	def calculate_languages_ratios(self,text):
#		languages_ratios = {}
#		tokens = wordpunct_tokenize(text)
#		words = [word.lower() for word in tokens]
#		# Compute per language included in nltk number of unique stopwords appearing in analyzed text
#		for language in stopwords.fileids():
#			stopwords_set = set(stopwords.words(language))
#			words_set = set(words)
#			common_elements = words_set.intersection(stopwords_set)
#			languages_ratios[language] = len(common_elements) # language "score"
#		return languages_ratios

	def Monograms(self,i,words):
		lmtzr = WordNetLemmatizer()
		Frecs_MG=self.FrecArray_monograms
		# < monograms > #
		words=[lmtzr.lemmatize(word) for word in words]
		word_frequencies = FreqDist(words)
		most_frequent = [word[0] for word in word_frequencies.items()]#[:10]]
		for w in most_frequent:
			if not Frecs_MG.has_key(w):
				Frecs_MG[w]=[]
			idpub_occs=i+"*"+`word_frequencies[w]`
			Frecs_MG[w].append(idpub_occs)
		#	print `word_frequencies[w]`+"\t: "+w
		# < / monograms > #

	def Bigrams(self,i,words):
		Frecs_BG=self.FrecArray_bigrams
		# < bigrams > #
		bgs = nltk.bigrams(words)
		word_frequencies = FreqDist(bgs)
		most_frequent = [word[0] for word in word_frequencies.items()]
		for w in most_frequent:
			W=" ".join(w)
			if not Frecs_BG.has_key(W):
				Frecs_BG[W]=[]
			idpub_occs=i+"*"+`word_frequencies[w]`
			Frecs_BG[W].append(idpub_occs)
		#	print `word_frequencies[w]`+"\t: "+" ".join(w)
		# < / bigrams > #
	
	def save(self,A,monobi):
		import codecs
		f = codecs.open("InvDict_"+monobi+".txt","w","utf-8")
		for i in A:
			if not i.isdigit():
				final=[]
				B=A[i]
				if len(B)==1:
					for j in B:
						raw=j.split("*")
						cont=int(raw[1])
						if cont>1:
							final.append(j)
				else: final=B
			
				if len(final)!=0:
					try: f.write(i+"("+";".join(final)+")\n")
					except: print "in FrecArray_"+monobi+"!!: "+i
		f.close()
