from nodo import nodo
import numpy as np
import xml.etree.cElementTree as ET
from lista_empresa import listaempresa

listaempresa=listaempresa()

class listatrans():
    def __init__(self):
        self.primero=None
        self.ultimo= None
        self.size = 0

    def insertar_trans(self, id_transaccion, idEmpresa_trans, idPunto_trans, idEscritorio_trans, dpi_trans, nombre_trans, idT_trans, cant_trans):
        global transaccionesE
        transaccionesE= nodo(dato=[id, id_transaccion, idEmpresa_trans, idPunto_trans, idEscritorio_trans, dpi_trans, nombre_trans, idT_trans, cant_trans])
        if self.primero is None:
            self.primero = transaccionesE
            self.ultimo= transaccionesE
        else:
            tmp = self.primero
            while tmp.getsiguiente() is not None:
                tmp=tmp.getsiguiente()
            tmp.setsiguiente(transaccionesE)




    def mostrar_trans(self):
        tmp = self.primero
        while tmp is not None:
            print("--TRANSACCIONES--")
            print("ID: ", tmp.dato[0])
            trans_id=tmp.dato[0]
            print("ID Empresa: ", tmp.dato[1])
            trans_idE=tmp.dato[1]
            print("ID Punto de Atención: ", tmp.dato[2])
            trans_idP=tmp.dato[2]
            cont_trans=0
            escritorios=[]
            for i in tmp.dato[3]:
                print("Escritorios activos: ", tmp.dato[3][cont_trans][0])
                escritorios.append(tmp.dato[3][cont_trans][0])
                cont_trans+=1
            print("DPI: ", tmp.dato[4])
            trans_dpi=tmp.dato[4]
            print("Nombre del cliente: ", tmp.dato[5])
            trans_cliente=tmp.dato[5]
            cont_id=0
            for i in tmp.dato[6]:
                print("ID transacción: ", tmp.dato[6][cont_id][0])
                print("Cantidad: ", tmp.dato[7][cont_id][0])
                trans_idtrans=[]
                trans_cant=[]
                trans_idtrans.append([tmp.dato[6][cont_id][0]])
                trans_cant.append([tmp.dato[7][cont_id][0]])
                cont_id+=1
            tmp=tmp.getsiguiente()




    def eliminardatos(self):
        if self.size>0:
            self.primero=None
            self.ultimo= None
            self.size=0
            print(self.size)