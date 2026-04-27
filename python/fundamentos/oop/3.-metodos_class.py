class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0

    def hacer_compra(self, monto):  #recibe como argumento el monto de la compra
        self.saldo_pagar += monto   #el saldo a pagar del usuario aumenta en la cantidad del valor recibido

    def aumentarCredito(self, aumento):
        self.limite_credito += aumento
        
    def cambiarCorreo(self, correo):
        self.email = correo


miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la")
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la")
marcelo = Usuario("Marcelo", "Ríos", "marcelo@gmail.com")

miyagi.hacer_compra(2000)
print(f"Primera compra de {miyagi.nombre}: {miyagi.saldo_pagar}")
segundaCompra = 300
miyagi.hacer_compra(segundaCompra)
print(f"Segunda compra: ${segundaCompra}")
#Imprimir cuanto credito le queda a Miyagi
print(f"Credito disponible: ${miyagi.limite_credito - miyagi.saldo_pagar}")
print(miyagi.saldo_pagar)

#Compras de Daniel 2 compras y muestra saldo a pagar ----
daniel.hacer_compra(10000)
print(f"Primera compra de {daniel.nombre}: {daniel.saldo_pagar}")
segundaCompra = 400
daniel.hacer_compra(segundaCompra)
print(f"Segunda compra: ${segundaCompra}")
print(f"Credito disponible: ${daniel.limite_credito - daniel.saldo_pagar}")
print(daniel.saldo_pagar)

'''
1.- Crear un nuevo método que permita aumentar el límite de crédito.
Imprimir el nuevo límite de crédito.

2.- Crear un método que permita cambiar el correo de la instancia.
Mostrar el nuevo correo.
'''
marcelo.aumentarCredito(800)
print(f"El nuevo de crédito es: {marcelo.limite_credito}")

marcelo.cambiarCorreo("marck069@gmail.com")
print(f"El nuevo correo establecido es: {marcelo.email}")

'''
daniel.hacer_compra(45)
print(miyagi.saldo_pagar) #Imprime: 350
print(daniel.saldo_pagar) #Imprime: 45
'''