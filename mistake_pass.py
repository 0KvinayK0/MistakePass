import requests as r
import hashlib as h
import sys

def request_api(_5hash):
    url = 'https://api.pwnedpasswords.com/range/' + _5hash
    # padding to increase uncertainty in the size of the response content
    padding = {'Add-Padding': 'true'}
    res = r.get(url, headers=padding)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching data: Status Code: \'{res.status_code}\', check the API and try again!')
    # print(len(res.content))
    return res

def get_password_leak_count(hashes, tail):
    hashes = (line.split(':') for line in hashes.text.splitlines() )
    for h,c in hashes:
        if h == tail:
            return c
    return 0

def pwned_pass_check(password):
    #Encode into UTF, convert to hexadecimal, and then convert to uppercase to match the hash pattern
    sha1_pwd = h.sha1(password.encode('utf-8')).hexdigest().upper()
    _5hash, tail = sha1_pwd[:5],sha1_pwd[5:]
    api_res = request_api(_5hash)
    return get_password_leak_count(api_res,tail)

def add_seperation(main):
    def wrapper_fun(*args,**kwargs):
        print('---------------START----------------------')
        main(*args,**kwargs)
        print('----------------END-----------------------')
    return wrapper_fun

@add_seperation
def main(passwords):
    for password in passwords:
        count = pwned_pass_check(password)
        if count:
            print(f'Like a secret whispered in the wind, your password \'{password}\' has been exposed \'{count}\' times, urging you to fortify your digital defenses.')
        else:
            print(f'Your password: \'{password}\', remains a fortress of digital strength, untouched and unyielding.')
    
if __name__ == '__main__':
    if len(sys.argv) > 1:
        try:
            sys.exit(main(sys.argv[1:]))
        except Exception as err:
            print(f'Error in processing arguments: str{err}')
    else:
        print('Oh dear wanderer, worried about unveiling your secret word? Fear not, for I shall patiently await your command... 🎶🎵')
