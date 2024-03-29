from nodo import nodo
import numpy as np
import xml.etree.cElementTree as ET


class listaempresa():
    def __init__(self):
        self.primero=None
        self.ultimo= None
        self.size = 0
        


    def insertar_empresa(self, idE, nombre, abreviatura, lista_puntosa, lista_escritorio, lista_trans):
        global empresa_data
        empresa_data= nodo(dato=[idE, nombre, abreviatura, lista_puntosa, lista_escritorio, lista_trans])
        self.size += 1
        if self.primero is None:
            self.primero = empresa_data
            self.ultimo= empresa_data
        else:
            tmp = self.primero
            while tmp.getsiguiente() is not None:
                tmp=tmp.getsiguiente()
            tmp.setsiguiente(empresa_data)
    
    


    
    def mostrarinicio(self):
        tmp = self.primero
        while tmp is not None:
            print("- - - - - - - - - - - - - - - - - - - - - - - - -")
            print("--EMPRESA--")
            print("ID: ", tmp.dato[0])
            print("Nombre: ", tmp.dato[1])
            print("Abreviación: ", tmp.dato[2])
            numeracion_puntoa=0
            for i in tmp.dato[3]:
                print("--PUNTO DE ATENCIÓN--")
                print("ID: ", tmp.dato[3][numeracion_puntoa][0])
                print("Nombre: ", tmp.dato[3][numeracion_puntoa][1])
                print("Direccion: ", tmp.dato[3][numeracion_puntoa][2])
                numeracion_puntoa+=1
            tmp=tmp.getsiguiente()



    #Método para imprimir lista
    def mostrar_empresa(self):
        tmp = self.primero
        while tmp is not None:
            print("- - - - - - - - - - - - - - - - - - - - - - - - -")
            print("--EMPRESA--")
            print("ID: ", tmp.dato[0])
            print("Nombre: ", tmp.dato[1])
            print("Abreviación: ", tmp.dato[2])
            numeracion_puntoa=0
            for i in tmp.dato[3]:
                print("--PUNTO DE ATENCIÓN--")
                print("ID: ", tmp.dato[3][numeracion_puntoa][0])
                print("Nombre: ", tmp.dato[3][numeracion_puntoa][1])
                print("Direccion: ", tmp.dato[3][numeracion_puntoa][2])
                print("--ESCRITORIOS--")
                numeracion_esc=0
                for i in tmp.dato[4]:
                    if tmp.dato[4][numeracion_esc][0]!=tmp.dato[3][numeracion_puntoa][0]:
                        numeracion_esc+=1
                    else:
                        while tmp.dato[4][numeracion_esc][0]==tmp.dato[3][numeracion_puntoa][0]:
                            print("ID: ", tmp.dato[4][numeracion_esc][1])
                            print("Código: ", tmp.dato[4][numeracion_esc][2])
                            print("Nombre: ", tmp.dato[4][numeracion_esc][3])
                            if tmp.dato[4][numeracion_esc][4]==True:
                                print("Estado de escritorio:  ACTIVO")
                            else:
                                print("Estado de escritorio:  INACTIVO")
                            numeracion_esc+=1
                            break
                numeracion_puntoa+=1
            numeracion_trans=0
            for i in tmp.dato[5]:
                print("-- TRANSACCIONES --")
                print("ID: ", tmp.dato[5][numeracion_trans][0])
                print("Nombre: ", tmp.dato[5][numeracion_trans][1])
                print("Tiempo de duración: ", tmp.dato[5][numeracion_trans][2])
                numeracion_trans+=1
            print("- - - - - - - - - - - - - - - - - - - - - - - - -")
            tmp=tmp.getsiguiente()
        print(f"Empresas creadas: {self.size}")


    def mostrartrans(self, idE, idP):
        tmp = self.primero
        numeracion_puntoa2=0
        while tmp is not None:
            if idE != tmp.dato[0]:
                tmp=tmp.getsiguiente()
            else:
                while idP != tmp.dato[3][numeracion_puntoa2][0]: #tmp.dato[3] son los puntos de atención
                    numeracion_puntoa2+=1
                else:
                    numeracion_trans=0
                    print("-- TRANSACCIONES --")
                    for i in tmp.dato[5]:
                        print("ID: ", tmp.dato[5][numeracion_trans][0])
                        print("Nombre: ", tmp.dato[5][numeracion_trans][1])
                        print("Tiempo de duración: ", tmp.dato[5][numeracion_trans][2])
                        numeracion_trans+=1
                    print("- - - - - - - - - - - - - - - - - - - - - - - - -")
                    break





    #Método para imprimir lista
    def mostrar_empresa2(self):
        tmp = self.primero
        while tmp is not None:
            print("- - - - - - - - - - - - - - - - - - - - - - - - -")
            print("--EMPRESA--")
            print("ID: ", tmp.dato[0])
            print("Nombre: ", tmp.dato[1])
            print("Abreviación: ", tmp.dato[2])
            tmp=tmp.getsiguiente()




    def eliminardatos(self):
        if self.size>0:
            self.primero=None
            self.ultimo= None
            self.size=0
            print(f"Empresas creadas: {self.size}")


    def imprimir(self):
        tmp = self.primero
        while tmp is not None:
            print(tmp.dato)
            tmp=tmp.getsiguiente()
            


    def empresaseleccionada(self, bus):
            tmp = self.primero
            numeracion_puntoa2=0
            while tmp is not None:
                if bus != tmp.dato[0]:
                    tmp=tmp.getsiguiente()
                else:
                    print("- - - - - - - EMPRESA SELECCIONADA - - - - - - -")
                    print("ID: ", tmp.dato[0])
                    print("Nombre: ", tmp.dato[1])
                    print("Abreviación: ", tmp.dato[2])
                    numeracion_puntoa=0
                    for i in tmp.dato[3]:    
                        print("ID: ", tmp.dato[3][numeracion_puntoa][0])
                        print("Nombre: ", tmp.dato[3][numeracion_puntoa][1])
                        print("Direccion: ", tmp.dato[3][numeracion_puntoa][2])
                        numeracion_puntoa+=1
                    print("- - - - - - - - - - - - - - - - - - - - - - - - -")
                    punto=input("Seleccione su punto de atención: ")
                    while punto != tmp.dato[3][numeracion_puntoa2][0]:
                        numeracion_puntoa2+=1
                    else:
                        print("- - - - - - - - - - - - - - - - - - - - - - - - -")
                        print("-- PUNTO DE ATENCIÓN SELECCIONADO --")
                        print("ID: ", tmp.dato[3][numeracion_puntoa2][0])
                        print("Nombre: ", tmp.dato[3][numeracion_puntoa2][1])
                        print("Direccion: ", tmp.dato[3][numeracion_puntoa2][2])
                        print("-- ESCRITORIOS --")
                        numeracion_esc=0
                        for i in tmp.dato[4]:
                            if tmp.dato[4][numeracion_esc][0]!=tmp.dato[3][numeracion_puntoa2][0]:
                                numeracion_esc+=1
                            else:
                                while tmp.dato[4][numeracion_esc][0]==tmp.dato[3][numeracion_puntoa2][0]:
                                    print("ID: ", tmp.dato[4][numeracion_esc][1])
                                    print("Código: ", tmp.dato[4][numeracion_esc][2])
                                    print("Nombre: ", tmp.dato[4][numeracion_esc][3])
                                    if tmp.dato[4][numeracion_esc][4]==True:
                                        print("Estado de escritorio:  ACTIVO")
                                    else:
                                        print("Estado de escritorio:  INACTIVO")
                                    numeracion_esc+=1
                                    break
                    break





    def empresaseleccionada2(self, bus, punto):
            tmp = self.primero
            numeracion_puntoa2=0
            while tmp is not None:
                if bus != tmp.dato[0]:
                    tmp=tmp.getsiguiente()
                else:
                    print("- - - - - - - EMPRESA SELECCIONADA - - - - - - -")
                    print("ID: ", tmp.dato[0])
                    print("Nombre: ", tmp.dato[1])
                    print("Abreviación: ", tmp.dato[2])
                    while punto != tmp.dato[3][numeracion_puntoa2][0]: #tmp.dato[3] son los puntos de atención
                        numeracion_puntoa2+=1
                    else:
                        print("- - - - - - - - - - - - - - - - - - - - - - - - -")
                        print("- - - - - PUNTO DE ATENCIÓN SELECCIONADO - - - - -")
                        print("ID: ", tmp.dato[3][numeracion_puntoa2][0])
                        print("Nombre: ", tmp.dato[3][numeracion_puntoa2][1])
                        print("Direccion: ", tmp.dato[3][numeracion_puntoa2][2])
                        print("-- ESCRITORIOS --")
                        numeracion_esc=0
                        for i in tmp.dato[4]:
                            if tmp.dato[4][numeracion_esc][0]!=tmp.dato[3][numeracion_puntoa2][0]:
                                numeracion_esc+=1
                            else:
                                #Comparo el id conectado de los escritorios con los id del punto de atención
                                while tmp.dato[4][numeracion_esc][0]==tmp.dato[3][numeracion_puntoa2][0]: #tmp.dato[4] son los escritorios
                                    print("ID: ", tmp.dato[4][numeracion_esc][1])
                                    print("Código: ", tmp.dato[4][numeracion_esc][2])
                                    print("Nombre: ", tmp.dato[4][numeracion_esc][3])
                                    if tmp.dato[4][numeracion_esc][4]==True:
                                        print("Estado de escritorio:  ACTIVO")
                                    else:
                                        print("Estado de escritorio:  INACTIVO")
                                    numeracion_esc+=1
                                    break
                    break

    def activarescritorios(self,bus,punto, escritorios):
        tmp = self.primero
        numeracion_puntoa2=0
        while tmp is not None:
            if bus != tmp.dato[0]:
                tmp=tmp.getsiguiente()
            else:
                while punto != tmp.dato[3][numeracion_puntoa2][0]: #tmp.dato[3] son los puntos de atención
                    numeracion_puntoa2+=1
                else:
                    numeracion_esc=0
                    for i in tmp.dato[4]:
                        if tmp.dato[4][numeracion_esc][0]!=tmp.dato[3][numeracion_puntoa2][0]:
                            numeracion_esc+=1
                        else:
                            #Comparo el id conectado de los escritorios con los id del punto de atención
                            while tmp.dato[4][numeracion_esc][0]==tmp.dato[3][numeracion_puntoa2][0]: #tmp.dato[4] son los escritorios
                                while tmp.dato[4][numeracion_esc][1]==escritorios:
                                    tmp.dato[4][numeracion_esc][4]=True
                                    break
                                numeracion_esc+=1
                                break
                                
                break
        
    def escritoriosa(self, bus):
            tmp = self.primero
            numeracion_puntoa2=0
            while tmp is not None:
                if bus != tmp.dato[0]:
                    tmp=tmp.getsiguiente()
                else:
                    print("- - - - - - - EMPRESA SELECCIONADA - - - - - - -")
                    print("ID: ", tmp.dato[0])
                    print("Nombre: ", tmp.dato[1])
                    print("Abreviación: ", tmp.dato[2])
                    numeracion_puntoa=0
                    for i in tmp.dato[3]:    
                        print("ID: ", tmp.dato[3][numeracion_puntoa][0])
                        print("Nombre: ", tmp.dato[3][numeracion_puntoa][1])
                        print("Direccion: ", tmp.dato[3][numeracion_puntoa][2])
                        numeracion_puntoa+=1
                    print("- - - - - - - - - - - - - - - - - - - - - - - - -")
                    punto=input("Seleccione su punto de atención: ")
                    while punto != tmp.dato[3][numeracion_puntoa2][0]:
                        numeracion_puntoa2+=1
                    else:
                        print("- - - - - - - - - - - - - - - - - - - - - - - - -")
                        print("-- PUNTO DE ATENCIÓN SELECCIONADO --")
                        print("ID: ", tmp.dato[3][numeracion_puntoa2][0])
                        print("Nombre: ", tmp.dato[3][numeracion_puntoa2][1])
                        print("Direccion: ", tmp.dato[3][numeracion_puntoa2][2])
                        print("-- ESCRITORIOS --")
                        numeracion_esc=0
                        for i in tmp.dato[4]:
                            if tmp.dato[4][numeracion_esc][0]!=tmp.dato[3][numeracion_puntoa2][0]:
                                numeracion_esc+=1
                            else:
                                while tmp.dato[4][numeracion_esc][0]==tmp.dato[3][numeracion_puntoa2][0]:
                                    print("ID: ", tmp.dato[4][numeracion_esc][1])
                                    print("Código: ", tmp.dato[4][numeracion_esc][2])
                                    print("Nombre: ", tmp.dato[4][numeracion_esc][3])
                                    if tmp.dato[4][numeracion_esc][4]==True:
                                        print("Estado de escritorio:  ACTIVO")
                                    else:
                                        print("Estado de escritorio:  INACTIVO")
                                    numeracion_esc+=1
                                    break
                        escritorios=input("Selecciona el ID del escritorio que deseas activar: ")
                        numeracion_esc2=0
                        while tmp.dato[4][numeracion_esc2][1]!=escritorios:
                                numeracion_esc2+=1
                        else:
                            tmp.dato[4][numeracion_esc2][4]=True  
                            break      




    def activarescritoriosauto(self,bus,punto):
            tmp = self.primero
            numeracion_puntoa2=0
            while tmp is not None:
                if bus != tmp.dato[0]:
                    tmp=tmp.getsiguiente()
                else:
                    while punto != tmp.dato[3][numeracion_puntoa2][0]: #tmp.dato[3] son los puntos de atención
                        numeracion_puntoa2+=1
                    else:
                        numeracion_esc=0
                        for i in tmp.dato[4]:
                            if tmp.dato[4][numeracion_esc][0]!=tmp.dato[3][numeracion_puntoa2][0]:
                                numeracion_esc+=1
                            else:
                                while tmp.dato[4][numeracion_esc][0]==tmp.dato[3][numeracion_puntoa2][0]:
                                    print("ID: ", tmp.dato[4][numeracion_esc][1])
                                    print("Código: ", tmp.dato[4][numeracion_esc][2])
                                    print("Nombre: ", tmp.dato[4][numeracion_esc][3])
                                    if tmp.dato[4][numeracion_esc][4]==True:
                                        print("Estado de escritorio:  ACTIVO")
                                    else:
                                        print("Estado de escritorio:  INACTIVO")
                                    numeracion_esc+=1
                                    break
                        escritorios=input("Selecciona el ID del escritorio que deseas activar: ")
                        numeracion_esc2=0
                        while tmp.dato[4][numeracion_esc2][1]!=escritorios:
                            numeracion_esc2+=1    
                        else:
                            tmp.dato[4][numeracion_esc2][4]=True  
                            break   





    def escritoriosdesa(self, bus):
            tmp = self.primero
            numeracion_puntoa2=0
            while tmp is not None:
                if bus != tmp.dato[0]:
                    tmp=tmp.getsiguiente()
                else:
                    print("- - - - - - - EMPRESA SELECCIONADA - - - - - - -")
                    print("ID: ", tmp.dato[0])
                    print("Nombre: ", tmp.dato[1])
                    print("Abreviación: ", tmp.dato[2])
                    numeracion_puntoa=0
                    for i in tmp.dato[3]:    
                        print("ID: ", tmp.dato[3][numeracion_puntoa][0])
                        print("Nombre: ", tmp.dato[3][numeracion_puntoa][1])
                        print("Direccion: ", tmp.dato[3][numeracion_puntoa][2])
                        numeracion_puntoa+=1
                    print("- - - - - - - - - - - - - - - - - - - - - - - - -")
                    punto=input("Seleccione su punto de atención: ")
                    while punto != tmp.dato[3][numeracion_puntoa2][0]:
                        numeracion_puntoa2+=1
                    else:
                        print("- - - - - - - - - - - - - - - - - - - - - - - - -")
                        print("-- PUNTO DE ATENCIÓN SELECCIONADO --")
                        print("ID: ", tmp.dato[3][numeracion_puntoa2][0])
                        print("Nombre: ", tmp.dato[3][numeracion_puntoa2][1])
                        print("Direccion: ", tmp.dato[3][numeracion_puntoa2][2])
                        print("-- ESCRITORIOS --")
                        numeracion_esc=0
                        for i in tmp.dato[4]:
                            if tmp.dato[4][numeracion_esc][0]!=tmp.dato[3][numeracion_puntoa2][0]:
                                numeracion_esc+=1
                            else:
                                while tmp.dato[4][numeracion_esc][0]==tmp.dato[3][numeracion_puntoa2][0]:
                                    print("ID: ", tmp.dato[4][numeracion_esc][1])
                                    print("Código: ", tmp.dato[4][numeracion_esc][2])
                                    print("Nombre: ", tmp.dato[4][numeracion_esc][3])
                                    if tmp.dato[4][numeracion_esc][4]==True:
                                        print("Estado de escritorio:  ACTIVO")
                                    else:
                                        print("Estado de escritorio:  INACTIVO")
                                    numeracion_esc+=1
                                    break
                        escritorios=input("Selecciona el ID del escritorio que deseas activar: ")
                        numeracion_esc2=0
                        while tmp.dato[4][numeracion_esc2][1]!=escritorios:
                            try:
                                numeracion_esc2+=1
                            except:
                                print("Todos los escritorios estan desactivados")
                        else:
                            tmp.dato[4][numeracion_esc2][4]=False 
                            break      




    def desactivarescritoriosauto(self,bus,punto):
            tmp = self.primero
            numeracion_puntoa2=0
            while tmp is not None:
                if bus != tmp.dato[0]:
                    tmp=tmp.getsiguiente()
                else:
                    while punto != tmp.dato[3][numeracion_puntoa2][0]: #tmp.dato[3] son los puntos de atención
                        numeracion_puntoa2+=1
                    else:
                        numeracion_esc=0
                        for i in tmp.dato[4]:
                            if tmp.dato[4][numeracion_esc][0]!=tmp.dato[3][numeracion_puntoa2][0]:
                                numeracion_esc+=1
                            else:
                                while tmp.dato[4][numeracion_esc][0]==tmp.dato[3][numeracion_puntoa2][0]:
                                    print("ID: ", tmp.dato[4][numeracion_esc][1])
                                    print("Código: ", tmp.dato[4][numeracion_esc][2])
                                    print("Nombre: ", tmp.dato[4][numeracion_esc][3])
                                    if tmp.dato[4][numeracion_esc][4]==True:
                                        print("Estado de escritorio:  ACTIVO")
                                    else:
                                        print("Estado de escritorio:  INACTIVO")
                                    numeracion_esc+=1
                                    break
                        escritorios=input("Selecciona el ID del escritorio que deseas activar: ")
                        numeracion_esc2=0
                        while tmp.dato[4][numeracion_esc2][1]!=escritorios:
                            try:
                                numeracion_esc2+=1
                            except:
                                print("Todos los escritorios estan desactivados")
                        else:
                            tmp.dato[4][numeracion_esc2][4]=False  
                            break   
                                    