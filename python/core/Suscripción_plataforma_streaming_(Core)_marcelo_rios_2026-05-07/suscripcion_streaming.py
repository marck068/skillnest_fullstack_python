#Atributos, métodos de clase, métodos estáticos

class SuscripcionStreaming:
    costos_suscripcion = {"Gratis": 0, "Estándar": 5.99, "Premium": 10.99}

    def __init__(self, usuario, tipo_suscripcion="Gratis"):
        self.usuario = usuario
        self.tipo_suscripcion = tipo_suscripcion
        self.costo_mensual = self.costos_suscripcion[tipo_suscripcion]
        self.saldo_pendiente = self.costo_mensual

    def realizar_pago(self, monto):
        self.saldo_pendiente -= monto
        print(f"{self.usuario} pagó ${monto}. Saldo restante: ${self.saldo_pendiente}")

    def cambiar_suscripcion(self, nuevo_tipo):
        if nuevo_tipo in self.costos_suscripcion:
            self.tipo_suscripcion = nuevo_tipo
            self.costo_mensual = self.costos_suscripcion[nuevo_tipo]
            self.saldo_pendiente += self.costo_mensual
            print(f"{self.usuario} cambió a {nuevo_tipo}")
        else:
            print(f"Error: '{nuevo_tipo}' no es un plan válido.")

    def ver_contenido_exclusivo(self):
        if self.tipo_suscripcion == "Gratis":
            print(f"{self.usuario}: Sin acceso. El plan Gratis no tiene contenido exclusivo.")
        else:
            print(f"{self.usuario}: Viendo contenido exclusivo.")

    def mostrar_info_suscripcion(self):
        print(f"[{self.usuario}] Plan: {self.tipo_suscripcion} | Deuda total: ${self.saldo_pendiente:.2f}")

s1 = SuscripcionStreaming("Daniel", "Gratis")
s2 = SuscripcionStreaming("Randy", "Estándar")
s3 = SuscripcionStreaming("Yoycer", "Premium")

print("\n--- Pruebas Usuario 1 (Intenta ver, mejora, paga) ---")

s1.ver_contenido_exclusivo()
s1.cambiar_suscripcion("Estándar")
s1.realizar_pago(5.99)

print("\n--- Pruebas Usuario 2 (Ve, mejora, paga 2 veces) ---")

s2.ver_contenido_exclusivo()
s2.cambiar_suscripcion("Premium")
s2.realizar_pago(10.00)
s2.realizar_pago(6.98)

print("\n--- Pruebas Usuario 3 (Paga menos, ve contenido) ---")

s3.realizar_pago(5.00)
s3.ver_contenido_exclusivo()

print("\n--- Resumen Final ---")
s1.mostrar_info_suscripcion()
s2.mostrar_info_suscripcion()
s3.mostrar_info_suscripcion()