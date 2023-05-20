# Mistake Pass - Not a yet another password checker

_This script written in Python, is a better alternative to using the haveibeenpwned website directly. The script only sends a portion of your hashed password to the API, and vice versa, making it very difficult for someone to sniff the traffic and guess your password._

_Password leaked? Oops, this is definitely a good time to change your password._


## Features

 1. Leverages K-anonymity to ensure no interacting parties have the full information on the password. (https://www.troyhunt.com/understanding-have-i-been-pwneds-use-of-sha-1-and-k-anonymity/)
 2. Padding has been enabled to increase the response size. This padding is randomly generated to increase the uncertainty of guessing the password hash prefix. (https://www.troyhunt.com/enhancing-pwned-passwords-privacy-with-padding/)


## Drawbacks

 1. If you run this command via the command line, your password may be shown in the history or saved "somewhere" locally.
 2. If you are still concerned about point 1, please make a pull request to add functionality that reads passwords from a text file and checks them one by one.


## Installation

#### Clone the repository:
```
git clone https://github.com/0KvinayK0/MistakePass.git
```
#### Change into MistakePass directory:
```
cd MistakePass
```
#### Provide executable permission:
```
chmod +x mistake_pass.py
```


## Usage
```
python3 mistake_pass.py <password1> <password2> …. <passwordn>
```


## Examples
* Use single or double quotes to send the password literally.

![example1](https://github.com/0KvinayK0/MistakePass/assets/126001522/453da9dc-0e08-4106-906d-529051b039ad)

![example2](https://github.com/0KvinayK0/MistakePass/assets/126001522/64940f35-ff0d-404c-88eb-755076a1ef30)

