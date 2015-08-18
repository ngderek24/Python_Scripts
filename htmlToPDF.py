import httplib2
import pdfcrowd
from bs4 import BeautifulSoup, SoupStrainer

#to use this script, you must install httplib2, pdfcrowd, and BeautifulSoup4. They are all free and available online.
#to change the company interview sets, you have to change s, outputFile, and li.find(...) to the desired company name

http = httplib2.Http()
#website where we want to download interview sets from
s = 'http://www.geeksforgeeks.org/tag/Symantec'
gotten = []
i = 0

def getPage(page):
	#use urllib2 to download html content
	import urllib2
	source = urllib2.urlopen(page)
	return source.read()

def saveAsPDF(s):
	#use pdfcrowd API to convert html content into new pdf file
	try:
		global i
		client = pdfcrowd.Client("tincan24", "6a997126b31d5d8a25e468cf419ddbc2")
		outputFile = open('symantec' + str(i) + '.pdf', 'wb')
		i += 1
		page = getPage(s)
		client.convertHtml(page, outputFile)
		outputFile.close()
	except pdfcrowd.Error, why:
		print 'Failed: ', why

if s.find('http://www.geeksforgeeks.org/') == 0 and s.find('forums') < 0:
	#get initial webpage
	response, content = http.request(s)
	#parse all html content with link attribute
	print 'Downloading files...'
	for link in BeautifulSoup(content, "html.parser", parse_only = SoupStrainer('a')):
		if link.has_attr('href'):
			#get link
			li = link['href']
			#download and save all relevant interview sets
			if li.find('symantec') >= 0 and li.find('#') < 0 and li.find('tag') < 0 and li.find('forum') < 0 and li not in gotten:
				print 'saving ' + li
				gotten.append(li)
				saveAsPDF(li)

print 'Downloaded ' + `i` + ' files'
print 'Finished'			
