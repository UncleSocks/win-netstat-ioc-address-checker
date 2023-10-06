# netstat-ioc-address-checker
A basic IP address indicator of compromise (IOC) checker, written in Python 3, that compares the foreign address in Windows NetStat with a list of blacklisted IP addresses.

**How to Use**

Run the "netfor.py" Python3 script on the target Windows machine. By default, it will use the "ioc.txt" wordlist for the blacklisted IP addresses comparison. The list is from Cisco Talos Intelligence (https://www.talosintelligence.com/documents/ip-blacklist). 
To use your own wordlist, use the "-w" option and specify the location of the wordlist file. 

**Example**:
netfor.py -w C:\Users\$Username\Documents\$Custom_Wordlist_File

The script simply run the "netstat -n" command, parses the foreign address output, cleans up any address duplicate, stores the cleaned output into a list, and compares it to the provided wordlist.

**Output**

If there are no matching IP addresses, the script should output a "No matching blacklisted IP address identified." string. However, if there is a match it outputs a "Machine is currently connected to the following blacklisted IP addresses:" string with the list of matched IP addresses (from your wordlist).

**Note**: This sript is simply part of my Python learning path as I journey towards my capstone project for my InfoSec masters. However, I'm putting it out here for anyone to use and hopefully be of help.
