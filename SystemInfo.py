#!/usr/bin/env python3

import re, sys, os,subprocess
from pwn import *
from termcolor import colored
import emoji


def main():
    if(len(sys.argv) != 2):
        print(colored('[?]','blue') + colored(' Usage SystemInfo <ip>','magenta'))
        sys.exit(1)

    print(colored('[*]','green') + colored(' SystemInfo by BlaZzes10','magenta'))
    try:
        p = subprocess.Popen(["/usr/bin/ping", "-c1", sys.argv[1]], stdout=subprocess.PIPE).stdout.read()
        response = p.decode()
        ttl = re.search(r'ttl=\w+',response)
        ttl = ttl.group().split('=')[1]
        sysinfo(ttl)
    except:
        print()
        print(colored('[-] error','red'))

def sysinfo(ttl):
    ttl = int(ttl)
    print()
    if(ttl <= 64):
        print(emoji.emojize(':heavy_multiplication_x:') + colored(' Linux', 'red') + colored(' ttl= {}'.format(ttl),'white'))
    elif(ttl <= 128):
        print(emoji.emojize(':heavy_multiplication_x:') + colored(' Windows', 'red') + colored(' ttl= {}'.format(ttl),'white'))
    else:
         print(emoji.emojize(':x:') + colored(' Other SO', 'red') + colored(' ttl= {}'.format(ttl),'white'))

try:
    main()
except KeyboardInterrupt:
    print("end")
