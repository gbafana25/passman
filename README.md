# passman

Password manager for Linux, written in Python 3.  Utilizes gpg and doesn't require third party libraries (yet)

**Currently if you take more than 1 attempt to input your gpg key password, the sites password won't get copied to the clipboard.**

## Dependencies

### GPG
 `sudo apt-get install gpg`

### Python 3
 `sudo apt-get install python3`
 
 *For development, it should be setup in a python virtualenv*
 - `python3 -m venv env`

## Usage

### Configuration

Create a config file in the base directory that you want to use, and name it `config.json`.  Categories must be placed into the config file ahead of time. 

This file can also be found in ![sample_config.json](https://github.com/gbafana25/passman/blob/main/sample_config.json)
```json
{
	"username": "user",
	"email": "foo@bar.com",
	"store_path": "/path/to/dir",
	"categories": ["Email", "Code"]
}
```

### Running

`python3 passman.py` or `chmod +x passman.py` and `./passman.py`
An shell alias can also be added

## TODO

- [ ] add comments and register multiple attempts to enter key password
- [x] ~Make running from command line easier by adding flags and passing path to conf file~
- [x] ~Organize passwords into files by their corresponding website, and folders of general categories~
- [x] ~Encrypt and decrypt passwords with `gpg` (via os.system)~
