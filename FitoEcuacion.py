import math

class Regresion:

    def vectores(self,veclateral,vecsuperior,frecuencia,rango):
        #operaciones#
        self.a=veclateral
        self.b=vecsuperior
        self.c=frecuencia
        self.d=rango
        print "FitoEcuacion"
        #print veclateral 
        #print vecsuperior

######### realizar formula de ecuacion de egresion ################33
#valores
#
#N=numero de muestras x and y
#media de x=sumatorai de vector altura y dividida entre N
#media de y=sumatoria de vector de diametro y dividida entre N
#VARIANZA DE X SUMATORIA DE X POR FRECUENCIA SOBRE N MENOS LA MEDIA DE X
#COBARIANZA SUMATORIA DE X *Y *FRECUENCIA DIVIDIDO ENTRE N MENOS LAS DOS MEDIAS MULTIPLICADAS
#
#
#
#
#media de x#
        rango=len(veclateral)
        sumax=0
        for a in veclateral:
            sumax += int(a)
        sumax=sumax/float(rango)
        #print "media de x :"+str(sumax)
        mediax=float(sumax)
#media de y
        sumay=0
        for a in vecsuperior:
            sumay += int(a)
        sumay=sumay/float(rango)
        #print "media de y :"+str(sumay)
        mediay=float(sumay)
################### varianza ########

        def cuadrado(numero):  #valores de x**2
            numero=int(numero)    
            numero=numero**2
            return numero
        lista2 =map(cuadrado, veclateral)
        #print lista2
        sumax=0 #media de x**2

        for a in lista2:
            sumax += int(a)*frecuencia
        sumax=sumax/float(rango)
        #print "media de x**2 :"+str(sumax)
        varianza=sumax-(mediax**2) #VARIANZA (SUMA**2*F/N) -MEDIA DE X
        #print "la varianza x es : "+str(varianza)
        varianza=float(varianza)
#################### covarianza
        dosmediasmul=mediax*mediay
        #print "multiplicacion de medias "+str(dosmediasmul)
        dosmediasmul=float(dosmediasmul)
        def operador(n,m): # sumo vetores de lista x and y 
            n=int(n)
            m=int(m)
            return n*m
#print veclateral
#print vecsuperior
        lista_suma = map(operador,veclateral,vecsuperior)
        #print lista_suma

        mediadsumas=0 #saco media de vector de sumas
        for a in lista_suma:
            mediadsumas += int(a)*frecuencia
        mediadsumas=mediadsumas/float(rango)
        #print "media de x :"+str(mediadsumas)
        mediadsumas=float(mediadsumas)
        covarianza=mediadsumas-dosmediasmul
        #print "la covarianza es: "+ str(covarianza)
        covarianza=float(covarianza)
        if varianza == 0.0 or covarianza == 0.0:
            m=float(1)
            b=float(1)
           #print " valores de varianza y covarianza es igual a cero"
################### ECUACION DE REGRESION ############3333
# rango tipo int
# mediax tipo float
# mediay tipo float
# varianza tipo float
# covarianza tipo float

#y-mediay=(varianza/covarianza)(x-mediax)

#y=(varianza/covarianza)x +(-(varianza/covarianza)mediax+mediay)
        if varianza !=0.0 and covarianza !=0.0:
            m=float(covarianza/varianza) 
    	    b=float(((covarianza/varianza)*-mediax)+mediay)
    	print "y   =   mx  + b  "
    	print "y = "+str(m)+" x (+/-) "+str(b)
        return m,b

