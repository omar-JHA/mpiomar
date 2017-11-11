#from picamera import PiCamera,Color
import httplib2 as http
from urlparse import urlparse
import datetime
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from FitoEcuacion import *
import tensorflow as tf


class FitoRegLineal: 
    def getRegLineal(self,lstData):  
        myListJsonData = json.loads(lstData)
        value=1
        frecuencia=1
        vecaltura=[]#vectores empizan el primer dato en posicion vecaltura[0]
  	vecdiametro=[]
  	for item in myListJsonData:
           # print item['x'] #variable int altura de la planta
           # print item['y'] # variable int diametro de la planta
            vecaltura.append(item['x'])
            vecdiametro.append(item['y'])
            #value = value * (item['x'] + item['y']) 
        print vecaltura
        print vecdiametro 
        x_data=vecaltura
        y_data=vecdiametro
        rango=len(vecaltura)
        regre=Regresion()
        datos=regre.vectores(vecaltura,vecdiametro,frecuencia,rango) #le doy argu
	#print datos
	m=datos[0] # variable de tipo float para usar en tensorflow
	b=datos[1] # tipo float
        ################################################################

        ma=m
        ba=b
        mentero1="{0:.4}".format(ma)
        bentero1="{0:.4}".format(ba)
        print "valor de m",mentero1 
        print "valor de b",bentero1


        W=tf.Variable([m],dtype=tf.float32) 
	b=tf.Variable([b],dtype=tf.float32)
	print "w"
	print type(W)
	print "b"
	print type(b)

	#print type(x_data)
	y = W * x_data + b
	#funcion de coste ,aqui se  calula su cuadrado y se hace la media
	loss = tf.reduce_mean(tf.square(y - y_data))
	#se crea un optimizador  para ser referenciado por train  para usar un algoritmo gradiente decendiente
	optimizer = tf.train.GradientDescentOptimizer(0.1)
	train = optimizer.minimize(loss)
	
	#se inicializan variables
	init=tf.global_variables_initializer()
	#se inicializa secoion
	sess=tf.Session() 
	sess.run(init) 

	for step in xrange(8):        
            sess.run(train)
            print(step, sess.run(W), sess.run(b))
            
            ma=float(sess.run(W))
            ba=float(sess.run(b))
            mentero2="{0:.4}".format(ma)
            bentero2="{0:.4}".format(ba)
            print "mentero nuevo",mentero2
            print "bentero nuevo",bentero2

            if mentero2 != mentero1 and bentero2 != bentero1:
                print step
                break

       #Graphic display
	plt.plot(x_data, y_data, 'ro')
	plt.plot(x_data, sess.run(W) * x_data + sess.run(b))
	
	plt.title('Grafica de relacion de crecimiento')
	plt.xlabel('Altura de las plantas')
	plt.ylabel('Diametro de las plantas')
	#######################################
	#encontrar valor minimo de vector x
	xmin=min(x_data)-1
	ymin=min(y_data)-1
	#encontrar valor maximo de vector y
	xmax=max(x_data)+1
	ymax=max(y_data)+1
	plt.xlim(xmin,xmax)
	plt.ylim(ymin,ymax)
	##########################################
	#plt.xlim(-2,2)
	#plt.ylim(0.1,0.6)
	plt.savefig("/home/fitosmartplatform/modules_fitotron_full/mpi/graficas/tensor.png")
	#plt.legend()
	#plt.show()
        return value;
