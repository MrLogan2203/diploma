import requests
from urllib.parse import urlparse 
import re
import requests
from bs4 import BeautifulSoup
import colorama
from colorama import Fore

def Get_full_URL(url, link):
       if link.startswith('http://') or link.startswith('https://'):
           print(link)
       else:
           print(url+link)     

def Scan_CGI(url):
        try:
                parsed_url = urlparse(url)
                if not parsed_url.scheme:
                        url = 'https://' + url
                       
                response = requests.get(url)
                html_content = response.text
                
                
                soup = BeautifulSoup(html_content, "html.parser")
                cgi_urls = [link.get("href") for link in soup.find_all(href=re.compile(r"\.cgi$"))]
                
                if len(cgi_urls) == 0:
                        print(f"No CGI scripts found on {url}")
                else:
                        print(f"CGI scripts found on {url}: ")
                        for link in cgi_urls:
                                Get_full_URL(url, link)
                
        except requests.exceptions.RequestException as e:
                print(f"Error occured: {str(e)}")

def Scan_JS(url):
        try:
                parsed_url = urlparse(url)
                if not parsed_url.scheme:
                        url = 'https://' + url
                       
                response = requests.get(url)
                html_content = response.text
                
                
                soup = BeautifulSoup(html_content, "html.parser")
                
                js_urls = [link.get("src") for link in soup.find_all(src=re.compile(r"\.js$"))]
                
                if len(js_urls) == 0:
                        print(Fore.GREEN+f"No JS scripts found on {url}"+Fore.WHITE)
                else:
                        print(Fore.GREEN+ f"JS scripts found on {url}: "+Fore.WHITE)
                        for link in js_urls:
                                Get_full_URL(url, link)
                                
        except requests.exceptions.RequestException as e:
                print(f"Error occured: {str(e)}")
                
