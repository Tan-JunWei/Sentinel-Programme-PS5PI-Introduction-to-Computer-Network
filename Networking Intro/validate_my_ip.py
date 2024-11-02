# Task
# 1. Write a Python function validate_ipv(ip) that checks if the input string is a valid IP address 
# and returns True if it is, or False otherwise. The criteria for a valid IP address are:

# It must have exactly four octets (four sets of numbers separated by dots).
# Each octet must be a decimal number ranging from 0 to 255.
# No leading zeros are allowed in any octet (e.g., 192.168.01.1
# is invalid).

# 2. Test your function with the following IP addresses to determine their validity.
# 192.168.1.1
# 256.100.50.25
# 123.45.67
# 172.16.254.1

# 10.0.0.256
# 192.168.01.1

def validate_ipv(ip):
    octets = ip.split(".")
    if len(octets) != 4:
        return False
    for octet in octets:
        if not octet.isdigit():
            return False
        if len(octet) > 1 and octet[0] == "0": # Reject octets with leading zeros (like "01", "001")
            return False
        if int(octet) < 0 or int(octet) > 255:
            return False
    return True

print(validate_ipv("192.168.1.1")) # True
print(validate_ipv("256.100.50.25")) # False
print(validate_ipv("123.45.67")) # False
print(validate_ipv("172.16.254.1")) # True
print(validate_ipv("10.0.0.256")) # False
print(validate_ipv("192.168.01.1")) # False
print(validate_ipv("0.2.3.0")) # True