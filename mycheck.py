# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 09:36:54 2021

@author: user
"""
import requests
import time
import sys

def writelog(msg):
    f = open("check.log",'a')
    string = "["+time.ctime(time.time())+"]"+"  " + msg
    f.write(string)
    
def run(): 
    url = "http://"+sys.argv[1]+":"+sys.argv[2]+"/"
    try:
        r = requests.post(url)
    except:
        writelog(url+" timeout\n")
        return 0
    print("r.status_code: ",r.status_code)
    if r.status_code >= 200 and r.status_code <= 399:
        writelog(url+" is alive\n")
        return 1
    else:
        writelog(url+" code:"+str(r.status_code)+"\n")
        return 0
    
    
if __name__ == "__main__":
    ret = run()
    print(ret)
    exit(ret)