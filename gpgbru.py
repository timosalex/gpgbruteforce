#original script:
# https://github.com/ddworken/gpgBruteForce/blob/master/gpgBruteForce.py

import hashlib,itertools
from subprocess import check_output as run
try: 
    from progress.bar import Bar
    progressBar = True
except:
    progressBar = False
import argparse

def getWordlist():
    with open("/usr/share/wordlists/rockyou.txt") as f:
        return f.read().splitlines()


def isCorrectPassword(password):
    try:
        output = run("gpg --pinentry-mode loopback --batch --yes --passphrase " + hashlib.sha256(password.encode()).hexdigest() + " -d  signal.log.gpg 2>&1", shell=True)   #shell injection potential, do not run on untrusted input
        if "decryption failed:" in output:
            return False
        else:
            return True
    except:
        return False

wordlist =getWordlist()
if progressBar: bar = Bar("Brute Forcing...", max=len(wordlist))
for part1 in wordlist:
    password="2021-05-23 " + part1
    if isCorrectPassword(password):
        if progressBar: bar.finish()
        print "The password is: " + password
        exit()
    if progressBar: bar.next()
if progressBar: bar.finish()
print "Failed to find the password, expand your wordlist and try again"
