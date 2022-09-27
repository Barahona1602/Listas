from nodo import nodo
import numpy as np
from iteration_utilities import duplicates
import xml.etree.cElementTree as ET


class listaempresa():
    def __init__(self):
        self.primero=None
        self.ultimo= None
        self.size = 0
        


    def siginsert(self, idE, nombre, abreviatura, lista_puntosa, lista_escritorio, lista_trans):
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

    def insertardata(self, idE, nombre, abreviatura):
        global empresa_data
        empresa_data= nodo(dato=[idE, nombre, abreviatura])
        self.size += 1
        if self.primero is None:
            self.primero = empresa_data
            self.ultimo= empresa_data
        else:
            tmp = self.primero
            while tmp.getsiguiente() is not None:
                tmp=tmp.getsiguiente()
            tmp.setsiguiente(empresa_data)
    

    def mostrarempresa(self):
        tmp = self.primero
        conteo=0
        while tmp is not None:
            conteo=conteo+1
            print("ID: ", tmp.dato[0])
            print("Nombre: ", tmp.dato[1])
            print("Abreviación: ", tmp.dato[2])
            print("---------------------------------")
            tmp=tmp.getsiguiente()