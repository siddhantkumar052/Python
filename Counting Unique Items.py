
import os
import sys

"""Taking input of the file name from the user"""
userInput = input("Enter the file name: ")
try:
    fHandle = open(userInput, 'r')
except IOError:
    print("Error: can\'t find file or read data.")
    sys.exit()

"""Part 1"""
"""Counting number of unique addresses in the file"""
if os.stat(userInput).st_size != 0:
    uniqueMails = 0
    items = set()
    for line in fHandle:
        if line.startswith("From:"):
            email = line.split(":")[1].split()
            if email[0].find("@"):
                items.add(email[0])
    uniqueMails = len(items)
    if uniqueMails > 0:
        print(f"Number of unique mail addresses found in {userInput} is \"{uniqueMails}\".")
    else:
        print("File does not contain sender's email address.")
else:
    print("File is empty.")

"""Part 2"""
"""Counting highest number of mails sent by a sender"""
try:
    fHandle = open(userInput, 'r')
except IOError:
    print("Error: can\'t find file or read data.")
    sys.exit()

if os.stat(userInput).st_size != 0:
    senders = dict()
    for line in fHandle:
        if line.startswith("From:"):
            email = line.split(":")[1].split()
            if email[0].find("@"):
                senders[email[0]] = senders.get(email[0], 0) + 1
    highCount = 0
    moreEmail = 0
    for email, count in senders.items():
        if highCount == 0 or highCount < count:
            moreEmail = email
            highCount = count
    if moreEmail != 0 and highCount > 0:
        print(f"Most number of emails are sent by \"{moreEmail}\" that is \"{highCount}\" mails.")
    else:
        print("File does not contain sender's email address.")
else:
    print("File is empty.")

"""Part 3 """
"""Printing all the unique mails occured in the file"""
print(f"The mail id\'s recived are : {items}")
