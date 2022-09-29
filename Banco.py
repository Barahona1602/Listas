from tkinter import filedialog
from tkinter import filedialog as fd
import xml.etree.ElementTree as ET
import numpy as np
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
    archivo = filedialog.askopenfilename(initialdir="C:/", title="abrir", filetypes=(("XML files",".XML"),("Todos los archivos",".*")))
    datos = ET.parse(archivo)
    empresa=datos.getroot()
    empresa_list=[]
    
    for k in datos.findall('empresa'):
        empresa_id=(k.attrib.get('id'))
        empresa_nombre=(k.find('nombre').text)
        empresa_abr=(k.find('abreviatura').text)
        lista_puntosa=k.find('listaPuntosAtencion')
        puntosa=[]
        escritorio=[]
        for l in lista_puntosa.findall('puntoAtencion'):
            puntosa_id=(l.attrib.get('id'))
            puntosa_nombre=(l.find('nombre').text)
            puntosa_direccion=(l.find('direccion').text)
            lista_escritorio=l.find('listaEscritorios')
            puntosa.append([puntosa_id, puntosa_nombre, puntosa_direccion])
            for m in lista_escritorio.findall('escritorio'):
                escritorio_id=(m.attrib.get('id'))
                escritorio_codigo=(m.find('identificacion').text)
                escritorio_encargado=(m.find('encargado').text)
                escritorio.append([puntosa_id, escritorio_id, escritorio_codigo, escritorio_encargado])
                

        listaempresa.insertar_empresa(empresa_id, empresa_nombre, empresa_abr, puntosa, escritorio)
    listaempresa.mostrar_empresa()
    


#Opción de salir
elif numero=="2":
    print("¡Regresa pronto! :)")
    quit()




