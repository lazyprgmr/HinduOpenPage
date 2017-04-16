import nltk
import nltk.tokenize
import nltk.corpus
import collections
import string
import collections
import sys
import urllib2
import heapq
import ReadHindu
import ScrapeHindu

class FrequencySummarizer:

	def __init__(self, min_cut=0.1, max_cut=0.9):
		self._min_cut = 0.1
		self._max_cut = 0.9
		self._stopwords = set(nltk.corpus.stopwords.words('english')+list(string.punctuation))
	
	def _compute_frequencies(self, word_sent):
		freq = collections.defaultdict(int)
		
		for sentence in word_sent:
			for word in sentence:
				if word not in self._stopwords:
					freq[word] += 1
				
		max_freq = float(max(freq.values()))	
		
		for word in freq.keys():
			freq[word] = freq[word]/max_freq
			if freq[word] > self._max_cut or freq[word] < self._min_cut:
				del freq[word]
		
		return freq
	
	def _summarize(self, text, n):
		sents = nltk.tokenize.sent_tokenize(text)  #creates a list of sentences
		
		if n <= len(sents):
			word_sent = [nltk.tokenize.word_tokenize(s.lower()) for s in sents]		#creates a list of lists of words in sentence
			self._freq = self._compute_frequencies(word_sent)
			rankings = collections.defaultdict(int)
			for i, sent in enumerate(word_sent):
				for word in sent:
					if word in self._freq:
						rankings[i] += self._freq[word]
					
			sents_idx = heapq.nlargest(n, rankings, key = rankings.get)
			return [sents[j] for j in sents_idx]
		else:
			print "Exiting because required summary size is greater than article size"
			sys.exit()
	
link_list, titles = ScrapeHindu.Scraper()

title=[]
st=""
c=0
for t in titles:
	for c in t:
		if c!='\n':
			st+=c	
	title.append(st.strip())
	st=""
#print title
for c, l in enumerate(link_list):
	text = ReadHindu.read_article(l.encode('ascii','ignore'))  #returns article in string format
	f = FrequencySummarizer()
	summary = f._summarize(text, 3)
	print "\n\n"
	print title[c], "---", l
	print "\n"
	print ''.join(summary)

