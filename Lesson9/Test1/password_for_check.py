#!/usr/bin/python3

def check_passwd(password):
    pas1 = password.lower()
    s = pas1.find("password")
    if len(password) < 6 or password.isdigit() or s != -1:
        return False
    else:
        for x in password:
            if [x for x in password if x in '1234567890']:
                return True
            else:
                return False
