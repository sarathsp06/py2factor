# py2factor

## Usage 

```
pip install py2factor
py2factor add [--name "<name>" --key "<key/secret>"][--url <"totpurl">]   #adds a profile given (name and key) or url
py2factor profiles --filter "<prefix>"               #list all profiles 
py2factor list --filter "<prefix>"                   #list all profiles name and totp
py2factor del --name "<name>"                        #deltes a profile if presen


```

## Development

First, you need to create a virtual environment and activate it.

```

  $ pip install virtualenv
  $ virtualenv .venv
  $ . .venv/bin/activate
  (.venv)$ pip install -r requirements.txt
  (.venv)$ python setup.py install
   
```
