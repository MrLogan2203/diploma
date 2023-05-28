import argparse
import colorama
from colorama import Fore
from shodan_test import Scan_Inf
from scrapping.scripts_search import Scan_CGI, Scan_JS
from scrapping.scrap import scrap,save
from scrapping.headers_search import Headers_Search
from port_scanner import run,scan

def main():
        # Create an argument parser
        parser = argparse.ArgumentParser()

        # Add the '-t' argument to specify a target host
        parser.add_argument('-t', metavar='<string>', help='provide a target host')

        # Add the '-s' argument for handling scrap function
        parser.add_argument('-s', metavar='<int>', type=int, nargs='?',default = 1, help='provide an integer value for scrapping depth. default = 1, only provided host is scanning')
        
        parser.add_argument('-p', metavar='<str>', type=str, nargs='?',const='1-65535', help ='provide the str range of ports to scan e.g. 1-500. Default is 1-65535, mention that it might be time consuming') 
        
        # Add the '--scripts' argument for handling the headers_searcher functions
        parser.add_argument('--scripts', action='store_true', help='use this argument to search for CGI and JS scripts on a target host')

        # Parse the command-line arguments
        args = parser.parse_args()

        # Check if the '-t' argument was provided
        if args.t:
            Scan_Inf(args.t)
            Headers_Search(args.t)
            
        if args.t and args.p:
            host = args.t
            start_port, end_port = map(int,args.p.split('-'))
            print(Fore.GREEN + f"Scanning for open ports from port {start_port} to {end_port}..."+Fore.WHITE)
            run(host, scan, start_port, end_port)
            print(Fore.GREEN + f"Scanning is done!"+Fore.WHITE)

        # Check if the '-s' argument was provided
        if args.t and args.s:
            name = args.t.replace(".","_")
            print(Fore.GREEN+f"Saving links..." + Fore.WHITE)
            scrap(args.t, args.s)
            save(args.t)
            print(Fore.GREEN+"Done!" + Fore.WHITE)
        elif args.t and args.s == None:
            print(Fore.GREEN+f"Saving links..." + Fore.WHITE)
            scrap(args.t, 1)
            save(args.t)
            print(Fore.GREEN+"Done!" + Fore.WHITE)
        
        # Cgeck if the '--scripts' argument was provided    
        if args.scripts:
                Scan_CGI(args.t)
                Scan_JS(args.t)

if __name__ == "__main__":
        main()
