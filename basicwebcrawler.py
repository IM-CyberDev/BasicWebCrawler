import requests
import re

global a = []
global url_starter = ""#change to your url here, searching only url with .com at the end, change it to what you want. Or include a pattern list
global url_domainname = None
global temp = re.search(r"\.([^ \.]+)\.com",url_starter)
if temp:
	url_domainname = temp.group(1)

def web_crawl(weburl):
	url = weburl
	page = requests.get(url)
	webpage = page.text
	xx = re.findall(r"href=\"([^ ]+)\"",webpage)
	if xx:
		s = "\n".join(xx)
		print (s)
	
	
	if xx == None:
		return
	a.append(url)
	
	for newp in xx:
		if "http" in newp:
			s = re.search(r"\.([^ \.]+)\.com",newp)
			if s.group(1) in url and newp not in a and s.group(1)==url_domainname:
				print newp
				web_crawl(newp)
		else:
			s = url+"/"+newp
			if s != url and ".." not in s:
				print s
				web_crawl(s)
				
	
	for newp in xx:
		if "http" in newp:
			s = re.search(r"\.([^ \.]+)\.com",newp)
			if s.group(1) in url and url!=newp and s.group(1)!=url_domainname:
				print newp
				web_crawl(newp)
		else:
			s = url+"/"+newp
			if s != url and ".." not in s:
				print s
				web_crawl(s)
		
	
	
	

web_crawl(url_starter)
