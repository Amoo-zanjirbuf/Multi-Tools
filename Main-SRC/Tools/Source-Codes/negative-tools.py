import sys,os
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

def display_menu():
    print(Fore.GREEN + """
    ―――――――――――――――――――――――――――――――――――――――――――――――――――――――
    1. Ip-Scanner                   | 7. Sub-Domain-Scanner      
    2. Removed...                   | 8. DDOS-TOOL
    3. Removed...                   | 9. Discord-Token-Grabber
    4. Email-Boomber                | 10. Soon
    5. Phone-Locator                | 11. Soon
    6. Port-Scanner                 | 12. Soon
    ――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    """)

def execute_command(command):
    if command == '1':
        os.startfile("ip-lookup.exe")
    elif command == '2':
        print("Removed...")
    elif command == '3':
        print("Removed...")
    elif command == '4':
        os.startfile("email-bomber.exe")
    elif command == '5':
        os.startfile("phone-locator.exe")
    elif command == '6':
        os.startfile("port-scanner.exe")
    elif command == '7':
        os.startfile("subdomain\\main.exe")
    elif command == '8':
        os.startfile("ddos.exe")
    elif command == '9':
        os.startfile("discord-token-grabber.exe")
    elif command == '10':
        print("Soon...")
    elif command == '11':
        print("Soon...")
    elif command == '12':
        print("Soon...")
    else:
        print(Fore.RED + 'Invalid option! Please choose the correct one.')

while True:
    display_menu()
    command = input('> ')

    if command.lower() == 'exit':
        break

    execute_command(command)
