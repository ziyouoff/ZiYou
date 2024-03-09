#==================[IMPORTS]==================#
import os
import time
import requests
from rich.console import Console
from rich.table import Table
con = Console()
#==================[IMPORTS]==================#
http_errors = {
    100: 'Continue',
    101: 'Switching Protocols',
    102: 'Processing',
    103: 'Early Hints',
    200: 'OK',
    201: 'Created',
    202: 'Accepted',
    203: 'Non-Authoritative Information',
    204: 'No Content',
    205: 'Reset Content',
    206: 'Partial Content',
    207: 'Multi-Status',
    208: 'Already Reported',
    226: 'IM Used',
    300: 'Multiple Choices',
    301: 'Moved Permanently',
    302: 'Found',
    303: 'See Other',
    304: 'Not Modified',
    305: 'Use Proxy',
    306: 'Switch Proxy',
    307: 'Temporary Redirect',
    308: 'Permanent Redirect',
    400: 'Bad Request',
    401: 'Unauthorized',
    402: 'Payment Required',
    403: 'Forbidden',
    404: 'Not Found',
    405: 'Method Not Allowed',
    406: 'Not Acceptable',
    407: 'Proxy Authentication Required',
    408: 'Request Timeout',
    409: 'Conflict',
    410: 'Gone',
    411: 'Length Required',
    412: 'Precondition Failed',
    413: 'Payload Too Large',
    414: 'URI Too Long',
    415: 'Unsupported Media Type',
    416: 'Range Not Satisfiable',
    417: 'Expectation Failed',
    418: "I'm a teapot",
    421: 'Misdirected Request',
    422: 'Unprocessable Entity',
    423: 'Locked',
    424: 'Failed Dependency',
    425: 'Too Early',
    426: 'Upgrade Required',
    428: 'Precondition Required',
    429: 'Too Many Requests',
    431: 'Request Header Fields Too Large',
    451: 'Unavailable For Legal Reasons',
    500: 'Internal Server Error',
    501: 'Not Implemented',
    502: 'Bad Gateway',
    503: 'Service Unavailable',
    504: 'Gateway Timeout',
    505: 'HTTP Version Not Supported',
    506: 'Variant Also Negotiates',
    507: 'Insufficient Storage',
    508: 'Loop Detected',
    510: 'Not Extended',
    511: 'Network Authentication Required'
}

def uclear():
    osname = os.name
    if osname == 'nt': os.system('cls')
    elif osname == 'posix': os.system('clear')

def import_dic():
    try:
        FILE = open('softs/dirbuster-dic.txt')
        dic = FILE.read()
        #!print(dic)
        sdic = dic.split('\n')
        con.log('[*]dirbuster-dic.txt loaded!', style='green')
        return sdic
    except: con.log('[*]dirbuster-dic.txt not found!', style='red')

def main():
    con.print('''
[red]██████╗ [/][dark_red]██╗[/][red]██████╗ [/][dark_red]██████╗ [/][red]██╗   ██╗[/][dark_red]███████╗[/][red]████████╗[/][dark_red]███████╗[/][red]██████╗ [/]
[red]██╔══██╗[/][dark_red]██║[/][red]██╔══██╗[/][dark_red]██╔══██╗[/][red]██║   ██║[/][dark_red]██╔════╝[/][red]╚══██╔══╝[/][dark_red]██╔════╝[/][red]██╔══██╗[/]
[red]██║  ██║[/][dark_red]██║[/][red]██████╔╝[/][dark_red]██████╔╝[/][red]██║   ██║[/][dark_red]███████╗[/][red]   ██║   [/][dark_red]█████╗  [/][red]██████╔╝[/]
[red]██║  ██║[/][dark_red]██║[/][red]██╔══██╗[/][dark_red]██╔══██╗[/][red]██║   ██║[/][dark_red]╚════██║[/][red]   ██║   [/][dark_red]██╔══╝  [/][red]██╔══██╗[/]
[red]██████╔╝[/][dark_red]██║[/][red]██║  ██║[/][dark_red]██████╔╝[/][red]╚██████╔╝[/][dark_red]███████║[/][red]   ██║   [/][dark_red]███████╗[/][red]██║  ██║[/]
[red]╚═════╝ [/][dark_red]╚═╝[/][red]╚═╝  ╚═╝[/][dark_red]╚═════╝ [/][red] ╚═════╝ [/][dark_red]╚══════╝[/][red]   ╚═╝   [/][dark_red]╚══════╝[/][red]╚═╝  ╚═╝[/]
[yellow]|   Version 1.0   |   Created by ZiYou    |    @ziyou_off   |[/]
''', justify='center')
    dic = import_dic()
    input_url = con.input('           [center][yellow][+]Введите ссылку для сканирования >> [/][/]')

    #==========[create_table]==========#
    table = Table(title='[red]Сканирование[/]')
    table.add_column('#', style='red', no_wrap=True)
    table.add_column('url', style='cyan', no_wrap=True)
    table.add_column('status code', style='yellow', no_wrap=True, justify='center')
    table.add_column('status', style='blue', no_wrap=True)
    table.add_column('time', style='magenta', no_wrap=True)
    #==========[create_table]==========#

    count_lines = 0
    for i in dic: count_lines += 1


    for i in range(count_lines):
        if input_url[-1] == '/': url = input_url + dic[i]
        elif input_url[-1] != '/': url = input_url + '/' + dic[i]

        start_time = time.time()
        try:
            request = requests.get(url)
            #!print(request.status_code)
        except: pass
        end_time = time.time()

        #TODO: if request.status_code == 200: color = 'green'
        #TODO: elif request.status_code == 404: color = 'red'
        #TODO: else: color = 'yellow'

        if request.status_code != 404:
            table.add_row(
                str(i), 
                url, 
                str(request.status_code), 
                str(http_errors[request.status_code]),
                str(end_time - start_time))
        
        if i % 10 == 0:
            uclear()
            con.print(table, justify='center')

uclear()
main()