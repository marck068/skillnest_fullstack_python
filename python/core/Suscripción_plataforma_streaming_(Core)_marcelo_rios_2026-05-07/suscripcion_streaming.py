#Atributos, métodos de clase, métodos estáticos

#DEFINICIÓN DE LA CLASE
class SuscripcionStreaming:
    
    #Atributo de clase
    costos_suscripcion = {
        "Gratis": 0,
        "Estándar": 5.99,
        "Premium": 10.99
    }

    #Lista con todas las suscripciones
    suscripciones = []

    #Método constructor
    def __init__(self, usuario, tipo_suscripcion="Gratis"):
        
        #Atributos de instancia
        self.usuario = usuario
        self.tipo_suscripcion = tipo_suscripcion
        self.costo_mensual = SuscripcionStreaming.costos_suscripcion[tipo_suscripcion]
        self.saldo_pendiente = self.costo_mensual

        #Agregar objeto a la lista
        SuscripcionStreaming.suscripciones.append(self)

    #Método de instancia
    def realizar_pago(self, monto):
        """Reduce el saldo pendiente según el monto pagado."""
        
        self.saldo_pendiente -= monto

        if self.saldo_pendiente < 0:
            self.saldo_pendiente = 0

        print(f"Pago realizado por {self.usuario}")
        print(f"Saldo pendiente: ${self.saldo_pendiente}")

    #Método de instancia
    def cambiar_suscripcion(self, nuevo_tipo):
        """Cambia el tipo de suscripción y actualiza el costo mensual."""
        
        self.tipo_suscripcion = nuevo_tipo
        self.costo_mensual = SuscripcionStreaming.costos_suscripcion[nuevo_tipo]
        self.saldo_pendiente = self.costo_mensual

        print(f"{self.usuario} cambió su suscripción a {nuevo_tipo}")

    #Método estático
    @staticmethod
    def ver_contenido_exclusivo(tipo_suscripcion):
        """Permite ver contenido exclusivo según el tipo de suscripción."""

        if tipo_suscripcion == "Premium":
            print("Puede ver películas y series exclusivas.")
        elif tipo_suscripcion == "Estándar":
            print("Puede ver contenido estándar.")
        else:
            print("No tiene acceso a contenido exclusivo.")

    #Método de instancia
    def mostrar_info_suscripcion(self):
        """Muestra la información de la suscripción del usuario."""

        print(f"Usuario: {self.usuario}")
        print(f"Tipo Suscripción: {self.tipo_suscripcion}")
        print(f"Costo Mensual: ${self.costo_mensual}")
        print(f"Saldo Pendiente: ${self.saldo_pendiente}")

    #Método de clase
    @classmethod
    def cantidad_suscripciones(cls):
        return len(cls.suscripciones)


#Creación de objetos
s1 = SuscripcionStreaming("Matias")
s2 = SuscripcionStreaming("Daniel", "Estándar")
s3 = SuscripcionStreaming("Randy", "Premium")

#Mostrar información
print("=== INFORMACIÓN SUSCRIPCIONES ===")
s1.mostrar_info_suscripcion()
print()

s2.mostrar_info_suscripcion()
print()

s3.mostrar_info_suscripcion()
print()

#Realizar pagos
print("=== PAGOS ===")
s2.realizar_pago(3)
print()

s3.realizar_pago(5)
print()

#Cambiar suscripción
print("=== CAMBIAR SUSCRIPCIÓN ===")
s1.cambiar_suscripcion("Premium")
print()

#Ver contenido exclusivo
print("=== CONTENIDO EXCLUSIVO ===")
SuscripcionStreaming.ver_contenido_exclusivo(s1.tipo_suscripcion)
print()

SuscripcionStreaming.ver_contenido_exclusivo(s2.tipo_suscripcion)
print()

SuscripcionStreaming.ver_contenido_exclusivo(s3.tipo_suscripcion)
print()

#Cantidad de suscripciones
print("=== TOTAL SUSCRIPCIONES ===")
print(f"Total: {SuscripcionStreaming.cantidad_suscripciones()}")