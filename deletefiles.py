#!/usr/bin/env python
import os, time, sys

def deleteFile(days,path):
   print(path)
   now = time.time()
   for f in os.listdir(path):
    f = os.path.join(path, f) 
    if os.stat(f).st_mtime < now - int(days) * 86400:
     if os.path.isfile(f):
       os.remove(f)
     
params=sys.argv;
if len(params)>1:
 deleteFile (params[1],params[2])
else:
 print("Missing arguments. i.e days and path")


    