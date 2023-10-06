import subprocess
import argparse

nsOutput = subprocess.check_output("netstat -n").decode('ascii').splitlines()
nsOutputStartLine = nsOutput[5:]

nsForeignAddress = [output[2] for output in map(str.split, nsOutputStartLine)]

uniqueForeignAddress = []
seenForeignAddress = set()
for entry in nsForeignAddress:
    foreignAddressAndPort = entry.split(":")
    foreignAddressOnly = foreignAddressAndPort[0]

    if  foreignAddressOnly not in seenForeignAddress:
        seenForeignAddress.add(foreignAddressOnly)
        uniqueForeignAddress.append(foreignAddressOnly)

parser = argparse.ArgumentParser(description="Netstat IP IOC Checker")
parser.add_argument("-w","--wordlist", default= "ioc.txt", help="IP address IOC wordlist file location.")
args = parser.parse_args()


iocAddress = []
with open(args.wordlist) as ioc:
    for entry in ioc:
        entry = entry.strip()
        iocAddress.append(entry)
matchedAddress = set(iocAddress).intersection(uniqueForeignAddress)

if not matchedAddress:
    print("No matching blacklisted IP address identified.")
else:
    print("Machine is currently connected to the following blacklisted IP addresses:")
    for match in matchedAddress:
        print(match)
