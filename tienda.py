from datetime import date, datetime
class Empresa:
    def __init__(self, nom = "Tecno bit", ruc ="0921171617001", telf ="0982971849", direc ="Bucay(Ganl. Antonio Elizalde"):
        self.nombre = nom 
        self.ruc = ruc 
        self.telefono = telf 
        self.direccion = direc 
    def mostrar_Empresa(self):
        print("Empresa:{:17} Ruc:{} Direcc: {}".format(self.nombre, self.ruc, self.direccion))

from abc import ABC, abstractmethod
class Cliente(ABC):
    def __init__(self, nom, ced, telf):
        self.nombre = nom 
        self.cedula = ced 
        self.telefono = telf
    @abstractmethod
    def get_Cedula(self):
        return self.cedula
    def mostrar_Cliente(self):
        print(self.nombre, self.cedula, self.telefono)
        
class Cliente_Corporativo(Cliente):
    def __init__(self,nomb, cedu, telfo, contrato = True):
        super().__init__(nomb, cedu, telfo)
        self.__contrato = contrato
    @property
    def contrato(self): # getter: obtener el valor del atributo prvado
        return self.__contrato
    @contrato.setter
    def contrato(self, value): # setterasigna el valor al atributo privado
        if value:
            self.__contrato = value
        else:
            self.__contrato = "Sin Contrato"
    def mostrar_Cliente(self):
        print(self.nombre, self.__contrato)

class Cliente_Personal(Cliente):
    def __init__(self,nom, ced, telf, promocion = True):
        super().__init__(nom, ced, telf)
        self.__promcion = promocion
        
    @property
    def promocion(self): # getter: obtener el valor del atributo prvado
        return self.__promcion == True:    
    def mostrar_Cliente(self):
        print("Cliente: {:13}  Cedula: {}".format(self.nombre, self.cedula))    
    def get_Cedula(self):
        return super().get_Cedula()

class Articulo:
    secuencia = 0 
    iva = 0.12
    def __init__(self, descp, prec, stock):
        Articulo.secuencia += 1
        self.codigo = Articulo.secuencia
        self.descripcion = descp
        self.precio = prec
        self.stock = stock
    def mostar_Articulo(self):
        print(self.codigo, self.descripcion)

class Deta_Venta:
    linea = 0
    def __init__(self, articulo, cantidad):
        Deta_Venta.linea += 1
        self.linea_det = Deta_Venta.linea
        self.articulo = articulo
        self.precio = articulo.precio
        self.cantidad = cantidad 
    
class Cab_Venta:
    def __init__(self, empresa, fac, fecha, cliente, tot = 0):
        self.empresa = empresa
        self.factura = fac
        self.fecha = fecha
        self.cliente = cliente
        self.total = tot 
        self.deta_vent = []

    def agregar_Deta(self, articulo, cantidad):
        detalle = Deta_Venta(articulo, cantidad)
        self.total += detalle.precio * detalle.cantidad
        self.deta_vent.append(detalle)
    
    def mostrar_Venta(self, empNombre, empRuc):
        print("Empresa: {:17}  Ruc:{}".format(empNombre, empRuc))
        print("Factura #:{:13} Fecha: {}".format(self.factura, self.fecha))
        self.cliente.mostrar_Cliente()
        print("Linea   Articulo    Precio   Cantidad   Subtotal")
        for det in self.deta_vent:
            print("{:5} {:15} {} {:6} {:7}".format(det.linea, det.articulo.descripcion, det.precio, det.camtidad, det.precio*det.cantidad))
        print("Total Venta: {:26}".format(self.total))

class Interfaces_SistemaPago(ABC):
    @abstractmethod
    def pago(self):
        pass
    @abstractmethod
    def saldo(self):
        pass

class Pago_TarjetaImplements(Interfaces_SistemaPago):
    def pago(self):
        return "Pago Tarjeta"
    def saldo(self):
        return "Saldo Tarjeta rebajado"

class Implements_pagoContrato(Interfaces_SistemaPago):
    def pago(self):
        return "Pago Contrato_2"
    def saldo(self):
        return "Saldo Contrato rebajado"

class Vendedor():
    def __init__(self, nombre):
        self.nombre = nombre
    def modulo_Pago(self, contrato_V):
        return contrato_V.pago()

pagoTarjeta = Pago_TarjetaImplements()
print(pagoTarjeta.pago())
pagoContrato = Implements_pagoContrato()
print(pagoContrato())


# emp = Empresa("El mas Barato","0982971849001", "09829718489", "JunaPeres y pedro")
# emp.mostrar_Empresa()
# print(emp.nombre)

# cli.1 = Cliente_Corporativo("Jose", "0982984785", "0982971489", "#001")
# cli.1 = mostrar_Cliente()
# print(cli.1.nombre)
# cli.1.contrato = "#002"
# print(cli.1.contrato)
# today = date.today()
# cli.1 = Cliente_Personal("Jose", "0982984785", "0982971489", True)
# cli.1 = mostrar_Cliente()