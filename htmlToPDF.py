import httplib2
import pdfcrowd
from bs4 import BeautifulSoup, SoupStrainer

http = httplib2.Http()
s = 'http://www.geeksforgeeks.org/tag/Symantec'
toGet = []
gotten = []
i = 0
toGet.append(s)

print len(toGet)
count = 0

def getPage(page):
	import urllib2
	source = urllib2.urlopen(page)
	return source.read()

def saveAsPDF(s):
	global i
	try:
		client = pdfcrowd.Client("tincan24", "6a997126b31d5d8a25e468cf419ddbc2")
		outputFile = open('symantec' + str(i) + '.pdf', 'wb')
		i += 1
		print 'opened file'
		page = getPage(s)
		client.convertHtml(page, outputFile)
		outputFile.close()
	except pdfcrowd.Error, why:
		print 'Failed: ', why

while len(toGet):
	#print toGet
	#print 'in while'
	#print p
	p = toGet.pop()
	if p.find('http://www.geeksforgeeks.org/') == 0 and p not in gotten and p.find('forums') < 0:
		#count += 1
		#print count
		gotten.append(p)
		response, content = http.request(p)
		for link in BeautifulSoup(content, "html.parser", parse_only = SoupStrainer('a')):
			print link
			if link.has_attr('href'):
				li = link['href']
				if p.find('http://www.geeksforgeeks.org/') == 0 and li not in gotten:
					saveAsPDF(li)
