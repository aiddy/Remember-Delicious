#!/usr/bin/env python
# Python script to post a link to delicious
import getpass
import sys
import json

# pip install requests 
# pip install requests[security] (fpr SSL support)
# pip install requests_ntlm for NTLM
import requests 	

def usage():
	print "usage: postlink URL Description Tags"
	print ""
	print "   URL\t\tThe URL of the page to post to delicious"
	print "   Description\tA string providing a description for the link"
	print "   Tags\t\tA string providing a comma delimited list of tags for the link"
	print ""
	print "Add Delicious username to config.json"
	exit (-1)


with open('config.json', 'rb') as fp:
			config = json.load(fp)
			if config.get("user"):
				user = config.get("user")
			else:
				usage()	
		

if len(sys.argv) != 4:
	usage()

headers = {'user-agent': 'Remember-Delicious/0.0.1'}
payload = {"url": 	sys.argv[1], "description": sys.argv[2], "tags": sys.argv[3]}

print "Posting link to delicious for " + user
print "\t\t" + payload['url']
print "\t\t" + payload['description']
print "\t\t" + payload['tags']

print "Enter password for " + user
passwd = getpass.getpass()

call = "https://api.del.icio.us/v1/posts/add"

r = requests.put(call, 
	auth=(user, passwd), 
	params=payload,
	headers=headers)
if r.status_code == 200:
	print "sumbitted okay"
else:
	print "error submitting. status code: " + str(r.status_code) 
		



