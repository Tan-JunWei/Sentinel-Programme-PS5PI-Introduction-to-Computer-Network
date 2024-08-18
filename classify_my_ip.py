# Public IP addresses are used for communication outside the internal
# network and can be routed on the internet.
# Private IP addresses are used within a private network and cannot be directly accessed from the 
# outside internet. They fall within specific ranges  (e.g.,  192.168.x.x ,  10.x.x.x ,  172.16.x.x  
# to 172.31.x.x ).
# Localhost (Loopback) address ( 127.0.0.1 ) is used by a device to
# send messages to itself. It's useful for testing and development.

# 1.
# Write a Python function
# classify_ip(ip)
# that takes an IPaddress as input, validates it, and classifi es it as 'private', 'public', or'localhost'. If the 
# IP address is invalid, it should return 'invalid'.
# 2.
# Test your function with the following IP addresses and classify each.Explain your findings:
# 192.168.1.1
# 10.25.30.50
# 172.20.10.5
# 127.0.0.1
# 172.32.0.1
# 216.58.214.206
import ipaddress
def classify_ip(ip):
    try:
        ip_add = ipaddress.ip_address(ip)
    except ValueError:
        return "invalid"
    
    if ip_add.is_loopback:
        return "localhost"
    elif ip_add.is_private:
        return "private"
    else:
        return "public"
    
print(classify_ip("192.168.1.1")) # private
print(classify_ip("10.25.30.50")) # private
print(classify_ip("172.20.10.5")) # private
print(classify_ip("127.0.0.1")) # localhost
print(classify_ip("172.32.0.1")) # public
print(classify_ip("216.58.214.206")) # public

# invalid trials
print(classify_ip("1923.168.1.1")) 
print(classify_ip("192.256.4.1")) 
print(classify_ip("255.255.255.256")) 
