class SuscripcionStreaming:
   costos_suscripcion = {"Gratis": 0, "Estándar": 5.99, "Premium": 10.99}

   def __init__(self, usuario, tipo_suscripcion="Gratis"):
       pass

   def realizar_pago(self, monto):
       """Reduce el saldo pendiente según el monto pagado."""
       pass

   def cambiar_suscripcion(self, nuevo_tipo):
       """Cambia el tipo de suscripción y actualiza el costo mensual."""
       pass

   def ver_contenido_exclusivo(self):
       """Permite ver contenido exclusivo según el tipo de suscripción."""
       pass

   def mostrar_info_suscripcion(self):
       """Muestra la información de la suscripción del usuario."""
       pass 