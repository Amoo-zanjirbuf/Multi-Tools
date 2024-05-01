import os
import sys 
import socket 
from datetime import datetime 
import colorama
from colorama import Fore
colorama.init()

os.system("cls")

print(Fore.MAGENTA+"""
―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
███╗   ██╗███████╗ ██████╗  █████╗ ████████╗██╗██╗   ██╗███████╗     █████╗ ████████╗████████╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ 
████╗  ██║██╔════╝██╔════╝ ██╔══██╗╚══██╔══╝██║██║   ██║██╔════╝    ██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██╔██╗ ██║█████╗  ██║  ███╗███████║   ██║   ██║██║   ██║█████╗█████╗███████║   ██║      ██║   ███████║██║     █████╔╝ █████╗  ██████╔╝
██║╚██╗██║██╔══╝  ██║   ██║██╔══██║   ██║   ██║╚██╗ ██╔╝██╔══╝╚════╝██╔══██║   ██║      ██║   ██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║ ╚████║███████╗╚██████╔╝██║  ██║   ██║   ██║ ╚████╔╝ ███████╗    ██║  ██║   ██║      ██║   ██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═══╝  ╚══════╝    ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                                                      
―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
                                                                 
BY: Amoo_zanjirbuf
""")

host = socket.gethostbyname(input(f"{Fore.GREEN}Enter your host ip address (E.x. '192.168.10.10) : "))

ports = input(str("Enter range between 1 to 1000 (E.x. 50) :  "))

print("-" * 40)
print("scanning : " + host)
print("Time started : " + str(datetime.now()))
print("-" * 40)
try:
             for port in range(int(ports)):
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    socket.setdefaulttimeout(1)
                    result = s.connect_ex((host,port))
                    if result == 0:
                            print(F"Following {port} is open")
                    s.close()
         
except KeyboardInterrupt:
    print("\r Exiting program")

except socket.gaierror:
    print("Host name could not be solved")
    Fore.WHITE
    sys.exit()
except socket.error:
    print("could not connect")
    Fore.WHITE
    sys.exit()