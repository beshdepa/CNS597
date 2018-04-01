##### Problem #####
##### CNS-380/597 - Ryan Haley####
#Solved by Ben Sherry

#Write a regular expression to fit the following:

#1 Phone number in the format of
#  xxx-xxx-xxxx
\d{3}\-\d{3}\-\d{4}


#2 Phone number in the format of
#  (xxx) xxx-xxx
#student comment: I'm going to assume that this is supposed to be (xxx) xxx-xxxx
\(\d{3}\)\ \d{3}\-\d{4}


#3 Phone number in the format of
#  +x xxx.xxx.xxxx
\+\d\ \d{3}\.\d{3}\.\d{4}



#4 SSN in the format of
#  xxx-xx-xxxx or xxxxxxxxx
\d{3}\-?\d{3}\-?\d{4}