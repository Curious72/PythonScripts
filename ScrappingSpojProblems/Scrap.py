from bs4 import BeautifulSoup
import urllib2
from pyquery import PyQuery as pq
import os
f=open("/home/coolsduy/try.txt","r") #path where try.txt file is saved
listofproblems=f.readlines()
f.close()
e=open("/home/coolsduy/trying/problems.txt","a") # file to which the scrapped problems are to be written
for y in listofproblems:
	path="http://www.spoj.com/problems/"+y[19:]
	r=urllib2.urlopen(path)
	html=r.read()
	doc=pq(html)
	j= doc("#problem-body").text()
	soup=BeautifulSoup(j)
	o=soup.get_text()
	e.write (o.encode('utf8'))
	e.write("\n\n\n\n\n\n\n")
e.close()
