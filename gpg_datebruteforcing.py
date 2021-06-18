# script to brute force a password in the type of yyyy-mm-dd secret_string
# here secret_string is bigtent
# bruteforcing for date range between start and end date

import hashlib
from subprocess import check_output as run

from datetime import date, timedelta


def gpgPassword(password):
    try:
        output = run("gpg --pinentry-mode loopback --batch --yes --passphrase " + hashlib.sha256(password.encode()).hexdigest() + " -d  firefox.log.gz.gpg 2>&1", shell=True)   #shell injection potential, do not run on untrusted input
        if "decryption failed:" in output:
            return False
        else:
            return True
    except:
        return False

start_date = date(2021, 1, 1)
end_date = date(2021, 6, 6)
day_count = (end_date - start_date).days + 1
for single_date in (start_date + timedelta(n) for n in range(day_count)):
    password=single_date.strftime("%Y-%m-%d") + " bigtent"
    if gpgPassword(password):
        print "Found it: " + password
        exit()
