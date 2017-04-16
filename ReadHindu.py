import urllib2
import bs4

def read_article(url):
	page = urllib2.urlopen(url).read().decode('utf8')
	soup = bs4.BeautifulSoup(page,"lxml")
	results = soup.find("p",{"class":"drop-caps"})
	article = results.getText().encode('ascii','ignore')
	nxt = results.findNextSiblings("p")
	for n in nxt:
		article += n.getText().encode('ascii','ignore')
	return article
