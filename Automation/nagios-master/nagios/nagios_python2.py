
#Setting up global imports
import plyvel
import json
from globalvars import Config

#Setting up variables
cache_path=Config.cache_path
service_data_perf=Config.service_data_perf
host_data_perf=""
file_lock=Config.file_lock
delta=10

#Run checks and create cache
cache = plyvel.DB(cache_path,create_if_missing=True)

from pathlib import Path
lock=Path(file_lock)
if lock.is_file():
  print("Lock obtained.")
else:
  print("Creating lock file.")
  open(file_lock, 'a').close()


def b(val):
  return bytes(val.encode("utf-8"))

def write_cache(key, var, cache):
  t = json.dumps(var)
  cache.put(b(key), b(json.dumps(t)))
  print(cache.get(b(key)))

def del_lock(file_lock):
  import os
  os.remove(file_lock)
  print("Lock released")

def truncatel(filename):
  f = open(filename, "w")
  f.truncate(0)

def check_record(timestamp, cache):
  t = cache.get(b(timestamp))
  if t == None:
    return t
  else:
    return json.loads(json.loads(t))

def process_lines(lines, cache):
  pruned = list(filter(None, lines))
  for line in pruned:
    temp1=None
    temp = line.split("\t")
    d = { "hostname" : temp[2],
      "servicedesc" : temp[3],
      "serviceexec" : temp[4],
      "servicelate" : temp[5],
      "serviceop" : temp[6],
      "serviceperf" : temp[7]
    }
    temp1 = check_record(temp[1], cache)
    
    if temp1 != None:
      temp1[temp[1]].append(d)
    else:
      temp1 = dict()
      temp1[temp[1]] = [d]
    write_cache(temp[1], temp1, cache)

from itertools import izip_longest

def grouper(iterable, n, fillvalue=None):
  args = [iter(iterable)] * n
  return izip_longest(*args, fillvalue=fillvalue)

def process_perfdata(filename, cache, delta):
  with open(filename, 'r') as infile:
    for lines in grouper(infile, delta, ''):
      process_lines(lines, cache)

process_perfdata(service_data_perf, cache, delta)
cache.close()
del_lock(file_lock)
truncatel(service_data_perf)
