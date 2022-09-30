from nodo import nodo
import numpy as np
import xml.etree.cElementTree as ET


class listatrans():
    def __init__(self):
        self.primero=None
        self.ultimo= None
        self.size = 0

    def insertar_trans(self, id, idE, idP, idEs, dpi, nombre, idT, cant):
        global empresa_trans
        empresa_trans= nodo(dato=[id, idE, idP, idEs, dpi, nombre, idT, cant])
        if self.primero is None:
            self.primero = empresa_trans
            self.ultimo= empresa_trans
        else:
            tmp = self.primero
            while tmp.getsiguiente() is not None:
                tmp=tmp.getsiguiente()
            tmp.setsiguiente(empresa_trans)



    def mostrar_empresa(self):
        tmp = self.primero
        while tmp is not None:
            numeracion_trans=0
            print("--TRANSACCIONES--")
            print("ID: ", tmp.dato[0])
            print("ID Empresa: ", tmp.dato[1])
            print("ID Punto de Atención: ", tmp.dato[2])
            cont_trans=0
            for i in tmp.dato[3]:
                print("Escritorios activos: ", tmp.dato[3][cont_trans][0])
                cont_trans+=1
            print("DPI: ", tmp.dato[4])
            print("Nombre del cliente: ", tmp.dato[5])
            cont_id=0
            for i in tmp.dato[6]:
                print("ID transacción: ", tmp.dato[6][cont_id][0])
                print("Cantidad: ", tmp.dato[7][cont_id][0])
                cont_id+=1
            numeracion_trans+=1
            tmp=tmp.getsiguiente()




    def eliminardatos(self):
        if self.size>0:
            self.primero=None
            self.ultimo= None
            self.size=0
            print(self.size)