from tkinter import filedialog
from tkinter import filedialog as fd
from types import NoneType
import xml.etree.ElementTree as ET
import numpy as np
from lista_empresa import listaempresa
from lista_trans import listatrans


listaempresa=listaempresa()
listatrans=listatrans()



def compile():
    #Menú principal
    print("Bienvenido a esta empresa")
    print("Me llamo Pablo Barahona y soy quien realizó el programa")
    print("Mi curso es Introducción a la Programación 2 sección D")
    print("Mi carnet es 202109715")
    pedirNumeroEntero()


#Método para cargar archivo y leerlo
def cargararchivo():
    #Abrir archivos (XML y todos los archivos)
    archivo = filedialog.askopenfilename(initialdir="C:/", title="abrir", filetypes=(("XML files",".XML"),("Todos los archivos",".*")))
    datos = ET.parse(archivo)
    
    for k in datos.findall('empresa'):
        empresa_id=(k.attrib.get('id'))
        empresa_nombre=(k.find('nombre').text)
        empresa_abr=(k.find('abreviatura').text)
        lista_puntosa=k.find('listaPuntosAtencion')
        lista_trans=k.find('listaTransacciones')
        puntosa=[]
        escritorio=[]
        trans=[]
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
        for n in lista_trans.findall('transaccion'):
            trans_id=(n.attrib.get('id'))
            trans_nombre=(n.find('nombre').text)
            trans_tiempo=(n.find('tiempoAtencion').text)
            trans.append([trans_id, trans_nombre, trans_tiempo])
                
        #Agregar datos al nodo a través de la lista
        listaempresa.insertar_empresa(empresa_id, empresa_nombre, empresa_abr, puntosa, escritorio, trans)
    # #llamar método para imprimir lista
    # listaempresa.mostrar_empresa()



def agregarempresa():
    empresa_id=input("Ingrese el id de la empresa: ")
    empresa_nombre=input("Ingrese el nombre de la empresa: ")
    empresa_abr=input("Ingrese la abreviatura de la empresa: ")
    puntosa=[]
    escritorio=[]
    trans=[]
    num=(input("Desea agregar un punto de atención? \n 1.Si \n 2.No \n Seleccione un número: "))
    while num=="1":
        puntosa_id=input("Ingrese el id del Punto de Atención: ")
        puntosa_nombre=input("Ingrese el nombre del Punto de Atención: ")
        puntosa_direccion=input("Ingrese la dirección del Punto de Atención: ")
        puntosa.append([puntosa_id, puntosa_nombre, puntosa_direccion])
        num2=(input("Desea agregar un escritorio? \n 1.Si \n 2.No \n Seleccione un número: "))
        num="0"
        while num2=="1":
            escritorio_id=input("Ingrese el id del escritorio: ")
            escritorio_codigo=input("Ingrese el código del escritorio: ")
            escritorio_encargado=input("Ingrese el encargado del escritorio: ")
            escritorio.append([puntosa_id, escritorio_id, escritorio_codigo, escritorio_encargado])
            num2=(input("Desea agregar otro escritorio? \n 1.Si \n 2.Agregar transacciones \n Seleccione un número: "))
            if num2=="2":
                num3="1"
                
        while num3=="1":
            trans_id=input("Ingrese el id de la transaccion: ")
            trans_nombre=input("Ingrese el nombre de la transaccion: ")
            trans_tiempo=input("Ingrese el tiempo de la transaccion: ")
            trans.append([trans_id, trans_nombre, trans_tiempo])
            num3=(input("Desea agregar otra transacción? \n 1.Si \n 2.Agregar otro punto de atención \n 3.Agregar otra empresa \n 4.Terminar registro \n Seleccione un número: "))

            if num3=="3":
                listaempresa.insertar_empresa(empresa_id, empresa_nombre, empresa_abr, puntosa, escritorio, trans)
                agregarempresa()
                
            if num3=="4":
                listaempresa.insertar_empresa(empresa_id, empresa_nombre, empresa_abr, puntosa, escritorio, trans)
                    
     
def insertar_trans():
    #Abrir archivos (XML y todos los archivos)
    archivo = filedialog.askopenfilename(initialdir="C:/", title="abrir", filetypes=(("XML files",".XML"),("Todos los archivos",".*")))
    datos = ET.parse(archivo)
    
    for k in datos.findall('configInicial'):
        config_id=(k.attrib.get('id'))
        config_idE=(k.attrib.get('idEmpresa'))
        config_idP=(k.attrib.get('idPunto'))
        escritorio_act=k.find('escritoriosActivos')
        escritorio=[]
        transaccion=[]
        cantidad=[]
        for m in escritorio_act.findall('escritorio'):
            escritorio_id=(m.attrib.get('idEscritorio'))
            escritorio.append([escritorio_id])
        clientes_list=k.find('listadoClientes')
        for n in clientes_list.findall('cliente'):
            cliente_dpi=(n.attrib.get('dpi'))
            cliente_nombre=(n.find('nombre').text)
            trans_list=n.find('listadoTransacciones')
            for l in trans_list.findall('transaccion'):
                trans_id=l.attrib.get('idTransaccion')
                trans_cantidad=l.attrib.get('cantidad')
                transaccion.append([trans_id])
                cantidad.append([trans_cantidad])

        #Agregar datos al nodo a través de la lista
        listatrans.insertar_trans(config_id, config_idE, config_idP, escritorio, cliente_dpi, cliente_nombre, transaccion, cantidad)
    # listaempresa.mostrar_empresa()


def pedirempresa():
    listaempresa.mostrar_empresa2()
    busqueda=input("Seleccione una empresa por id: ")
    listaempresa.empresaseleccionada(busqueda)
    







def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            print("- - - - - - - - - - - MENU - - - - - - - - - - -")
            print("1. Limpiar Sistema")
            print("2. Cargar archivo de configuración del sistema")
            print("3. Crear nueva empresa")
            print("4. Cargar archivo inicial de prueba")
            print("5. Ver datos de empresas")
            print("6. Ver listado de clientes")
            print("7. Seleccionar empresa")
            
            print ("Elige una opcion")
            num = int(input("Introduce un número: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     


    salir = False
    opcion = 0

    while not salir:

        opcion = num
    
        if opcion == 1:
            print("Limpiando Sistema...")
            listaempresa.eliminardatos()
            pedirNumeroEntero()
        elif opcion == 2:
            print("Leyendo archivos...")
            cargararchivo()
            print("Archivos cargados exitosamente")
            pedirNumeroEntero()
        elif opcion == 3:
            print("Creando empresa...")
            agregarempresa()
            pedirNumeroEntero()
        elif opcion == 4:
            print("Cargando archivos...")
            insertar_trans()
            print("Archivos cargados exitosamente")
            pedirNumeroEntero()
        elif opcion == 5:
            print("Cargando empresa...")
            listaempresa.mostrar_empresa()
            pedirNumeroEntero()
        elif opcion==6:
            print("Cargando clientes...")
            listatrans.mostrar_trans()
            pedirNumeroEntero()
        elif opcion ==7:
            print("Cargando empresa...")
            pedirempresa()
            pedirNumeroEntero()
        else:
            print ("Introduce un numero entre 1 y 7")

compile()





