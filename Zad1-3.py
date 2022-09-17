import ipaddress

import netifaces as ni
from scapy.all import *
from scapy.layers.inet import IP, ICMP, TCP
import netaddr
import socket
import scapy.all as scapy

from scapy.layers.l2 import ARP, Ether

# 1. Ustalić własny adres IP.
ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
print(ip)

# 2. Ustalić maskę podsieci.
mask = ni.ifaddresses('eth0')[ni.AF_INET][0]['netmask']
print(mask)

# 3. Na podstawie powyższych informacji przeskanować sieć i ustalić adres IP celu.

target_ip = netaddr.IPNetwork('%s/%s' % (ip, mask))
target_ip_str = str(target_ip)
p = 219
i=1
while i <= 255 :
    ip_str = '10.3.117.' + str(p)
    port = 1274
    packet = IP(dst=ip_str, ttl=20)/TCP(dport=80, sport=port) 
    reply = sr1(packet, timeout=3)
    i += 1
    port += 1
    print(ip_str)
    print(reply)
    p += 1




