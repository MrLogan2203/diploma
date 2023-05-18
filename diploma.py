import sys, getopt
from port_scanner import Scan_Port
from shodan_test import Scan_Inf
from scrapping.scripts_search import Scan_CGI, Scan_JS
from scrapping.scrap import scrap

def main(argv):
        host = ''
        try:
                opts,args = getopt.getopt(argv,"ht:",["host="])
        except getopt.GetoptError:
                print ('diploma.py -t <host name/IP>')
                sys.exit(2)
        for opt, arg in opts:
                if opt == '-h':
                        print ('diploma.py -t <host name/IP>')
                        sys.exit()
                elif opt in ("-t", "--target"):
                        host = arg
                        #Scan_Port()
                        Scan_Inf(host)
                        Scan_CGI(host)
                        Scan_JS(host)
                        print("Internal links:")
                        scrap(host)


if __name__ == "__main__":
        main(sys.argv[1:])
