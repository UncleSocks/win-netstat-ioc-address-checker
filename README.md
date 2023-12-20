# Windows Netstat IOC Address Checker
A basic IP address indicator of compromise (IOC) checker, written in Python 3, that compares the foreign address in Windows Netstat with a list of blacklisted IP addresses.

**How to Use**

Run the "netioc.py" Python3 script on the target Windows machine. By default, it will use the "ioc.txt" wordlist for the blacklisted IP addresses comparison. The list is from Cisco Talos Intelligence (https://www.talosintelligence.com/documents/ip-blacklist). 
To use your own wordlist, use the "-w" option and specify the location of the wordlist file. A "-h" option is also available for help reference.

![image](https://github.com/UncleSocks/win-netstat-ioc-address-checker/assets/79778613/9d6550ae-c38c-4441-ab87-253c26734898)



**Example**:
netioc.py -w C:\Users\\$Username\Documents\\$Custom_Wordlist_File.txt

The script simply run the "netstat -n" command, parses the foreign address output, cleans up any address duplicate, stores the cleaned output into a list, and compares it to the provided wordlist.

**Output**

If there are no matching IP addresses, the script should output a "No matching blacklisted IP address identified." string. However, if there is a match it outputs a "Machine is currently connected to the following blacklisted IP addresses:" string with the list of matched IP addresses (from your wordlist).

**Note**: This script is just a part of my Python learning path as I journey towards my capstone project for my InfoSec masters. However, I'm putting it out here for anyone to use and hopefully be of help.
