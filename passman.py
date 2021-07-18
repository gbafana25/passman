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
			os.mkdir(path, 0o600)
		except FileExistsError:
			print("\"" + path + "\" folder already exists")


def create_pass(email, categories):
	site_name = input("Name of website: ")
	password = input("Website Password: ")
	for c in categories:
		print(c)
	cat = input("Category (case sensitive): ")
	if cat not in categories:
		sys.exit("Category was not spelled correctly")
	os.chdir(cat)
	with open("temp_pass.txt", "w+") as tmp:
		tmp.write(password)
	
	command = 'gpg --encrypt -r ' + email + ' --output ' + site_name + '.enc temp_pass.txt' 		
	os.system(command)
	os.remove("temp_pass.txt")



if __name__ == "__main__":
	print("Passman v1.0")
	config_data = read_config_file()
	#create_folders(config_data['categories'])
	create_pass(config_data['email'], config_data['categories'])
	
