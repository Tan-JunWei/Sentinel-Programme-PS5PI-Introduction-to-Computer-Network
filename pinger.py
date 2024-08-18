import sys
import subprocess

def ping(ip):
    response = "No"
    time = None
    try:
        ping_output = subprocess.check_output(['ping', '-n', '1', ip], stderr=subprocess.STDOUT, universal_newlines=True)

        if "TTL=" in ping_output:
            time = ping_output.split("time=")[1].split("ms")[0]
            response = "Yes"

    except subprocess.CalledProcessError:
        response = "No"

    return response, time

if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        ping_response, response_time = ping(sys.argv[i])
        if ping_response == 'Yes' and response_time:
            print(f"IP Address: {sys.argv[i]} | Responded: {ping_response} | Response Time: {response_time} ms")
        else:
            print(f"IP Address: {sys.argv[i]} | Responded: {ping_response}")

# python pinger.py ipaddress1 ipaddress2 ipaddress3

# Example usage and output (Given example in pdf)
# python pinger.py 8.8.8.8 1.1.1.1
# IP Address: 8.8.8.8 | Responded: Yes | Response Time: 7 ms
# IP Address: 1.1.1.1 | Responded: Yes | Response Time: 6 ms

# trials:
# python pinger.py 8.8.8.8 1.1.1.1 208.67.222.222 52.22.115.45 13.107.21.200 157.240.22.35 140.82.114.4
# IP Address: 8.8.8.8 | Responded: Yes | Response Time: 7 ms
# IP Address: 1.1.1.1 | Responded: Yes | Response Time: 8 ms
# IP Address: 208.67.222.222 | Responded: Yes | Response Time: 6 ms
# IP Address: 52.22.115.45 | Responded: No
# IP Address: 13.107.21.200 | Responded: Yes | Response Time: 8 ms
# IP Address: 157.240.22.35 | Responded: Yes | Response Time: 377 ms
# IP Address: 140.82.114.4 | Responded: Yes | Response Time: 288 ms
