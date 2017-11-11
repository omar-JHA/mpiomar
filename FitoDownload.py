#from picamera import PiCamera,Color
import httplib2 as http
from urlparse import urlparse
import datetime
import urllib
import json
import time

class DemoClass(object):
 pass

def MyClass(obj):
 return obj.__dict__


class FitoDownload:

 def getImageData(self, data,urlData):
  
  count=1;
  imagesList = [] 
  #now = datetime.datetime.now()
  #print now
  print data
  jsonimg = json.loads(data)
  
  for item in jsonimg:
    print item['urlImagelat']
    print item['urlImageSup']
    testfile  = urllib.URLopener()
    urlImagelat = urlData +"/dataLat" + str(count) + ".jpg";
    urlImageSup = urlData +"/dataSup" + str(count) + ".jpg";
    testfile.retrieve(item['urlImagelat'],urlImagelat )
    time.sleep(2)
    testfile.retrieve(item['urlImageSup'],urlImageSup )
    time.sleep(2)
    count = count+1;

    myImage = DemoClass()
    myImage.urlImagelat = urlImagelat
    myImage.urlImageSup = urlImageSup
    
    imagesList.append(myImage)
    #print urlImage
  json_string = json.dumps(imagesList, default=MyClass)

  #print json_string
  return json_string
