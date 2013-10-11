#! /usr/bin/python
#-*- coding: utf-8 -*-
# Andrés Pinguino 2013
from pynguino import PinguinoProcessing
from time import sleep as delay
########################################################################
class MotorDC():
#----------------------------------------------------------------------
#Estado inicial
def __init__(self):
self.pinguino=PinguinoProcessing()
self.pinguino.RecursiveConect()
self.conectar()
#----------------------------------------------------------------------
#Establecemos la comunicación con Pinguino
def conectar(self):
if self.pinguino.RecursiveConect():
for i in range(25,29):              #Parte alta del puerto D como salida
self.pinguino.pinMode(i,"output")   #pinMode(pin,"output" ó "input")
self.pinguino.digitalWrite(i,0)     #Los pines del puerto en estado bajo
return
else: self.conectar()
#----------------------------------------------------------------------
#Manejo del puerto D
def puertoD(self,A,B,C,D,tiempo):
self.pinguino.digitalWrite(25,A)    #digitalWrite(pin,estado)
self.pinguino.digitalWrite(26,B)
self.pinguino.digitalWrite(27,C)
self.pinguino.digitalWrite(28,D)
delay(tiempo)
#----------------------------------------------------------------------
#Motores parados un cierto tiempo
def detenido(self,tiempo):
self.puertoD(0,0,0,0,tiempo)        #puertoD(A,B,C,D,tiempo)
#----------------------------------------------------------------------
#Se mueve hacia adelante un cierto tiempo
def atras(self,tiempo):
self.puertoD(0,1,1,0,tiempo)
 #puertoD(A,B,C,D,tiempo)
self.detenido(0.5)
#----------------------------------------------------------------------
#Se mueve hacia atras un cierto tiempo
def adelante(self,tiempo):
self.puertoD(1,0,0,1,tiempo)       #puertoD(A,B,C,D,tiempo)
self.detenido(0.5)
#----------------------------------------------------------------------
#Giro a la izquierda un cierto tiempo
def giroderecha(self,tiempo):
self.puertoD(0,1,0,1,tiempo)       #puertoD(A,B,C,D,tiempo)
self.detenido(0.5)
#----------------------------------------------------------------------
#Giro a la derecha un cierto tiempo
def giroizquierda(self,tiempo):
self.puertoD(1,0,1,0,tiempo)       #puertoD(A,B,C,D,tiempo)
self.detenido(0.5)

#----------------------------------------------------------------------

defmain():               #Subrutina principal
robot=MotorDC()          #Creación de la instancia robot
retardo=1                #Definición de una variable de tiempo en segundos
while True:              #Estructura de repetición
robot.adelante(retardo)
robot.giroizquierda(retardo)
robot.adelante(retardo)
robot.giroderecha(retardo)
robot.atras(retardo)
robot.giroizquierda(retardo)
robot.detenido(retardo)

#----------------------------------------------------------------------

if__name__=='__main__':   #Llamada a la Subrutina principal
main()





