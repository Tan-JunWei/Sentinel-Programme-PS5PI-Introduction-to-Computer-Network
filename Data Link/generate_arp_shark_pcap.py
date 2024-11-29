from scapy.all import *

def generate_arp_shark_pcap():
    packets = []

    # First set of ARP request and response
    arp_request1 = Ether(src="aa:bb:cc:dd:ee:ff", dst="ff:ff:ff:ff:ff:ff") / ARP(pdst="192.168.1.100", hwdst="00:00:00:00:00:00", psrc="192.168.1.1", hwsrc="aa:bb:cc:dd:ee:ff", op=1)
    arp_reply1 = Ether(src="52:1a:7f:9b:3e:cd", dst="aa:bb:cc:dd:ee:ff") / ARP(pdst="192.168.1.1", hwdst="aa:bb:cc:dd:ee:ff", psrc="192.168.1.100", hwsrc="52:1a:7f:9b:3e:cd", op=2)
    packets.append(arp_request1)
    packets.append(arp_reply1)

    # Second set of ARP request and response
    arp_request2 = Ether(src="aa:bb:cc:dd:ee:ff", dst="ff:ff:ff:ff:ff:ff") / ARP(pdst="192.168.1.150", hwdst="00:00:00:00:00:00", psrc="192.168.1.1", hwsrc="aa:bb:cc:dd:ee:ff", op=1)
    arp_reply2 = Ether(src="a6:4f:2d:8e:7c:51", dst="aa:bb:cc:dd:ee:ff") / ARP(pdst="192.168.1.1", hwdst="aa:bb:cc:dd:ee:ff", psrc="192.168.1.150", hwsrc="a6:4f:2d:8e:7c:51", op=2)
    packets.append(arp_request2)
    packets.append(arp_reply2)

    # ARP request without response (different subnet)
    arp_request3 = Ether(src="aa:bb:cc:dd:ee:ff", dst="ff:ff:ff:ff:ff:ff") / ARP(pdst="10.0.0.200", hwdst="00:00:00:00:00:00", psrc="192.168.1.1", hwsrc="aa:bb:cc:dd:ee:ff", op=1)
    packets.append(arp_request3)

    wrpcap("arp_shark.pcap", packets)

generate_arp_shark_pcap()