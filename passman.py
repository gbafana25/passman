#!/usr/bin/python3 

import os
import json
import sys





def read_config_file():
	with open("config.json", "r") as conf_file:
		try:
			data = json.load(conf_file) 
			return data
		except JSONDecodeError:
			print("configuration file isn't formatted correctly")


def create_folders(folders):
	for path in folders:
		try:
			os.mkdir(path, 0o700)
		except FileExistsError:
			print("\"" + path + "\" folder already exists")




config_data = read_config_file()
create_folders(config_data['categories'])


def main():
	if len(sys.argv) < 2:
		sys.exit("Not enough arguments supplied")
	if sys.argv[1] == '-c':
		create_pass(config_data['email'], config_data['categories'])
		sys.exit()
	if sys.argv[1] == '-u':
		get_pass(config_data['categories'])		


def check_category(categories):
	for c in categories:
		print(c)
	cat = input("Category (case sensitive): ")
	if cat not in categories:
		sys.exit("Category was not spelled correctly")
	os.chdir(cat)


def create_pass(email, categories):
	site_name = input("Name of website: ")
	password = input("Website Password: ")
	check_category(categories)
	with open("temp_pass.txt", "w+") as tmp:
		tmp.write(password)
	
	command = 'gpg --encrypt -r ' + email + ' --output ' + site_name + '.enc temp_pass.txt' 		
	os.system(command)
	os.remove("temp_pass.txt")


def get_pass(categories):
	check_category(categories)
	website = input("Website Name: ")

	command = 'gpg --decrypt ' + website + '.enc | xclip -l 1 -selection clipboard'
	os.system(command)
	print("Password for " + website + " can now be pasted with Ctrl-v.\nIt will disappear after one paste.")



if __name__ == "__main__":
	print("Passman v1.0")
	main()
	
