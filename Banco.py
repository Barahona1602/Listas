from selectors import SelectSelector
from tkinter import filedialog
from xml.dom import minidom
from tkinter import filedialog as fd
import xml.etree.ElementTree as ET
import numpy as np
from nodo import nodo
from lista_empresa import listaempresa


listaempresa=listaempresa()

#Menú principal
print("Bienvenido a esta empresa")
print("Me llamo Pablo Barahona y soy quien realizó el programa")
print("Mi curso es Introducción a la Programación 2 sección D")
print("Mi carnet es 202109715")
numero = input('Ingrese "1" si quiere ingresar sus archivos, ingrese "2" si quiere salir: ')


if numero=="1":
    print("Gracias por ingresar")
    #Abrir archivos (XML y todos los archivos)
    archivo = filedialog.askopenfilename(title="abrir", initialdir="C:/", filetypes=(("XML files",".XML"),("Todos los archivos",".*")))
    datos = minidom.parse(archivo)
    empresa = datos.getElementsByTagName('empresa')
    
    a=0
    #Leer archivo XML con dom
    for i in empresa:
        nombre = i.getElementsByTagName('nombre')
        abreviatura = i.getElementsByTagName('abreviatura')
        puntoa=datos.getElementsByTagName('puntoAtencion')
        trans=i.getElementsByTagName('listaTransacciones')
        empresa_id=(empresa[a].attributes['id'].value)
        b=0
        for j in puntoa:
            puntoa_id=(puntoa[b].attributes['id'].value)
            puntoa_nombre=j.getElementsByTagName('nombre')
            puntoa_direccion=j.getElementsByTagName('direccion')
            escritorio=j.getElementsByTagName('escritorio')
            c=0
            for k in escritorio:
                escritorio_id=(escritorio[c].attributes['id'].value)
                escritorio_identificacion=j.getElementsByTagName('identificacion')
                escritorio_encargado=j.getElementsByTagName('encargado')
                c+=1
            b+=1
        a+=1
        listaempresa.insertardata(empresa_id, nombre[0].firstChild.data, abreviatura[0].firstChild.data)
    listaempresa.mostrarempresa()
    

        
        
        # 
        # for i in puntoa:
        #     
        #     
        #     print(nombre2[0].firstChild.data)
        #     print(direccion[0].firstChild.data)
            
        # #Guardar datos en nodo
        # listasimple.siginsert(numpaciente, nombre[0].firstChild.data, edad[0].firstChild.data, periodos[0].firstChild.data, m[0].firstChild.data, orden, matriz)



#Opción de salir
elif numero=="2":
    print("¡Regresa pronto! :)")
    quit()