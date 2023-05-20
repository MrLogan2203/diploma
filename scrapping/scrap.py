import requests
from urllib.parse import urlparse, urljoin
import re
import requests
from bs4 import BeautifulSoup

intlinks = []
extlinks = []

def scrap(url, depth = 1):
    parsed_url = urlparse(url)
    if not parsed_url.scheme:
        url = 'https://' + url +'/'
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, "lxml")
    for bs_link in soup.find_all('a'):
        try:
            new_link = bs_link.get("href")
            if new_link.startswith("http"):
                extlinks.append(urljoin(url,new_link))
            else:
                if depth >=1:
                    new_url = urljoin(url, new_link)
                    if new_link.startswith('/') and new_url not in intlinks:
                        #print(new_url)
                        intlinks.append(new_url)
                        scrap(new_url,depth-1)
                    else:
                        continue
        except AttributeError:
            continue

def save(url):
	with open("./scrapping results/internal_"+url.replace(".","_")+".txt","a") as f:
		for link in intlinks:
			f.write(link+"\n")
	with open("./scrapping results/external_"+url.replace(".","_")+".txt","a") as f:
			for link in extlinks:
				f.write(link+"\n")
