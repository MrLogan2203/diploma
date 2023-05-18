#!/usr/bin/python3
import shodan
import socket


api = shodan.Shodan('JRnrsKbAPhAL2LVdifFTr0PRlkdTVxyx')

def Scan_Inf(host_name):
        try:
                #host_name = input("Type host name: ")
                host_IP = socket.gethostbyname(host_name)
                #name = socket.gethostbyaddr(host_IP)
                host = api.host(host_IP)

                # Print general info
                print("""
                        IP: {}
                        Organization: {}
                        Operating System: {}
                """.format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))
        
                # Print all banners
                for item in host['data']:
                        print("""
                                Port: {}
                                Banner: {}
        
                        """.format(item['port'], item['data']))
        except socket.gaierror:
                print("Host not found")
                


