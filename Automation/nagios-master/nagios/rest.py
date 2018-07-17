#Imports
import plyvel
from flask import Flask
from flask_restplus import Resource, Api
from globalvars import Config

app = Flask(__name__)
api = Api(app)

def open_cache(cache_path):
  from pathlib import Path
  lock=Path(Config.file_lock)
  if lock.is_file():
    return False
  else:
    return plyvel.DB(cache_path)


@api.route('/cache')
class Cache(Resource):
  def get(self):
    import os
    import subprocess
    cwd=os.getcwd()
    c = subprocess.call(["python36", cwd+"/nagios.py"])
    if c==0:
      return {"msg":"Caching complete."}
    else:
      return {"msg": "Caching results failed."}

@api.route('/today')
class Today(Resource):
  def get(self):

    db = open_cache(Config.cache_path)
    if db == False:
      return {"msg": "Caching in progress. Please retry."}

    import time
    import json

    time_midnight = time.strftime( "%m/%d/%Y" ) + " 00:00:00"
    midnight_epoch = int( time.mktime( time.strptime( time_midnight, "%m/%d/%Y %H:%M:%S" ) ) ) 
    now_epoch = int(time.time())
    d = dict()
    for i in range(midnight_epoch, now_epoch):
      t = db.get(bytes(str(i),"utf-8"))
      if t != None:
        d[str(i)]=json.loads(json.loads(t))
    return d   

@api.route('/days/<int:days>')
class Days(Resource):
  def get(self, days):
    db = open_cache(Config.cache_path)
    if db == False:
      return {"msg": "Caching in progress. Please retry."}

    from datetime import datetime, timedelta
    import time
    import json
    d = dict()
    ago = datetime.now() - timedelta(days=days)
    ts = int(ago.strftime('%s'))
    now_epoch = int(time.time())
    for i in range(ts, now_epoch):
      t = db.get(bytes(str(i),"utf-8"))
      if t != None:
        d[str(i)]=json.loads(json.loads(t))
    return d    

if __name__ == '__main__':
  app.run(host=Config.host, port=Config.port, debug=Config.debug)
