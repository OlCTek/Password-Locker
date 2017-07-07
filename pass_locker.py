import csv
import time
import sys

password = '3486'
pass_dict = {}
confirm = ['yes', 'Yes', 'y', 'Y']
add_pass = ['add', 'Add']
no = ['no', 'No', 'n', 'N']
exit = ['no', 'No', 'exit', 'Exit', 'n', 'N']

def exit_pro():
	print("Very well.")
	time.sleep(1)
	print("Shutting down database...")
	time.sleep(1)
	print("Goodbye!")
	time.sleep(1)
	sys.exit()
	
def add():
	print("Please enter password key: ")
	user_key = raw_input("User input: ")
	time.sleep(1)
	if user_key in exit:
		exit_pro()
	print("Please enter password: ")
	user_pass = raw_input("User input: ")
	time.sleep(1)
	if user_pass in exit:
		exit_pro()
	print("Saving new password to database...")
	time.sleep(1)
	global pass_dict
	pass_dict.setdefault(user_key, user_pass)

def main():
	while True:
		print("Please enter desired password: ")
		user_in = raw_input("User input: ")
		time.sleep(1)
		if user_in in pass_dict.keys():
			print("Password for " + user_in + ": " + pass_dict[user_in])
			time.sleep(1)
		elif user_in in exit:
			exit_pro()
		elif user_in in add_pass:
			print("Preparing to add to password list...")
			time.sleep(1)
			add()
		else:
			print("Password for " + user_in + " does not exist. Add to database?")
			user_in = raw_input("User input: ")
			time.sleep(1)
			if user_in in confirm or user_in in add_pass:
				add()
			elif user_in in no:
				print("Very well.")
				time.sleep(1)
			elif user_in in exit:
				exit_pro()
			else:
				print("Very well.")
				time.sleep(1)
		print("Would you like to continue?")
		user_in = raw_input("User input: ")
		time.sleep(1)
		if user_in in exit:
			exit_pro()

a = 0
while a < 3:
	print("Welcome to Password Loockup Database (PLD)")
	time.sleep(1)
	print("Please input master password for access: ")
	user_in = raw_input("User input: ")
	time.sleep(1)
	if user_in == password:
		print("Access granted.")
		time.sleep(1)
		print("Initiating account database lookup...")
		time.sleep(1)
		main()
	else:
		print("Access denied.")
		time.sleep(1)
		a += 1
print("Exiting system.")
time.sleep(1)
sys.exit()