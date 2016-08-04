import re

pattern=re.compile("^(\d{3})-(\d{3})-(\d{4})$")
phoneNumber=raw_input("Please enter the phone number:")

valid=pattern.match(phoneNumber)
if valid:
	print("ok, thats a valid num!")
else:
	print("\nplease enter the number in the following format xxx-xxx-xxxx")