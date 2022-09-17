import mask as mask
import netaddr
from netaddr import ip
from scapy.all import ARP, Ether, srp
from scapy.layers.inet import IP, ICMP, TCP
import netifaces as ni

# 1. Ustalić własny adres IP.
ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
print(ip)

# 2. Ustalić maskę podsieci.
mask = ni.ifaddresses('eth0')[ni.AF_INET][0]['netmask']
print(mask)

# 3. Na podstawie powyższych informacji przeskanować sieć i ustalić adres IP celu.
from scapy.all import ARP, Ether, srp

target_ip = netaddr.IPNetwork('%s/%s' % (ip, mask))
target_ip_str = str(target_ip)
arp = ARP(pdst=target_ip_str)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
packet = ether/arp
result = srp(packet, timeout=3, verbose=1)[0]
clients = []

for sent, received in result:
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})

print("Available devices in the network:")
print("IP" + " "*18+"MAC")
for client in clients:
    print("{:16}    {}".format(client['ip'], client['mac']))
