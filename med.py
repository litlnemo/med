#!/usr/bin/env python

"""med.py: A script for searching the Middle English Dictionary.
   The script defaults to Boolean search with full "open" results.
"""

import re

from bs4 import BeautifulSoup
import requests


search_term = raw_input("What word would you like to search for? ")

url = "http://quod.lib.umich.edu/cgi/m/mec/med-idx?type=boolean&q1=" + search_term + "&rgn1=Anywhere&operator1=And&q2=&rgn2=Anywhere&operator2=And&q3=&rgn3=Anywhere&size=All"

# Get text of search results

r  = requests.get(url)
page_data = r.text
soup = BeautifulSoup(page_data)
count = 0

# Open file to write to, write HTML for top of page

file = open("medresults.html", "wb")
file.write("<html>" + "\n" + "<head><title>MED search results</title><base href=\"http://quod.lib.umich.edu\" /></head>" + "\n" + "<body>" + "\n")
file.write("<h1>MED search results for word \"" + str(search_term) + "\"</h1>" + "\n")
file.write("<ul>" + "\n" )

# find relevant links, build LIs with them

get_urls = soup.select('li > font > a')
if get_urls == []:
	
	the_word = soup.select("p > font > strong")
	
	if the_word == []:
		print "Error! No results."
		file.write("<li>" + "\n")
		file.write("Sorry, no results!" + "\n")
		file.write("</li>" + "\n")
		
	else:
		print "Single page result"
		permalink = soup.input["value"]
		print permalink
		file.write("<li>" + "\n")
		file.write("<a href=\"" + str(permalink) + "&egs=all&egdisplay=open\">" + str(the_word) + "</a>")
		file.write("</li>" + "\n")
		print "Added 1 to page"
	


for link in get_urls:
	file.write("<li>" + "\n")
	
	short_url = link.get('href')
	full_url = "http://quod.lib.umich.edu" + short_url + "&egs=all&egdisplay=open"
	
	link["href"] = full_url
	
	file.write(str(link))
	file.write("</li>" + "\n")
	print "Added " + str(count + 1) + " to page"
	count = count+ 1
	
#finish HTML and close 'er up!
	
file.write("</ul>" + "\n" + "</body>" + "\n" + "</html>" )
file.flush()
file.close()
