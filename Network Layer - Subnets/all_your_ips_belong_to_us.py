# All Your IPs Belong to Us
# Write a Python script that takes an IP address, a subnet, and a subnet mask from the user, then determines whether the IP address 
# belongs to the specified subnet.

# Additionally, the script should print the range of IP addresses within the subnet.

# Hint: Python ipaddress library

# Instructions
# Input Handling: Prompt the user to input an IP address, a subnet address and a subnet mask.
# Subnet Validation: Implement a function to verify if the given IP address belongs to the specified subnet. This involves:
# Calculating the network address from the subnet and subnet mask.
# Determining if the IP address falls within the range of the calculated network address and the last address in the subnet.
# Print Subnet Range: Based on the subnet mask, calculate and print the range of valid IP addresses within the subnet.
# Display Results: Inform the user whether the IP address belongs to the subnet and display the subnet's IP range.
# Example Usage and Output
# Example output of when an IP does not belong in the subnet

# Please enter an IP address: 192.168.1.5
# Please enter the subnet: 192.168.0.1
# Please enter the subnet mask: 255.255.255.0
# IP address 192.168.1.5 does NOT belong to the subnet 192.168.0.0/24.
# Subnet Range: 192.168.0.1 to 192.168.0.254
# Example output of when an IP belongs in the subnet

# Please enter an IP address: 192.168.0.60
# Please enter the subnet: 192.168.0.1
# Please enter the subnet mask: 255.255.255.0
# IP address 192.168.0.60 belongs to the subnet 192.168.0.0/24.
# Subnet Range: 192.168.0.1 to 192.168.0.254

import ipaddress

def calculate_cidr(subnet_mask):
    return subnet_mask.split(".").count("255") * 8

def check_ip_in_subnet(ip_address, subnet, subnet_mask):
    cidr = calculate_cidr(subnet_mask)
    check = ipaddress.ip_address(ip_address) in ipaddress.ip_network(f"{subnet}/{cidr}", strict=False)

    return check

ip_address = input("Please enter an IP address: ")
subnet = input("Please enter the subnet: ")
subnet_mask = input("Please enter the subnet mask: ")

subnet_network = ipaddress.ip_network(f"{subnet}/{calculate_cidr(subnet_mask)}", strict=False)

if check_ip_in_subnet(ip_address, subnet, subnet_mask):
    print(f"IP address {ip_address} belongs to the subnet {subnet}/{calculate_cidr(subnet_mask)}.")
    print(f"Subnet Range: {subnet_network.network_address+1} to {subnet_network.broadcast_address-1}")
else:
    print(f"IP address {ip_address} does NOT belong to the subnet {subnet}/{calculate_cidr(subnet_mask)}.")
    print(f"Subnet Range: {subnet_network.network_address+1} to {subnet_network.broadcast_address-1}")