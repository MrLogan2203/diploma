# diploma
Diploma project for cybersecurity


## usage

``` bash
usage: diploma.py [-h] [-t <string>] [-s [<int>]] [-p [<str>]] [--scripts]

options:
  -h, --help   show this help message and exit
  -t <string>  provide a target host
  -s [<int>]   provide an integer value for scrapping depth. default = 1, only provided host is scanning
  -p [<str>]   provide the str range of ports to scan e.g. 1-500. Default is 1-65535, mention that it might be
               time consuming
  --scripts    use this argument to search for CGI and JS scripts on a target host
                                                                                       
```
