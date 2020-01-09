import requests
import re

a = []
url_starter = ""#change to your url here, searching only urls with .com at the end, change it to what you want. Or include a pattern list
url_domainname = None
temp = re.search(r"\.([^ \.]+)\.com",url_starter)
if temp:
	url_domainname = temp.group(1)

def web_crawl(weburl):
	url = weburl
	page = requests.get(url)
	webpage = page.text
	newLinks = re.findall(r"href=\"([^ ]+)\"",webpage)
	if newLinks:
		s = "\n".join(newLinks)
		print (s)
	
	
	if newLinks == None:
		return
	a.append(url)
	
	for newp in newLinks:
		try:
			if "http" in newp:
				s = re.search(r"\.([^ \.]+)\.com",newp)
				if s.group(1) in url and newp not in a and s.group(1)==url_domainname and url!=newp:
					print (newp)
					web_crawl(newp)
			else:
				s = url+"/"+newp
				if s != url and ".." not in s:
					print (s)
					web_crawl(s)
		except:
			continue
	
	
web_crawl(url_starter)
