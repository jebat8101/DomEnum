# DomEnum

This is a little tool made in Python which I wrote to automate subdomain enumeration procedure for myself. Actually it takes a domain as an input and uses OneForAll,Subfinder and Amass to derive subdomains, then it puts all the subdomains in a single file, delete the duplicate ones and performs Tomnomnom's Httprobe on it, after that the probed domains are passed to aquatone to take screenshots of the alive domains. It's a nice little tool but to use it, you might need to tweak the code a bit to point the calls according to your system paths. Thanks

## Command: sudo python3 DomEnum.py www.test.com
