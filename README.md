# py2factor

##Usage 

```
pip install py2factor
py2factor add --name "<name>" --key "<key/secret>"   #adds a profile
py2factor profiles --filter "<prefix>"               #list all profiles and its current totp

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
