#from picamera import PiCamera,Color
import httplib2 as http
from urlparse import urlparse
import datetime
import json
#analysis libraries
import cv2
import plantcv as pcv
import numpy as np
from time import sleep

class FitoMpiProcess:
 
 

 def getMetricLateral(self,urlImage):
  #value=1;
  self.r=urlImage
  
  ##############################################################33
  img, path, filename = pcv.readimage(urlImage) #chekar si recibe ulr (string) o (int)
  img=img[120:360,160:460] # recorte del codigo de barras
  cv2.imwrite("recorte.jpg",img)# guarda imagen recortada
  sleep(1) #tiempo de espera
  img=cv2.imread("recorte.jpg",1)#lee imagen recortada
   #datos necesarios para usar plantcv
  device = 0
  debug=None
  # Classify the pixels as plant or background
  device,mask = pcv.naive_bayes_classifier(img, pdf_file="/home/fitosmartplatform/plantCV/codigos/lateral/naive_bayes_pdfs.txt", device=0, debug="print")
  kept_mask=cv2.imread("1_naive_bayes_plant_mask.jpg",0)

  ##########################################GET THE HEIGHT OF THE PLANT ##################################33        
  contornos, hierarchy = cv2.findContours(kept_mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
  #cv2.drawContours(img,contornos,-1,(0,0,255),5)   # draws the outer contour of the image
  areas=[cv2.contourArea(temp) for temp in contornos]
  max_index=np.argmax(areas)
  largest_contour=contornos[max_index]
  ################## Applying the boundary proximity theorem ##################
  approx=cv2.approxPolyDP(largest_contour,0.01*cv2.arcLength(largest_contour,True),True)
  hull=cv2.convexHull(approx,returnPoints=True)
  x,y,width,heigth=cv2.boundingRect(largest_contour)
  cv2.rectangle(img,(x,y),(x+width,y+heigth),(0,255,0),2) 
  ######## Measure of an object set at 25 cm distance #####################
  EcHeigth = int ( (1*heigth) / 27 )
  cv2.putText(img,"Altura :"+str(EcHeigth) +"cm",(x,y),cv2.FONT_HERSHEY_DUPLEX,0.5,(0,0,0))
  ##################################################################
  value=EcHeigth
  #value=1
  return value; ##RETORNA VALOR INT

 def getMetricSuperior(self,urlImage):
  #value=2;
  self.r=urlImage
  #value=2;
  ############################################################################3
  img, path, filename = pcv.readimage(urlImage)
  device = 0
  debug=None
  # Classify the pixels as plant or backgroun
  device,mask = pcv.naive_bayes_classifier(img, pdf_file="/home/fitosmartplatform/plantCV/codigos/superior/naive_bayes_pdfs.txt", device=0, debug="print")
  kept_mask=cv2.imread("1_naive_bayes_plant_mask.jpg",0)
  contornos, hierarchy = cv2.findContours(kept_mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
  #cv2.drawContours(img,contornos,-1,(0,0,255),5)
  # dibuja el contorno externo de la imagen
  areas=[cv2.contourArea(temp) for temp in contornos] #busca el are de contornos encontrados en la planta
  max_index=np.argmax(areas)
  largest_contour=contornos[max_index]
  ################## aplicando teorema de aproximidad de contorno ##################
  approx=cv2.approxPolyDP(largest_contour,0.01*cv2.arcLength(largest_contour,True),True)
  #parametros son 3 ya estan
  hull=cv2.convexHull(approx,returnPoints=True)#muestra los contornos del objeto(xy)
  x,y,width,heigth=cv2.boundingRect(largest_contour) # encunetra contornos para crear un rectangulo
  cv2.rectangle(img,(x,y),(x+width,y+heigth),(0,255,0),2) #encierra borde de objeto en rectangulo
  EcWidth  = int ( (1*width) / 27 )
  cv2.putText(img,"Diametro :"+str(EcWidth) +"cm",(x,y),cv2.FONT_HERSHEY_DUPLEX,0.5,(0,0,0))
  #############################################################################
  value=EcWidth
  #value=2	
  return value #RETORNA VALOR INT	
