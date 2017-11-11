#from picamera import PiCamera,Color
import httplib2 as http
from urlparse import urlparse
import datetime
import json


class FitoWebData:

 def getDeviceData(self, cloud_api,fechaInicio,fechaFin):

  now = datetime.datetime.now()
  #print fechaInicio +" " +fechaFin

  now = str(now)

  headers = {
    'Content-Type': 'application/json'
  }
  url = cloud_api
  #path = "/getdevice?device=" + deviceid getImages?fechaInicio=2017-07-13 11:52:00&fechaFin=2017-07-14 11:52:00
  #path = "/getImages?fechaInicio="+now+"&fechaFin="+now
  path = "/getImages?fechaInicio="+fechaInicio+"&fechaFin="+fechaFin 
  target = urlparse(url+path)
  method = 'GET'
  body = ''

  #print target
  
  h = http.Http()
  response, content = h.request(
        target.geturl(),
        method,
        body,
        headers)
# assume that content is a json reply
# parse content with the json module
  #print target.geturl()
  print content

  data = json.loads(content)
  data = content
  
  #djson = json.loads(data)
  return data #['coord']