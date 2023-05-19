import requests 
from urllib.parse import urlparse 

def Headers_Search(url):

        parsed_url = urlparse(url)
        if not parsed_url.scheme:
            url = 'https://' + url

        response = requests.get(url)
        #print(response.text)
        headers = response.headers 
        desired_headers = ["Content-Type", "Server", "Strict-Transport-Security", "X-Frame-Options", "X-XSS-Protection", "X-Content-Type-Options", "Referrer-Policy"]

        for header in desired_headers:
                if header not in headers:
                        if header == "Strict-Transport-Security":
                                print(f"{header}: header not found. The lack of this header may cause the vulnerability for the MITM (man-in-the-middle) attack, which downgrades connection to HTTP")
                        elif header == "X-Frame-Options":
                                print(f"{header}: header not found. The lack of this header may cause the vulnerability for the clickjacking attack")
                        elif header == "X-XSS-Protection":
                                print(f"{header}: header not found. The lack of this header may cause the vulnerablity for XSS attack.")
                        elif header == "Referrer-Policy":
                                print(f"{header}: header not found. The lack of this header may cause the sensitive information leakage.")
                else:
                        print(f"{header}: {headers[header]}")
