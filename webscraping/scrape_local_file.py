#https://www.youtube.com/watch?v=ng2o98k983k

#"beautifulsoup4" recommends the "lxml" parser
#could use the "html5lib" parser
#need "requests"  library
#all 4 programs need installed by default

from bs4 import BeautifulSoup
import requests

with open('/home/craig/Desktop/python_cookbook2/webscraping/simple.html', 'r') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
    #pass in your file and the parser

#prints all the html
# print(soup.prettify())

#prints the first title and only the text
# match = soup.title.text
# print(match)

#if you want specific divs (or whatever), you must pass in the second argument telling it what you want
#class is a key word in python so you must use class_, but id is just id
#if you leave the .text off it will bring back all the html
# match = soup.find('div', class_="footer").text
# print(match)
############################################################################################


#find the first article 
#first inspect the article to see what you want
# article = soup.find('div', class_='article')
# print(article)

#<div class="article">
# <h2><a href="article_1.html">Article 1 Headline</a></h2>
# <p>This is a summary of article 1</p>
# </div>

# #then you can dig deeper into the article to just find the headline
# headline = article.h2.a.text
# print(headline)

# #and you can dig deeper into the article to just find the summary
# summary = article.p.text
# print(summary)

#####################################################################################################
#now lets try to find all the articles----use findall, which returns a list of all tags that match
for article in soup.findAll('div', class_='article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)

    print()