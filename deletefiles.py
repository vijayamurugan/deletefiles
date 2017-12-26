#!/usr/bin/env python
import os, time, sys


def deleteFile(days,path):
  input_args = locals()
  print("input arguments are", input_args)
  now = time.time()
  for root, dirs, files in os.walk(path, topdown=False):
    if os.stat(path).st_mtime < now - int(days) * 86400:
     for name in files:
        os.remove(os.path.join(root, name))
     for name in dirs:
        os.rmdir(os.path.join(root, name))
     print(os.stat(path).st_mtime)
params=sys.argv;
if len(params)>1:
 deleteFile (params[1],params[2])
else:
 print("Missing arguments. i.e days and path")
