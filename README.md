![py2factor-logo](https://raw.githubusercontent.com/sarathsp06/py2factor/master/logo.png)

# py2factor
> Two Factor Authentication

Two-factor authentication (also known as 2FA) is a type (subset) of multi-factor authentication. It is a method of confirming a user's claimed identity by utilizing a combination of two different factors: 1) something they know, 2) something they have, or 3) something they are.

>  py2factor app

Two Factor authentication app for desktop (Linux). The app can be used along with other two factor applications like `authy` ,`google authenticator` etc.  Unlike the mobile two factor authenticators ,this app requires the user to read the QR given for two factor using mobile and pass the   data read from that as input to the application

## Installing / Getting started

A quick introduction of the minimal setup you need to setup and use **py2factor**

#### Installation

```shell
pip install py2factor
```

#### Usage
```
py2factor add [--name "<name>" --key "<key/secret>"][--url <"totpurl">]   #adds a profile given (name and key) or url
py2factor profiles --filter "<prefix>"               #list all profiles 
py2factor list --filter "<prefix>"                   #list all profiles name and totp
py2factor del --name "<name>"                        #deletes a profile if present
```

Here you should say what actually happens when you execute the code above.

## Developing

Here's a brief intro about what a developer must do in order to start developing
the project further:

> Make sure virtual environment is installed

```shpell
sudo pip install virtualenv
```

> Get the code from github and start hacking
```
git clone git@github.com:sarathsp06/py2factor.git
cd py2factor
virtualenv .venv
. .venv/bin/activate
pip install -r requirements.txt
python setup.py install
```

## Features

What's all the bells and whistles this project can perform?
* Manage two factor authenntication details for multiple accounts
* It can generate two factor code for any account offline  
* Can add a two factor account using the URL from QR code 
* Can add a two factor accoount using just the key 
* Can delete and list the account in different formats
* Output can be formatted in different formats so that it can be piped to other applications 

## Contributing

If you'd like to contribute, please fork the repository and use a feature
branch. Pull requests are warmly welcome.

## Licensing

The code in this project is licensed under MIT license.

