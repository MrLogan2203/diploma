import socket
import threading
import concurrent.futures
import re
import time
import sys


def scan(ip, port):
    lock = threading.Lock()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(.1)

    try:
        con = s.connect((ip, port))
        with lock:
            result = f"Port {port} is OPEN Running {socket.getservbyport(port)}"
            print(result)
        con.close()
    except:
        pass


def run(ip_num: str, scan, start: int, end: int):
    with concurrent.futures.ThreadPoolExecutor(max_workers=200) as executor:
        try:
            for port in range(start,end+1):
                #print(port)
                executor.submit(scan, ip_num, port + 1)
        except KeyboardInterrupt:
            sys.exit()


def main():
    t = time.time()
    run("google.com", scan, 1,5000)
    print("Total execution time", time.time() - t)


if __name__ == "__main__":
    main()
