#!/usr/bin/env python

__author__ = "BoscoTsang"

import hashlib
import getpass

def genhash():
    while(True):
        domain = raw_input("Input your website domain:\n")
        print "Your website domain is: ", domain
        print "Enter your password"
        pwd = getpass.getpass()
        print "Confirm your password"
        ver_pwd = getpass.getpass()
        if pwd != ver_pwd:
            print "Error, reenter your password"
        salt = raw_input("Input the salt or press enter to skip")
        return hashlib.md5(salt+domain+pwd).hexdigest()

def mapping(s):
    s = "".join([chr(int(int(s[i*2: (i+1)*2], 16)/256. * 75 + 48)) for i in xrange(16)])
    return s if not s.endswith(' ') else s[:-1] + '/'

def main():
    print mapping(genhash())

if "__main__" == __name__:
    main()
