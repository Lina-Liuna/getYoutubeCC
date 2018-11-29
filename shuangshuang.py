import requests
import urllib
import urllib.request
import time
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
url = "http://shuangchinese.com/galleries-page"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

# To download the whole data set, let's do a for loop through all a tags
#for i in range(26,len(soup.findAll('a'))+1): #'a' tags are for links
for i in range(18,35, 1): #'a' tags are for links
    print("i = " + str(i))
    one_a_tag = soup.findAll('a')[i]
    link = one_a_tag['href']
    download_url = 'http://shuangchinese.com'+ link
    #print(str(link))
    print("download url = " + str(download_url))
    newresponse = requests.get(download_url)
    newsoup = BeautifulSoup(newresponse.text, "html.parser")
    for j in range(2, len(newsoup.findAll('a'))):
        update_tag = newsoup.findAll('a')[j]
        update_link = update_tag['href']
        if 'http' and '.jpg' not in str(update_link):
            continue
        print("update_link = " + str(update_link))
        #print(str(update_link)[-6:])
        urllib.request.urlretrieve(str(update_link), "/Users/lina/Documents/temp/" + str(i-17) + str(update_link)[-6:])
        #update_url = 'http://shuangchinese.com'+ update_link
        #print("update_url = " + str(update_url) )
        #newurl = urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:])
    #print(newurl)
    #response = requests.get(download_url)
    #updatesoup = BeautifulSoup(response.text, "html.parser")
    #print(updatesoup.head.contents[6])
    #mystr = str(updatesoup.head.contents[6])
    #print("\n")
    #print(re.findall('"([^"]*)"', mystr)[0])
    print("\n")
    #print(updatesoup.prettify())
    #time.sleep(1) #pause the code for a sec
