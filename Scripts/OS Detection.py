from scapy.all import *

import socket
from scapy.layers.inet import IP, ICMP
from scapy.layers.inet import IP,TCP
from scapy.layers.inet import IP, ICMP

ip = scapy.all.IP()
icmp = scapy.all.ICMP()
icmp.dst = str(input("Enter the Host IP Yu want to check\n"))
pack = ip / icmp
res = sr1(pack, timeout=3, verbose=0)
if res:
    if IP in res:
        print("Host is UP")
        ttl = res.getlayer(IP).ttl
        if ttl > 64:
            print("Host is running Windows OS")
        elif ttl <= 64:
            print("Host is running Linux OS")
else:
    print("Host is Down")