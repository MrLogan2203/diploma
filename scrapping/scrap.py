import requests
from urllib.parse import urlparse, urljoin 
import re
import requests
from bs4 import BeautifulSoup

links = []

def scrap(url,depth =1):
        if depth == 0:
                return
        parsed_url = urlparse(url)
        if not parsed_url.scheme:
                url = 'https://' + url
                       
        response = requests.get(url)
        html_content = response.content
        #print(html_content)
        
        soup = BeautifulSoup(html_content, "html.parser")
        for link in soup.find_all('a'):
                try: 
                        link = link.get("href") 
                        if link.startswith("http"):
                                continue
                        else:
                                new_url = urljoin(url,link)
                                if new_url not in links: 
                                        print(new_url)
                                        links.append(new_url)
                                        scrap(new_url,depth -1)
                                else:
                                        continue
                except requests.exceptions.ConnectionError:
                        continue
        #for link in links:
                #print(url+link)
                
