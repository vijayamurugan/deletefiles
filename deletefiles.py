#!/usr/bin/env python
import os, time, sys
import shutil

def deleteFile(days,path):
  input_args = locals()
  print("input arguments are", input_args)
  now = time.time()
  for f in os.listdir(path):
    f = os.path.join(path, f) 
    if os.stat(f).st_mtime < now - int(days) * 86400:
     print(f)
     shutil.rmtree(f)
     os.remove(f)
     os.rmdir(f)
     
     
params=sys.argv;
if len(params)>1:
 deleteFile (params[1],params[2])
else:
 print("Missing arguments. i.e days and path")
