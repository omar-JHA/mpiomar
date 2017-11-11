from FitoDownload import *
from FitoWebData import *
from FitoConfig import *
from FitoMpiProcess import *
from FitoRegLineal import *

class DemoClass(object):
 pass

def MyClass(obj):
 return obj.__dict__

class FitoMpi:

 def runMpi(self,webApi,fechaInicio,fechaFin,urlData):

    #mySend = FitoDownload()
    #myData = mySend.sendData(ip, lat, lng);
     myDeviceData = FitoWebData();
        
     myDevData = myDeviceData.getDeviceData(webApi,fechaInicio,fechaFin);
     data =  myDevData


     myDownloadData = FitoDownload();
     myListData = myDownloadData.getImageData(data,urlData);
    
     #myListProcess =


     valuesList = []
     #convert string in json
     myListJsonData = json.loads(myListData) 
     #print myListJsonData
     for item in myListJsonData:
     	myProcess  = FitoMpiProcess()
        valueX=0
        valueY=0
        
     	valueX = myProcess.getMetricLateral(item['urlImagelat'])
        print valueX
     	 
     	valueY = myProcess.getMetricSuperior(item['urlImageSup'])
        print valueY

        myValue = DemoClass()
        myValue.x = valueX
        myValue.y = valueY
        valuesList.append(myValue)
        #print urlImage
     json_string = json.dumps(valuesList, default=MyClass)
     #print json_string

     myRegLinealData = FitoRegLineal();
     myReqLineal = myRegLinealData.getRegLineal(json_string);
     print myReqLineal

	


    

def main():
    print "init ..."
    myFitoConfig = FitoConfig();
    myData = myFitoConfig.getConfigData();    
    print myData
    cloud_api = myData['cloud_api'];
        

    print "running main..."
    myMpi = FitoMpi()
    webApi = cloud_api
    fechaInicio = "2017-10-22%2011:52:00"
    fechaFin = "2017-10-25%2011:59:00"
    urlData = "/home/fitosmartplatform/modules_fitotron_full/mpi/data"
    myMpi.runMpi(webApi,fechaInicio,fechaFin,urlData)
 	#runMai(ip, lat, lng)

if __name__ == "__main__":
	print 'running by itself ...'
 	main()
else:
	print 'running imported by another module' 
