# passman

Password manager for Linux, written in Python 3.  No external python dependencies are used.  Passwords are stored in the following hierarchy:

```
-- Website name
	|
	-- user_1.enc
	|
	-- user_2.enc
```

This layout lets you store multiple accounts for one website.
The inspiration for this project was ![`pass`](https://passwordstore.org), a shell script that encrypts passwords with the same kind of folder structure.

## Dependencies

 - `gpg`
 - `python3`
 - `xclip`

 *For development, it should be setup in a python virtualenv*
 - `python3 -m venv env`


### Configuration

Create a config file in the base directory that you want to use, and name it `config.json`.  Categories must be placed into the config file ahead of time. 

This file can also be found in ![`sample_config.json`](https://github.com/gbafana25/passman/blob/main/sample_config.json)
```json
{
	"username": "user",
	"email": "foo@bar.com",
	"store_path": "/path/to/dir",
}
```
If you want to run `passman` from anywhere, then you can:
 - add the repo directory to the `$PATH` variable
 - put it in a directory already in the path (`/usr/bin`, `/usr/local/bin/`, etc)
 - make sure that the path to the config file (found at the top of the program) is set to the absolute path




## Usage

 - to save a password
	- `./passman.py -c website_name`
	- you will be prompted to enter the username and password (it won't echo)
 - to access a password
	- `./passman.py -u website_name`
	- enter the number listed before the username
		- if you only have one account for that site, it will go straight to the password prompt
	- you will be prompted to enter your gpg password

 **Note: The default number of pastes for xclip is 3. This is required with chromium (only one that I tested other than firefox)**


## TODO

- [ ] add comments 
- [x] Make running from command line easier by adding flags and passing path to conf file
- [x] Organize passwords into files by their corresponding website, and folders of general categories
- [x] Encrypt and decrypt passwords with `gpg` (via os.system)
