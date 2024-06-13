# -*- coding: utf-8 -*-

from modelos import Socio, Compra, engine
from sqlalchemy.orm import sessionmaker

def altaSocio():
    print("\nNUEVO SOCIO")
    nom = input("Nombre del socio: ")
    tel = input("Teléfono del socio: ")
    nuevo = Socio(nombre = nom, telefono = tel)
    sesion.add(nuevo)
    sesion.commit()


def altaCompras():
    print("\nNUEVA COMPRA")
    num = input("Número de socio que realiza la compra: ")
    socio = sesion.query(Socio).filter(Socio.num == num).scalar()
    if socio:
        print("Compra de", socio.nombre)
        producto = input("Código de producto: ")
        total = input("Total de compra: ")
        nueva = Compra(producto=producto, total=total)
        socio.miscompras.append(nueva)
        sesion.commit()
    else:
        print("Socio", num, "no encontrado.")
        
def consultaSocios():
    concompras = sesion.query(Socio).join(Compra)
    print("\nCLIENTES CON COMPRAS:")
    for reg in concompras:
        totalf = 0
        print("------")
        listado = ""
        for com in reg.miscompras:
            listado += "\n  -- Nº factura: {} Total: {}".format(
    				com.factura, com.total)
            totalf += com.total
        print("Total facturas de", reg.nombre,": %2.2f" % totalf, listado)

Session = sessionmaker(bind = engine)
sesion = Session() 

oper = ""
while(oper != "0"):
    print("\nOPCIONES:\n1- Altas de socios\n2- Altas de compras"\
          "\n3- Consulta de socios y compras\n\n0-Salir")
    oper = input("Indique la opción: ")
    if oper == "1":
        altaSocio()
    if oper == "2":
        altaCompras()
    if oper == "3":
        consultaSocios()
print("Gracias por usar SQLAlchemy.")
