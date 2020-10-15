from bs4 import BeautifulSoup
import requests


source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

# print(soup.prettify())

#say we want all the videos
#so grab one videos' information and once that is successful we can modify it to loop through all the videos
article = soup.find('article')

#first print the html to help you navigate where you need to go
# print(article.prettify())

headline = article.h2.a.text
print(headline)

# summary = article.div.p.text
#the above and below both work, bottom uses the find method where you pass in a tag and a class or id
summary = article.find('div', class_='entry-content').p.text
print(summary)

#we want the video link---but it is embedded so we need to get the embedded link and parse the url to just give us the video id
#vid_src = article.find('iframe', class_='youtube-player')
#the above would give us:
#<iframe allowfullscreen="true" class="youtube-player" height="360" src="https://www.youtube.com/embed/z0gguhEmWiY?version=3&amp;rel=1&amp;fs=1&amp;autohide=2&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;wmode=transparent" style="border:0;" width="640"></iframe>

#However, we just want the link which has a key of['src'] ----just like a dictionary where we want the value of that attribute
vid_src = article.find('iframe', class_='youtube-player')['src']
print(vid_src)
#https://www.youtube.com/embed/z0gguhEmWiY?version=3&rel=1&fs=1&autohide=2&showsearch=0&showinfo=1&iv_load_policy=1&wmode=transparent

#now we have to parse this out for the id which we can see comes after a /, so lets split string based on /
# vid_id = vid_src.split('/')
# print(vid_id)

#once we do that we can see the id is the first part of the 4th index so we change it to
vid_id = vid_src.split('/')[4]
print(vid_id)
#z0gguhEmWiY?version=3&rel=1&fs=1&autohide=2&showsearch=0&showinfo=1&iv_load_policy=1&wmode=transparent

#now we have to split on the ?
vid_id2 = vid_id.split('?')[0]
print(vid_id2)

#now we format it as a youtube link
yt_link = f"https://youtube.com/watch?v={vid_id2}"
print(yt_link)