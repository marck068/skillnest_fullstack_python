#Atributos, métodos de clase, métodos estáticos

#DEFINICION DE LA CLASE
class SuscripcionStreaming:
    #Atributo de clase
    costos_suscripcion = {
        "Gratis": 0,
        "Estándar": 5.99,
        "Premium": 10.99
    }

    #Lista en donde esten todas las suscripciones
    suscripciones = []

    #Método CONSTRUCTOR
    def __init__(self, usuario, tipo_suscripcion="Gratis"):
        #Atributos de instancia
        self.usuario = usuario
        self.tipo_suscripcion = tipo_suscripcion
        self.costo_mensual = SuscripcionStreaming.costos_suscripcion[tipo_suscripcion]
        self.saldo_pendiente = self.costo_mensual

        #Agregar elementos a la lista SuscripcionStreaming (objeto)
        SuscripcionStreaming.suscripciones.append(self)

    #Método de instancia
    def realizar_pago(self, monto):
        """Reduce el saldo pendiente según el monto pagado."""
        self.saldo_pendiente = self.saldo_pendiente - monto

        print(f"Pago realizado por: {self.usuario}")
        print(f"Saldo pendiente: {self.saldo_pendiente}")

    #Método de instancia
    def cambiar_suscripcion(self, nuevo_tipo):
        """Cambia el tipo de suscripción y actualiza el costo mensual."""
        self.tipo_suscripcion = nuevo_tipo
        self.costo_mensual = SuscripcionStreaming.costos_suscripcion[nuevo_tipo]
        self.saldo_pendiente = self.costo_mensual

        print(f"Nueva suscripción: {self.tipo_suscripcion}")

    #Método estático
    #Este no usa CLS ni SELF, solo parámetros.
    @staticmethod
    def ver_contenido_exclusivo(tipo_suscripcion):
        """Permite ver contenido exclusivo según el tipo de suscripción."""
        if tipo_suscripcion == "Premium":
            print("Acceso a contenido exclusivo Premium")
        elif tipo_suscripcion == "Estándar":
            print("Acceso a contenido estándar")
        else:
            print("No tiene acceso a contenido exclusivo")

    #Método de instancia
    def mostrar_info_suscripcion(self):
        """Muestra la información de la suscripción del usuario."""
        print(f"Usuario: {self.usuario}")
        print(f"Tipo de suscripción: {self.tipo_suscripcion}")
        print(f"Costo mensual: {self.costo_mensual}")
        print(f"Saldo pendiente: {self.saldo_pendiente}")

    #Método de CLASE
    # Usa "CLS" porque trabaja con la información de la clase
    @classmethod
    def cantidad_suscripciones(cls):
        return len(cls.suscripciones)

#Creación de objetos (Instancias)
s1 = SuscripcionStreaming("Daniel")
s2 = SuscripcionStreaming("Randy", "Estándar")
s3 = SuscripcionStreaming("Yoycer", "Premium")

#Uso de métodos de instancia
print("== MÉTODO DE INSTANCIA==")

#Mostrar datos de suscripciones
s1.mostrar_info_suscripcion()
print()

s2.mostrar_info_suscripcion()
print()

s3.mostrar_info_suscripcion()
print()

#Uso de método de instancia
print("== REALIZAR PAGOS ==")

s2.realizar_pago(3)
print()

s3.realizar_pago(5)
print()

#Uso de método de instancia
print("== CAMBIAR SUSCRIPCIÓN ==")

s1.cambiar_suscripcion("Premium")
print()

#Método estático
print("=== MÉTODO ESTÁTICO ===")

SuscripcionStreaming.ver_contenido_exclusivo(s1.tipo_suscripcion)
print()

SuscripcionStreaming.ver_contenido_exclusivo(s2.tipo_suscripcion)
print()

SuscripcionStreaming.ver_contenido_exclusivo(s3.tipo_suscripcion)
print()

#Contar suscripciones
print("== CONTAR SUSCRIPCIONES ==")

print(f"Total suscripciones: {SuscripcionStreaming.cantidad_suscripciones()}")