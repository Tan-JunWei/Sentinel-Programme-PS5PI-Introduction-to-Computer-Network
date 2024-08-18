import requests

flagged_addresses = []

# Function to perform GeoIP lookup using the ipinfo.io API
def lookup_ip(ip_address):
    # Construct the API URL
    api_url = f"https://ipinfo.io/{ip_address}/json"
    try:
        # Make the API request
        response = requests.get(api_url)
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response and return it 
            return response.json()
        else:
            print(f"Failed to retrieve data for IP: {ip_address}, Status Code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Read IP addresses from the log file and perform GeoIP lookup
with open('server_log.txt', 'r') as file:
    # Read the file line by line
    for line in file:
        # Split the line into words
        words = line.split()
        # Example line: 2024-03-25T12:34:56 server request from 93.184.216.34: GET /index.html

        ip_address = words[-3].split(":")[0] 
        print(f"IP Address: {ip_address}")

        data = lookup_ip(ip_address)

        if data:
            print(data)
            try:
                if data['country'] == 'FR':
                    flagged_addresses.append(ip_address)
            except KeyError:
                print(f"Country information not available for IP: {ip_address}")


## Brief report on flagged IP addresses
print(f"\nFlagged IP Addresses from France ({len(flagged_addresses)}):")
for i in range(len(flagged_addresses)):
    print(f"Flagged IP Address {i+1}: {flagged_addresses[i]}")



