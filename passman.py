#!/usr/bin/python3 

import os
import json
import sys




def read_config_file():
	with open("config.json", "r") as conf_file:
		try:
			data = json.load(conf_file) 
			try:
				os.mkdir(data['store_path'])
			except FileExistsError:
				print("Storage directory " + data['store_path'] + " already exists")

			os.chdir(data['store_path'])
			return data
		except JSONDecodeError:
			print("configuration file isn't formatted correctly")


def create_folder(folder):
	try:
		os.mkdir(folder, 0o700)
	except FileExistsError:
		print("\"" + folder + "\" folder already exists")




def main():
	if len(sys.argv) < 3:
		sys.exit("Not enough arguments supplied")
	if sys.argv[1] == '-c':
		config_data = read_config_file()
		create_folder(sys.argv[2])
		create_pass(config_data['email'], sys.argv[2])
		sys.exit()
	if sys.argv[1] == '-u':
		config_data = read_config_file()
		get_pass(sys.argv[2])	



def create_pass(email, site_name):
	os.chdir(site_name)
	user = input("Website Username: ")
	password = input("Website Password: ")
	with open("temp_pass.txt", "w+") as tmp:
		tmp.write(password)
	
	command = 'gpg --encrypt -r ' + email + ' --output ' + user + '.enc temp_pass.txt' 		
	os.system(command)
	os.remove("temp_pass.txt")


def get_pass(website):
	os.chdir(website)
	user = input("Website username: ")
	command = 'gpg --decrypt ' + user + '.enc'
	output = os.popen(command).read()
	write_to_clip = 'echo ' + output + ' | xclip -l 1 -selection clipboard'
	os.system(write_to_clip)
	print("Password for " + website + " can now be pasted with Ctrl-v.\nIt will disappear after one paste.")



if __name__ == "__main__":
	print("Passman v1.0\n\nCopyright (C) 2021  Gareth Moodley") 
	main()
	
