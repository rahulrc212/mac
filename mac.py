#!/usr/bin/python3
import requests
import json
f1=input("please Enter MAC addressin correc format")
link="https://api.macaddress.io/v1?apiKey=at_QAiM31cr6sXrT8pE3U25BXp8vNYhc&output=json&search="+f1
request=requests.get(link)
fd=request.json()
print (fd["vendorDetails"]["companyName"])
