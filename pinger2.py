import sys
import subprocess
import platform

def ping(ip):
    response = "No"
    time = None
    try:
        # Determine the platform and set the appropriate ping command
        if platform.system() == "Windows":
            ping_command = ['ping', '-n', '1', ip]
        else:
            ping_command = ['ping', '-c', '1', ip]

        # Execute the ping command and capture the output
        ping_output = subprocess.check_output(ping_command, stderr=subprocess.STDOUT, universal_newlines=True)
        
        # Print the raw output for debugging
        print(f"Debug: ping_output for {ip}:\n{ping_output}")

        # Check for "time=" in the output for Unix-like systems or "time=" in Windows
        if "time=" in ping_output:
            time = ping_output.split("time=")[1].split(" ")[0]
            response = "Yes"
        elif "time=" in ping_output.lower():
            time = ping_output.split("time=")[1].split(" ")[0]
            response = "Yes"

    except subprocess.CalledProcessError:
        response = "No"

    return response, time

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for ip in sys.argv[1:]:
            ping_response, response_time = ping(ip)
            if ping_response == 'Yes' and response_time:
                print(f"IP Address: {ip} | Responded: {ping_response} | Response Time: {response_time} ms")
            else:
                print(f"IP Address: {ip} | Responded: {ping_response}")
