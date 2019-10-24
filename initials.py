"""
Tung Hoang - 10/04/19
This program will ask for the user name, then it will figure out what the
initials would be with the given name
"""

# Ask user for full name
fullName = input("Full Name: ")

# Split the full name into first, middle, and last names then eliminate
# whitespaces
nameList = fullName.split(" ")
while "" in nameList:
    nameList.remove("")

# Set the initials as the first letter of every name
initials = ""
for name in nameList:
    initials += name[0].upper()

print ("Initials: " + initials)
