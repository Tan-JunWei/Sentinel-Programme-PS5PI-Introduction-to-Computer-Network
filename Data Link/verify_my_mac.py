def verify_mac(mac_address):
    valid = False
    separator = mac_address[2]

    if len(mac_address) != 17:
        return valid

    else: 
        for i in mac_address.split(separator):
            # check chars
            for char in i:
                if char.isalpha() and char.lower() in 'abcdef':
                    valid = True
                elif char.isalpha() and char.upper() in 'ABCDEF':
                    valid = True
                elif char.isdigit() and int(char) in range(0, 10):
                    valid = True
                else:
                    valid = False
                    break
    
    return valid


mac_address_input = input("Enter a MAC address: ").strip()
valid_mac_address = verify_mac(mac_address_input)

if valid_mac_address:
    print("The MAC address is valid.")
else: 
    print("The MAC address is not valid.")