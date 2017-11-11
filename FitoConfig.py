import json


class FitoConfig:

 def getConfigData(self):

  url = "device.config"
  
  #print url
  
  with open(url) as f:
    content = f.read()
  
# assume that content is a json reply
# parse content with the json module
  #print content
  data = json.loads(content)
  #print data
  #djson = json.loads(data)
  return data #['coord']