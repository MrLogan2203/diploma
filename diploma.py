import argparse
import colorama
from colorama import Fore
from port_scanner import Scan_Port
from shodan_test import Scan_Inf
from scrapping.scripts_search import Scan_CGI, Scan_JS
from scrapping.scrap import scrap,save
from scrapping.headers_search import Headers_Search

def main():
        # Create an argument parser
        parser = argparse.ArgumentParser()

        # Add the '-t' argument to specify a target host
        parser.add_argument('-t', metavar='<string>', help='provide a target host')

        # Add the '-s' argument for handling scrap function
        parser.add_argument('-s', metavar='<int>', type=int, nargs='?',const=1, help='provide an integer value for scrapping depth. default = 1, only provided host is scanning')
        
        # Add the '--scripts' argument for handling the headers_searcher functions
        parser.add_argument('--scripts', action='store_true', help='use this argument to search for CGI and JS scripts on a target host')

        # Parse the command-line arguments
        args = parser.parse_args()

        # Check if the '-t' argument was provided
        if args.t:
            Scan_Port(args.t)
            Scan_Inf(args.t)
            Headers_Search(args.t)

        # Check if the '-s' argument was provided
        if args.t and args.s:
            name = args.t.replace(".","_")
            print(Fore.GREEN+f"Saving links..." + Fore.WHITE)
            scrap(args.t, args.s)
            save(args.t)
            print(Fore.GREEN+"Done!" + Fore.WHITE)
        
        # Cgeck if the '--scripts' argument was provided    
        if args.scripts:
                Scan_CGI(args.t)
                Scan_JS(args.t)

if __name__ == "__main__":
        main()
