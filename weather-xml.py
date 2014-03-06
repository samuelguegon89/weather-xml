# -*- coding: utf-8 -*-

from lxml import etree
from jinja2 import Template
import webbrowser

plan=open("plantilla.html","r")
abrir=open("salida.html","w")
contador=0
provincias=["Almeria","Cadiz","Cordoba","Huelva","Jaen","Malaga","Sevilla"]
listaminima=[]
listamaxima=[]
listavelocidad=[]
listadireccion=[]

for i in provincias:
	
	obtener=etree.parse('http://api.openweathermap.org/data/2.5/weather?q=%s&mode=xml&units=metric&lang=es'% i)
	temperaturaminima=obtener.find('temperature')
	tempmin=temperaturaminima.attrib['min']
	listaminima.append(tempmin)
	
	temperaturamaxima=obtener.find('temperature')
	tempmax=temperaturamaxima.attrib['max']
	listamaxima.append(tempmax)
	
	velocidad=obtener.find('wind/speed')
	vel=velocidad.attrib['value']
	listavelocidad.append(vel)
	
	direccion=obtener.find('wind/direction')
	direc=direccion.attrib['code']
	listadireccion.append(direc)

salida = ""

for linea in plan:
	salida += linea

plantilla = Template(salida)
plantilla = plantilla.render(provincias=provincias,temperatura_minima=listaminima,temperatura_maxima=listamaxima,velocidad_vel=listavelocidad,direccion_dir=listadireccion)

abrir.write(plantilla)

webbrowser.open('salida.html')
