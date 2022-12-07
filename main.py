import pyfiglet
import sys
import socket
from datetime import datetime

# getting the banner printed on the shell!

ascii_banner = pyfiglet.figlet_format("VMAP")
print(ascii_banner)

# Defining a target

if(len(sys.argv) == 2):

    #translate hostname to IPv4 
    target = socket.gethostbyname(sys.argv[1])

else:
    print("Invalid amount of Arguement")

#Add Banner
print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at: " + str(datetime.now()))
print("-" * 50)

try:

    # scanning ports b/w 1 to 65535
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        # returns an error indicator
        result = s.connect_ex((target, port))
        if(result == 0):
            print("Port {} is open ".format(port))
        s.close()


except KeyboardInterrupt:
    print("\n Exiting the program !!!!")
    sys.exit()
except socket.gaierror:
    print("\n Hostname could not be resolved !!!!")
    sys.exit()
except socket.error:
    print("\ Server not responding !!!")
    sys.exit()
