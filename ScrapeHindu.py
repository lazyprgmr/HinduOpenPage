import bs4
import urllib2
import re

def Scraper():
	lst = []
	title = []
	page = urllib2.urlopen("http://www.thehindu.com/opinion/open-page/").read().decode('utf8')
	soup = bs4.BeautifulSoup(page,"lxml")
	for c, link in  enumerate(soup.findAll("a",{"href":re.compile("^http://www.thehindu.com/opinion/open-page/.*\.ece$")})):
		if c==3 or c==4 or c==5 or c==7:
			lst.append(link.get('href'))
			title.append(link.text.encode('ascii','ignore'))		
	return lst, title
