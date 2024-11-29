from scapy.all import Ether, ARP, IP, UDP, DNS, DNSQR, DNSRR, TCP, wrpcap, Raw
import random

vendor_mac_prefixes = {
    "Apple": ["00:1A:2B", "00:1B:63", "00:1C:B3"],
    "Intel": ["00:1A:80", "00:1B:21", "00:1B:77"],
    "HP": ["00:09:6B", "00:0A:57", "00:0B:CD"]
}

# Function to generate random MAC addresses, except for Carol's device as per the clue
def random_mac(vendor=""):
    if vendor in vendor_mac_prefixes:
        return random.choice(vendor_mac_prefixes[vendor]).lower() + ":" + ":".join(["%02x" % random.randint(0, 255) for _ in range(3)])
    # Random MAC for other devices
    return "02:%02x:%02x:%02x:%02x:%02x" % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Default gateway IP and MAC address
gateway_ip = "192.168.0.1"
gateway_mac = "02:00:00:00:01:01"

# List of devices with specific adjustment for Carol's iPhone
devices = [
    {"name": "Alice's iPhone", "ip": "192.168.0.2", "mac": random_mac("Apple")},
    {"name": "Bob-PC", "ip": "192.168.0.3", "mac": random_mac("Intel")},
    {"name": "Carol's iPhone", "ip": "192.168.0.4", "mac": vendor_mac_prefixes["Apple"][0].lower() + ":8c:3a:e3"},
    {"name": "Dan-PC", "ip": "192.168.0.5", "mac": random_mac("HP")},
    {"name": "Eve's iPhone", "ip": "192.168.0.6", "mac": random_mac("Apple")},
    {"name": "Frank-PC", "ip": "192.168.0.7", "mac": random_mac("Intel")},
    {"name": "Grace's iPhone", "ip": "192.168.0.8", "mac": random_mac("Apple")},
    {"name": "Hank-PC", "ip": "192.168.0.9", "mac": random_mac("Intel")},
    {"name": "Ivy's iPhone", "ip": "192.168.0.10", "mac": random_mac("Apple")}
]

# Initialize request-response pairs
request_response_pairs = []

# Generate ARP packets for all devices and DNS queries from Bob-PC for each device, with responses
for device in devices:
    arp_req = Ether(dst="ff:ff:ff:ff:ff:ff", src=gateway_mac) / ARP(pdst=device["ip"], psrc=gateway_ip, hwsrc=gateway_mac)
    arp_rep = Ether(dst=gateway_mac, src=device["mac"]) / ARP(op=2, pdst=gateway_ip, psrc=device["ip"], hwdst=gateway_mac, hwsrc=device["mac"])
    request_response_pairs.append((arp_req, arp_rep))

    # DNS queries are made by Bob-PC for all devices
    bob_pc = next(device for device in devices if "Bob-PC" == device["name"])
    device_query_name = device["name"]#.replace("-", "").lower() + ".local"
    transaction_id = random.randint(0, 65535)  # Generate a random transaction ID
    dns_query = Ether(dst=gateway_mac, src=bob_pc["mac"]) / IP(dst=gateway_ip, src=bob_pc["ip"]) / UDP(dport=53) / DNS(id=transaction_id, rd=1, qd=DNSQR(qname=device_query_name))
    dns_response = Ether(dst=bob_pc["mac"], src=gateway_mac) / IP(dst=bob_pc["ip"], src=gateway_ip) / UDP(sport=53) / DNS(id=transaction_id, qr=1, aa=1, rd=1, qd=DNSQR(qname=device_query_name), an=DNSRR(rrname=device_query_name, ttl=86400, rdata=device["ip"]))
    request_response_pairs.append((dns_query, dns_response))

# Add the HTTP red-herring packet pair for Eve
eve_device = next(device for device in devices if "Eve's iPhone" == device["name"])
eve_sport = random.randint(1024, 65535)
http_req = Ether(src=eve_device["mac"], dst=gateway_mac) / IP(src=eve_device["ip"], dst="13.37.13.37") / TCP(sport=eve_sport, dport=80, flags="PA") / Raw(load="GET /how-to-hack-smart-fridges-and-steal-cookies HTTP/1.1\r\nHost: dubiousinfo.com\r\n\r\n")
http_res = Ether(src=gateway_mac, dst=eve_device["mac"]) / IP(src="13.37.13.37", dst=eve_device["ip"]) / TCP(sport=80, dport=eve_sport, flags="PA") / Raw(load="HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<html><body><h1>How to Hack Smart Fridges (and Steal Cookies)</h1><p>Don't try this at home!</p></body></html>")
request_response_pairs.append((http_req, http_res))

# Create a list of only the requests and shuffle
packets = [req for req, _ in request_response_pairs]
random.shuffle(packets)

# Iterate through the responses and add them ensuring they appear after their respective requests
for req, resp in request_response_pairs:
    insert_index = random.randint(packets.index(req) + 1, len(packets))
    packets.insert(insert_index, resp)

# Write the packets to a pcap file
wrpcap("network_capture_enhanced.pcap", packets)

print("Network capture file generated.")
