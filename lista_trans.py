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

    def insertar_trans(self, id_transaccion, idEmpresa_trans, idPunto_trans, idEscritorio_trans, clientes, idT_trans):
        global transaccionesE
        transaccionesE= nodo(dato=[id_transaccion, idEmpresa_trans, idPunto_trans, idEscritorio_trans, clientes, idT_trans])
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
            
            contadora3=0 
            print("--TRANSACCIONES--") 
            print("ID: ", tmp.dato[0]) 
            print("ID Empresa: ", tmp.dato[1]) 
            print("ID Punto de Atención: ", tmp.dato[2]) 
            contadora1=0 
            for i in tmp.dato[3]: 
                print("Escritorios activos: ", tmp.dato[3][contadora1][0]) 
                contadora1+=1 
            contadora2=0
            for j in tmp.dato[4]:   
                print("--CLIENTE--") 
                print("DPI: ", tmp.dato[4][contadora2][0]) 
                print("Nombre del cliente: ", tmp.dato[4][contadora2][1]) 
                print("--TRANSACIONES--")
                cont_id=0 
                for l in tmp.dato[5]: 
                    if tmp.dato[5][cont_id][0]!=tmp.dato[4][contadora2][0]:
                        cont_id+=1
                    else:
                        while tmp.dato[5][cont_id][0]==tmp.dato[4][contadora2][0]:    
                            print("ID transacción: ", tmp.dato[5][cont_id][1]) 
                            print("Cantidad: ", tmp.dato[5][cont_id][2]) 
                            cont_id+=1 
                            break
                contadora2+=1     
            contadora3+=1 
            print("-------------------------")
            tmp=tmp.getsiguiente()





    def agregarcliente(self, idE, dpi, cliente, trans, cantidad): 
        tmp = self.primero 
        while tmp is not None: 
            if idE != tmp.dato[1]:
                tmp=tmp.getsiguiente()
            else:
                contadora2=0
                for j in tmp.dato[4]:   
                    print("--CLIENTE--") 
                    print("DPI: ", tmp.dato[4][contadora2][0]) 
                    print("Nombre del cliente: ", tmp.dato[4][contadora2][1])
                    print("--TRANSACIONES--")
                    cont_id=0  
                    for l in tmp.dato[5]: 
                        if tmp.dato[5][cont_id][0]!=tmp.dato[4][contadora2][0]:
                            cont_id+=1
                        else:
                            while tmp.dato[5][cont_id][0]==tmp.dato[4][contadora2][0]:    
                                print("ID transacción: ", tmp.dato[5][cont_id][1]) 
                                print("Cantidad: ", tmp.dato[5][cont_id][2]) 
                                cont_id+=1 
                                break
                    contadora2+=1     
                print("-------------------------")
                print(contadora2)
                break








    def eliminardatos(self):
        if self.size>0:
            self.primero=None
            self.ultimo= None
            self.size=0
            print(self.size)