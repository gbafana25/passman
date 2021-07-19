# passman

Password manager for Linux, written in Python 3.  Utilizes gpg and doesn't require third party libraries (yet)


## Dependencies

### GPG
 `sudo apt-get install gpg`

### Python 3
 `sudo apt-get install python3`
 
 *For development, should be setup in a python virtualenv*
 - `python3 -m venv env`

## Usage

### Configuration

Create a config file in the base directory that you want to use, and name it `config.json`.  Categories must be placed into the config file ahead of time.

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

- [ ] Make running from command line easier by adding flags and passing path to conf file
- [x] ~Organize passwords into files by their corresponding website, and folders of general categories~
- [x] ~Encrypt and decrypt passwords with `gpg` (via os.system)~
