import requests
from urllib.parse import urlparse 
import re
import requests
from bs4 import BeautifulSoup

links = []

def scrap(url):
        parsed_url = urlparse(url)
        if not parsed_url.scheme:
                url = 'https://' + url
                       
        response = requests.get(url)
        html_content = response.text
        
        soup = BeautifulSoup(html_content, "html.parser")
        for link in soup.find_all('a', attrs ={'href': re.compile("/.*/$")}):
                link = link.get("href") 
                if 'http' in link:
                        continue
                else:
                        links.append(link)
        for link in links:
                print(url+link)
                
