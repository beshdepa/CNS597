##### Web Brute Force #####
##### CNS-380/597 Advanced Cybersecurity Automation - Ryan Haley####

'''
During your pentest you find a website that you believe to be of high value.
You decide to probe it to find any webpages it might be hiding and hopefullly
return a page with that you can use to gather contact information.

Write a script that will take in a list of file paths (you can use the txt
file provided WebPath.txt) and check them against the given website.
The script will then notify the user which link(s) were successful.

You then must scrape the webpage of any directories/files that were found and
return any phone numbers and email addresses you find on the page.

NOTE: This problem is only to be done against the given URL.
'''
import requests #using requests module
from requests import request #using request because I'm lazy
import urllib3 #importing requests required thing so I can interact with it
import re #import regex


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) # suppressing warnings regarding unverified HTTPS
print("Loading resources...") # status message
url = 'https://www.secdaemons.org/' #url to check
totalscrape = '' #sum total of text to regex through
emails = [] #email list
phnums = [] #phone number list


with open("WebPath.txt") as WebPath: #open file with paths in it
   paths = WebPath.read().split() #turn it into  a list
   
print("WARNING: Connecting with broken HTTPS. Standard URLLIB warnings suppressed. Checking URLS...")

for path in paths: # for each individual path
    print("Checking: "+path) #print status
    response = request("GET", url+path,verify=False) # make request
    if response.status_code==200: # if successful connection
        print("Page found! "+url+path) # print status
        totalscrape = totalscrape+response.text #add page contents to string to rege through
        
phnums = re.findall('\(?\d{3}\)?\ ?\-?\d{3}-?\ ?\d{4}',totalscrape) #search for phone numbers
emails = re.findall('\w{2,63}\@\w{2,63}\.com',totalscrape) # search for emails

print("Phone Numbers Found:")
print(phnums)
print("Emails found")
print(emails)
#status messages above
