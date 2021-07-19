# passman

Password manager for Linux, written in Python 3.  No external python dependencies are used.  Passwords are stored in the following hierarchy:

```
	-- Website name
		|
		-- username.enc
```

This layout lets you store multiple accounts for one website.

## Dependencies

 - `gpg`
 - `python3`
 - `xclip`

 *For development, it should be setup in a python virtualenv*
 - `python3 -m venv env`

## Usage

 - to save a password
	- `./passman.py -c website_name`
 - to access a password
	- `./passman.py -u website_name`

### Configuration

Create a config file in the base directory that you want to use, and name it `config.json`.  Categories must be placed into the config file ahead of time. 

This file can also be found in ![sample_config.json](https://github.com/gbafana25/passman/blob/main/sample_config.json)
```json
{
	"username": "user",
	"email": "foo@bar.com",
	"store_path": "/path/to/dir",
}
```


## TODO

- [ ] add comments 
- [x] ~Make running from command line easier by adding flags and passing path to conf file~
- [x] ~Organize passwords into files by their corresponding website, and folders of general categories~
- [x] ~Encrypt and decrypt passwords with `gpg` (via os.system)~
