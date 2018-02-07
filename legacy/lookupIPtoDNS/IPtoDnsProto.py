import socket
import os


def IPtoDNS(PATH, FNAME):
    with open(PATH + '/' + FNAME, 'r') as f:

        IPline = f.readlines()

    if len(IPline) > 0:

        for i in range(0, len(IPline)):
            IPline[i] = IPline[i].rstrip()
            print(IPline[i].strip())

    else:
        IPline = "No IP in File"

    return IPline

print("loading...")

result = open('result.txt', 'w')

for item in IPtoDNS(os.getcwd(), "ipList.txt"):
    try:
        item_DNS = socket.gethostbyaddr(item)
        result.write("%s\n" % item_DNS[0])
    except socket.error:
        result.write("DNS Not Found\n")
