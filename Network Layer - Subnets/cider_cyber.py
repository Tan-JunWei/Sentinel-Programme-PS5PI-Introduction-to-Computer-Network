# Cider Cyber 🍏
# Add CIDR support to the script from the previous exercise.

# Background on CIDR Notation
# CIDR (Classless Inter-Domain Routing) notation is a shorthand for specifying IP addresses and their associated network prefixes. 
# It combines an IP address, a slash (/), and a number indicating the length of the subnet mask in bits.

# For example, 192.168.1.0/24 in CIDR notation:

# The IP address 192.168.1.0 represents the network address.
# The /24 indicates that the first 24 bits (out of 32 for an IPv4 address) are used for the network portion, leaving 8 bits for host 
# addresses.
# The subnet mask corresponding to /24 is 255.255.255.0, dividing the IP address space into 256 addresses (192.168.1.0 to 192.168.1.255).
# The usable range for devices within this subnet is 192.168.1.1 to 192.168.1.254.

# Instructions
# Prompt for Input: Prompt the user to enter an IP address and a subnet. If the subnet is in CIDR notation (e.g., 192.168.1.0/24), 
# there's no need to ask for a subnet mask. If not (e.g., 192.168.1.0), prompt them to enter a subnet mask.

# Subnet Membership Check: Write a function to determine if the provided IP address falls within the given subnet's range.

# Calculate and Print Subnet Range: Calculate the range of valid IP addresses within the provided subnet and display this range to the
# user.

# Example Usage and Output
# Example of using CIDR Notation as input for subnet:

# Please enter a subnet (CIDR notation): 192.168.1.0/24
# Please enter an IP address: 192.168.1.10
# IP address 192.168.1.10 belongs to the subnet 192.168.1.0/24.
# Subnet Range: 192.168.1.1 to 192.168.1.254

# Example of using subnet masks as input if CIDR Notation is not given:
# Please enter the subnet address: 192.168.1.0
# Please enter the subnet mask (e.g., 255.255.255.0): 255.255.255.0
# Please enter an IP address: 192.168.1.10
# IP address 192.168.1.10 belongs to the subnet 192.168.1.0/24.
# Subnet Range: 192.168.1.1 to 192.168.1.25

import ipaddress

def calculate_cidr(subnet_mask):
    return subnet_mask.split(".").count("255") * 8

subnet = input("Please enter a subnet: ")

if "/" not in subnet:
    subnet_mask = input("Please enter the subnet mask (e.g., 255.255.255.0): ")
    subnet = f"{subnet}/{calculate_cidr(subnet_mask)}"

ip_address = input("Please enter an IP address: ")

subnet_network = ipaddress.ip_network(subnet, strict=False)

if ipaddress.ip_address(ip_address) in subnet_network:
    print(f"IP address {ip_address} belongs to the subnet {subnet}.")
    print(f"Subnet Range: {subnet_network.network_address+1} to {subnet_network.broadcast_address-1}")

else:
    print(f"IP address {ip_address} does NOT belong to the subnet {subnet}.")
    print(f"Subnet Range: {subnet_network.network_address+1} to {subnet_network.broadcast_address-1}")


