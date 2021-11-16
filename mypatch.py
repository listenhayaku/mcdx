import requests
import mycheck
import sys
import time

def writelog(msg):
    f = open("patch.log",'w')
    #string = "["+time.ctime(time.time())+"]"+"  " + msg
    f.write(msg)

if __name__ == "__main__":
    url = "http://"+sys.argv[1]+":"+sys.argv[2]+"/"
    if mycheck.run() == 1:
        payload = "?cmdline=dir"
        payload = "?cmdline=ipconfig"
        r = requests.get(url+"myweb/mcdx/index/flag/admin/ctf/temp/defense"+payload)
        print(r.text)
        #writelog(r.text)
        flag = 0
        count = 0
        for i in r.text:
            count += 1
            print("count:",count,flag,hex(ord(i)),i != '\x0D' and i != '\x0A' and i != '\x09' and i != '\x00' and i != '\x20')
            if flag == 0:
                if i == '<':
                    flag = 1
                elif i != '\x0D' and i != '\x0A' and i != '\x09' and i != '\x00' and i != '\x20':
                    print("fail")
                    exit(0)
            else:
                if i == '>':
                    flag = 0
        print("success")
