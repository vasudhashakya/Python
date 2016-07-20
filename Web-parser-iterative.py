import urllib
from BeautifulSoup import *

url = raw_input('Enter URL:')
position=raw_input('Enter Position:')
count=raw_input('Enter Iteration Count:')

url_array=[]

# Read the first url and copy all the links into an array
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tags= soup('a')
for tag in tags:
	url_array.append(tag.get('href',None))


# Iterate the url_array for the count indicated looking for the given position	
for i in range (1,int(count)):
	html=urllib.urlopen(url_array[int(position)-1]).read()
	soup = BeautifulSoup(html)
	tags=soup('a')
	url_array=[]
	for tag in tags:
		#print tag.get('href',None)
		url_array.append(tag.get('href',None))
		
print url_array[int(position)-1]
