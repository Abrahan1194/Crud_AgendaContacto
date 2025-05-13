# Agenda de Contactos con CRUD
# Crear, Leer, Actualizar y Eliminar contactos

# Diccionario para almacenar los contactos
agenda = {}

# ----------------------------------------
# Crear contacto
def agregar_contacto(nombre, telefono, email):
    if nombre in agenda:
        print("\033[91mEl contacto '" + nombre + "' ya existe.\033[0m")
    else:
        agenda[nombre] = {"teléfono": telefono, "email": email}
        print("\033[92mContacto '" + nombre + "' agregado correctamente.\033[0m")

# ----------------------------------------
# Listar todos los contactos
def listar_contactos():
    if not agenda:
        print("\033[93mLa agenda está vacía.\033[0m")
    else:
        print("\033[96mLista de contactos:\033[0m")
        for nombre, datos in agenda.items():
            print("\033[94mNombre:\033[0m " + nombre)
            print("  \033[94mTeléfono:\033[0m " + datos["teléfono"])
            print("  \033[94mEmail:\033[0m " + datos["email"])
            print("-" * 30)

# ----------------------------------------
# Buscar un contacto por nombre
def buscar_contacto(nombre):
    if nombre in agenda:
        datos = agenda[nombre]
        print("\033[96mContacto encontrado:\033[0m")
        print("\033[94mNombre:\033[0m " + nombre)
        print("  \033[94mTeléfono:\033[0m " + datos["teléfono"])
        print("  \033[94mEmail:\033[0m " + datos["email"])
    else:
        print("\033[91mEl contacto '" + nombre + "' no existe.\033[0m")

# ----------------------------------------
# Actualizar un contacto existente
def actualizar_contacto(nombre, nuevo_telefono=None, nuevo_email=None):
    if nombre in agenda:
        if nuevo_telefono:
            agenda[nombre]["teléfono"] = nuevo_telefono
        if nuevo_email:
            agenda[nombre]["email"] = nuevo_email
        print("\033[92mContacto '" + nombre + "' actualizado correctamente.\033[0m")
    else:
        print("\033[91mEl contacto '" + nombre + "' no existe.\033[0m")

# ----------------------------------------
# Eliminar un contacto existente
def eliminar_contacto(nombre):
    if nombre in agenda:
        del agenda[nombre]
        print("\033[92mContacto '" + nombre + "' eliminado correctamente.\033[0m")
    else:
        print("\033[91mEl contacto '" + nombre + "' no existe.\033[0m")

# ----------------------------------------
# Menú interactivo para el usuario
while True:
    print("\n\033[96mMenú de Agenda de Contactos\033[0m")
    print("1. Agregar contacto")
    print("2. Listar contactos")
    print("3. Buscar contacto")
    print("4. Actualizar contacto")
    print("5. Eliminar contacto")
    print("6. Salir")
    
    opcion = input("Seleccione una opción (1-6): ")
    
    if opcion == "1":
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        email = input("Email: ")
        agregar_contacto(nombre, telefono, email)
    
    elif opcion == "2":
        listar_contactos()
    
    elif opcion == "3":
        nombre = input("Nombre a buscar: ")
        buscar_contacto(nombre)
    
    elif opcion == "4":
        nombre = input("Nombre del contacto a actualizar: ")
        nuevo_telefono = input("Nuevo teléfono (dejar vacío si no cambia): ")
        nuevo_email = input("Nuevo email (dejar vacío si no cambia): ")
        actualizar_contacto(
            nombre,
            nuevo_telefono if nuevo_telefono.strip() != "" else None,
            nuevo_email if nuevo_email.strip() != "" else None
        )
    
    elif opcion == "5":
        nombre = input("Nombre del contacto a eliminar: ")
        eliminar_contacto(nombre)
    
    elif opcion == "6":
        print("\033[93mSaliendo del programa.\033[0m")
        break
    
    else:
        print("\033[91mOpción no válida. Intente de nuevo.\033[0m")