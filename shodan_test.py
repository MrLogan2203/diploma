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
                        Country: {}
                        City: {}
                        Latitude: {}
                        Longitude: {}
                        Hostnames: {}
                """.format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a'), host.get('country_name','n/a'), host.get('city','n/a'), host.get('latitude','n/a'), host.get('longitude','n/a'), host.get('hostnames','n/a')))
        
        except socket.gaierror:
                print("Host not found")
                


