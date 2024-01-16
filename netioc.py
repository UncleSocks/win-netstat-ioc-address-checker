import subprocess
import argparse

ns_output = subprocess.check_output("netstat -n").decode('ascii').splitlines()
ns_output_startline = ns_output[5:]

ns_foreign_address_parser = [output[2] for output in map(str.split, ns_output_startline)]

ns_output_startline = []
seen_foreign_addresses = set()
for match in ns_foreign_address_parser:
    foreign_address_and_port = match.split(":")
    parsed_foreign_address = foreign_address_and_port[0]

    if  parsed_foreign_address not in seen_foreign_addresses:
        seen_foreign_addresses.add(parsed_foreign_address)
        ns_output_startline.append(parsed_foreign_address)

argument_parser = argparse.ArgumentParser(description="Netstat IP IOC Checker")
argument_parser.add_argument("-w","--wordlist", default= "ioc.txt", help="IP address IOC wordlist file location.")
argument = argument_parser.parse_args()


ioc_address_list = []
with open(argument.wordlist) as ioc_wordlist:
    for entry in ioc_wordlist:
        entry = entry.strip()
        ioc_address_list.append(entry)
matched_address = set(ioc_address_list).intersection(ns_output_startline)

if not matched_address:
    print("No matching blacklisted IP address identified.")
else:
    print("Machine is currently connected to the following blacklisted IP addresses:")
    for match in matched_address:
        print(match)
