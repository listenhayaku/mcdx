import requests
import sys
import time
import random

def writelog(url,msg):
    f = open("/var/log/dirb_script/patch.log",'a')
    string = "["+time.ctime(time.time())+"] "+ url + msg
    f.write(string)

def connect(url):
	try:
		r = requests.post(url)
	except:
		writelog(url," timeout\n")
		return 0

	if r.status_code >= 200 and r.status_code <= 399:
		return 1
	else:
		return 0
	

def run(url):
	if connect(url) == 1:
		payload = ["ls","pwd","ip a","whoami","who","last","date"]
		payload = "?cmdline="+payload[random.randint(0,len(payload) - 1)]
		url += payload
		r = requests.get(url)
		print(r.text)
		#writelog(r.text)
		flag = 0
		count = 0
		for i in r.text:
			count += 1
			#print("count:",count,flag,hex(ord(i)),i != '\x0D' and i != '\x0A' and i != '\x09' and i != '\x00' and i != '\x20')
			if flag == 0:
				if i == '<':
				    flag = 1
				elif i != '\x0D' and i != '\x0A' and i != '\x09' and i != '\x00' and i != '\x20':	#the response shows something
				    print("patch fail")
				    writelog(url," vulnerability is exist\n")
				    return 0
			else:
				if i == '>':
				    flag = 0
		print("patch successful")	#the response doesn't show something
		writelog(url," vulnerability is not exist\n")
		return 1
	else:
		writelog(url," can\'t find the page\n")
		return 1


if __name__ == "__main__":
	url = "http://"+sys.argv[1]+":"+sys.argv[2]+"/"+"myweb/mcdx/index/flag/admin/ctf/temp/defense"
	ret = run(url)
	print(ret)
	exit(ret)
