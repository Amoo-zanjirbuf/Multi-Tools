import os
from random import randint
from colorama import init, Fore
from time import sleep
from pwinput import pwinput
from webbrowser import open
init(autoreset=True)


try:
    os.remove("Installer.exe")
except:
    pass

os.chdir("Tools")

red = Fore.RED
yellow = Fore.LIGHTYELLOW_EX
cyan = Fore.CYAN
green = Fore.GREEN
plus = f"{red}[{green}+{red}]{yellow}"
err = f"{red}[-]{yellow}"

creator = f"{plus} Made With {red}<3 {yellow}BY :{red} Amoo_zanjirbuf\n"
version = f"{plus} Version : {red}0.3\n"


skull = f'''{yellow}
                                .,od88888888888bo,.
                            .d88888888888888888888888b.
                         .d88888888888888888888888888888b.
                       .d888888888888888888888888888888888b.
                     .d8888888888888888888888888888888888888b.
                    d88888888888888888888888888888888888888888b
                   d8888888888888888888888888888888888888888888b
                  d888888888888888888888888888888888888888888888
                  8888888888888888888888888888888888888888888888
                  8888888888888888888888888888888888888888888888
                  8888888888888888888888888888888888888888888888
                  Y88888888888888888888888888888888888888888888P
                  "8888888888P'   "Y8888888888P"    "Y888888888"
                   88888888P        Y88888888P        Y88888888
                   Y8888888          ]888888P          8888888P
                    Y888888          d888888b          888888P
                     Y88888b        d88888888b        d88888P
                      Y888888b.   .d88888888888b.   .d888888
                       Y8888888888888888P Y8888888888888888
                        888888888888888P   Y88888888888888
                        "8888888888888[     ]888888888888"
                           "Y888888888888888888888888P"
                                "Y88888888888888P"
                             888b  Y8888888888P  d888
                             "888b              d888"
                              Y888bo.        .od888P
                               Y888888888888888888P
                                "Y88888888888888P"
                                  "Y8888888888P"
          d8888bo.                  "Y888888P"                  .od888b
         888888888bo.                  """"                  .od8888888
         "88888888888b.                                   .od888888888[
         d8888888888888bo.                              .od888888888888
       d88888888888888888888bo.                     .od8888888888888888b
       ]888888888888888888888888bo.            .od8888888888888888888888b=
       888888888P" "Y888888888888888bo.     .od88888888888888P" "Y888888P=
        Y8888P"           "Y888888888888bd888888888888P"            "Y8P
          ""                   "Y8888888888888888P"
                                 .od8888888888bo.
                             .od888888888888888888bo.
                         .od8888888888P"  "Y8888888888bo.
                      .od8888888888P"        "Y8888888888bo.
                  .od88888888888P"              "Y88888888888bo.
        .od888888888888888888P"                    "Y8888888888888888bo.
       Y8888888888888888888P"                         "Y8888888888888888b=
       888888888888888888P"                            "Y8888888888888888=
        "Y888888888888888                                "Y88888888888888P=
             ""Y8888888P                                  "Y888888P"
                "Y8888P                                     Y888P"
                   ""                                        """ 


'''

help = f'''{yellow}
_____________________________________________________________________________________________

{red}[{green}0{red}]{yellow} Exit                                     {red}[{green}5{red}]{yellow} Opens C4J Port Scanner BY Amoo_zanjirbuf      
{red}[{green}1{red}]{yellow} Opens SMS-Bomber BY @esfelurm            {red}[{green}6{red}]{yellow} Opens Webhook-Spammer BY Amoo_zanjirbuf       
{red}[{green}2{red}]{yellow} Opens Qubo Scanner BY replydev           {red}[{green}7{red}]{yellow} Opens Negative-Tools BY Amoo_zanjirbuf        
{red}[{green}3{red}]{yellow} Opens Pysilon Malware BY mategol         {red}[{green}8{red}]{yellow} Opens Discord Nuke Bot BY TKperson            
{red}[{green}4{red}]{yellow} Opens Recaf ByteCode Editor BY Col-E     {red}[{green}9{red}]{yellow} Clears The Screen  

_____________________________________________________________________________________________

'''


def cls():
    os.system("cls")
    print(skull + creator + version + help)

print(skull + creator + version)


# adminUser = ""
# adminPass = ""
access = False
troll = False

while True:
    try:
        user = input(f"{plus} Enter UserName>{Fore.CYAN} ")
        password = pwinput(f"{plus} Enter PassWord>{Fore.CYAN} ")

        if user == "troll" or password == "troll" :
            print(f"{plus} Logged in as \"{user}\" Access Granted")
            print(f"{plus} Troll Mode Activated...")
            # access = True
            troll = True
            sleep(2)
            break

        elif user == user and password == password:
            print(f"{plus} Logged in as \"{user}\" Access Granted")
            access = True
            sleep(2)
            break

        else:
            # Soon :)
            print(f"{err} Wrong Username OR Password...")
            
    except:
        print(f"{err} Something Went Wrong...")


if troll == True:
    chance = randint(0,100)
    if chance <= 85:
        open("https://whatismyipaddress.com/#google_vignette")
        sleep(10)
        open("https://www.youtube.com/watch?v=xvFZjo5PgG0")
        sleep(10)
        open("https://www.google.com/search?q=download+more+ram&sca_esv=f807be754d1cd3a2&sxsrf=ACQVn0_zybx0V-8CHjshxsbF82Luj94ocQ%3A1714421751628&ei=9_8vZpP9JbWpxc8PlZGUsAc&udm=&ved=0ahUKEwjT1IDcnuiFAxW1VPEDHZUIBXYQ4dUDCBA&uact=5&oq=download+more+ram&gs_lp=Egxnd3Mtd2l6LXNlcnAiEWRvd25sb2FkIG1vcmUgcmFtMggQABiABBjLATIIEAAYgAQYywEyCBAAGIAEGMsBMggQABiABBjLATIIEAAYgAQYywEyCBAAGIAEGMsBMggQABiABBjLATIIEAAYgAQYywEyCBAAGIAEGMsBMggQABiABBjLAUipDFCNBVj6CXABeAGQAQCYAacCoAHuCKoBAzItNLgBA8gBAPgBAZgCAqACkwLCAgoQABiwAxjWBBhHwgINEAAYgAQYsAMYQxiKBZgDAIgGAZAGBJIHBTEuMC4xoAeNHw&sclient=gws-wiz-serp")
        sleep(10)
        open("https://www.google.com/search?q=ok+i%27m+done+now%2C+you%27re+free&oq=ok&gs_lcrp=EgZjaHJvbWUqCAgAEEUYJxg7MggIABBFGCcYOzIGCAEQRRg7MgYIAhBFGDsyEAgDEC4YgwEY1AIYsQMYgAQyCggEEAAYsQMYgAQyBwgFEAAYgAQyEAgGEC4YgwEY1AIYsQMYgAQyDAgHEAAYQxiABBiKBTIKCAgQABixAxiABDIHCAkQABiPAtIBCDEzMTRqMGo3qAIIsAIB&sourceid=chrome&ie=UTF-8")
    else:
        print(f"{plus} You Lucky One...")
        sleep(2)

cls()

while True:
    try:
        command = input(f"{plus} MultiTools> {cyan}").strip().lower()
        if command == "1" and access == True:
            os.startfile("sms.exe")
            print(f"{plus} Opened sms.exe BY @esfelurm...")

        elif command == "2" and access == True:
            os.startfile("qubo.jar")
            print(f"{plus} Opened qubo.jar BY replydev...")

        elif command == "3" and access == True:
            os.startfile("PySilon-malware-main\\PySilon.bat")
            print(f"{plus} Opened PySilon.bat BY mategol...")

        elif command == "4" and access == True:
            os.startfile("recaf.jar")
            print(f"{plus} Opened recaf.jar BY Col-E...")

        elif command == "5" and access == True:
            os.startfile("C4J.exe")
            print(f"{plus} Opened C4J.exe BY Amoo_zanjirbuf...")

        elif command == "6" and access == True:
            os.startfile("webhook.exe")
            print(f"{plus} Opened webhook.exe BY Amoo_zanjirbuf...")
        
        elif command == "7" and access == True:
            os.startfile("Negative-GUI.exe")
            print(f"{plus} Opened Negative-Tools BY Amoo_zanjirbuf")

        elif command == "8" and access == True:
            os.startfile("Nuke.exe")
            print(f"{plus} Opened Nuke.exe BY TKperson...")

        elif command == "9" and access == True:
            print(f"{plus} No Way You Saw This...")
            cls()

        elif command == "0" and access == True:
            print(f"{plus} Exiting...")
            sleep(1)
            break    

        elif command == "help" and access == True:
            print(help)

        elif troll == True and access == False:
            print(f"{err} You Can Not Use This Command In Troll Mode...")

        else:
            print(f"{err} Unknown Command...")

    except:
        print(f"{err} Somthing Went Wrong...")

Fore.RESET

exit()