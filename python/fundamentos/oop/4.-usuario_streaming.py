'''
🗂️ Define la clase UsuarioStreaming, que debe incluir:

Atributos:
nombre
email
suscripcion (Gratis, Estándar o Premium)
lista_reproduccion (lista de títulos agregados por el usuario).
Métodos:
agregar_a_lista(self, titulo) agrega un contenido a la lista de reproducción.
ver_contenido(self, titulo) simula que el usuario reproduce un contenido.
cambiar_suscripcion(self, nueva_suscripcion) modifica el tipo de suscripción del usuario.
mostrar_info_usuario(self) muestra los datos del usuario y su lista de reproducción.
🧪 Realizar las siguientes pruebas con instancias:

Crea 3 usuarios de la plataforma de streaming.
Haz que el primer usuario agregue dos títulos a su lista y los vea.
Haz que el segundo usuario agregue un título, lo vea y cambie su suscripción.
Haz que el tercer usuario agregue tres títulos, los vea y cambie su suscripción dos veces.
'''

class UsuarioStreaming:
    def __init__(self, nombre, email, suscripcion="Gratis"):
       self.nombre = nombre
       self.email = email
       self.suscripcion = suscripcion
       self.lista_reproduccion = []


    def agregar_a_lista(self, titulo):
       self.lista_reproduccion.append(titulo)


    def ver_contenido(self, titulo):
        if titulo in self.lista_reproduccion:
            print(f"{self.nombre} está viendo {titulo}")
        else:
            print("Ese título no está en tu lista.")


    def cambiar_suscripcion(self, nueva_suscripcion):
        self.suscripcion = nueva_suscripcion
        print(f"Suscripción actualizada a: {self.suscripcion}")


    def mostrar_info_usuario(self):
        print("\n--- Información del Usuario ---")
        print(f"Nombre: {usser1.nombre}")
        print(f"Email: {usser1.email}")
        print(f"Suscripción: {usser1.suscripcion}")
        print("Lista de reproducción:")
        
        if self.lista_reproduccion:
            for titulo in self.lista_reproduccion:
                print(f"- {titulo}")
        else:
            print("Lista vacía")
    
# Todos los valores que se deban registrar debe ser con input
# Añadir un menu while para llamar a los métodos.
# (Menú de selección)

usser1 = UsuarioStreaming("usuario-N1", "user1@gmail.com")
usser2 = UsuarioStreaming("usuario-N2", "user2@gmail.com")
usser3 = UsuarioStreaming("usuario-N3", "user3@gmail.com")

# Usuario 1: agrega 2 títulos y los ve
usser1.agregar_a_lista("Matrix")
usser1.agregar_a_lista("Inception")
usser1.ver_contenido("Matrix")
usser1.ver_contenido("Inception")

# Usuario 2: agrega 1 título, lo ve y cambia suscripción
usser2.agregar_a_lista("Interstellar")
usser2.ver_contenido("Interstellar")
usser2.cambiar_suscripcion("Premium")

# Usuario 3: agrega 3 títulos, los ve y cambia suscripción 2 veces
usser3.agregar_a_lista("Avatar")
usser3.agregar_a_lista("Titanic")
usser3.agregar_a_lista("Avengers")

usser3.ver_contenido("Avatar")
usser3.ver_contenido("Titanic")
usser3.ver_contenido("Avengers")

usser3.cambiar_suscripcion("Estándar")
usser3.cambiar_suscripcion("Premium")