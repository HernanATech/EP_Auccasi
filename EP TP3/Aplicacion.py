
import os

# Archivos que almacenan los datos de personas
archivos_personas = {
    'dni': 'dni.txt',
    'nombre': 'nombre.txt',
    'apellido': 'apellido.txt'
}

def validar_usuario(usuario, clave):
    """Valida el usuario y la clave contra los archivos de login."""
    datos_login = cargar_datos_archivo('login.txt')
    datos_clave = cargar_datos_archivo('clave.txt')
    return usuario == datos_login and clave == datos_clave

def iniciar_sesion():
    """Inicia sesión, con un límite de intentos."""
    intentos = 3
    
    while intentos > 0:
        usuario = input('Usuario: ').strip()
        clave = input('Contraseña: ').strip()
        
        if validar_usuario(usuario, clave):
            print("Acceso concedido.")
            return True
        else:
            intentos -= 1
            print(f"Credenciales incorrectas. Intentos restantes: {intentos}")
    
    print("Demasiados intentos fallidos. Salida del sistema.")
    return False

def cargar_datos_archivo(ruta):
    """Carga los datos de un archivo y devuelve el contenido o un mensaje de error."""
    if os.path.exists(ruta):
        with open(ruta, 'rt', encoding='utf8') as archivo:
            return archivo.read().strip()
    else:
        print(f"Archivo {ruta} no encontrado.")
        return None

def mostrar_personas():
    """Muestra las personas registradas leyendo desde los archivos correspondientes."""
    if todos_archivos_existen():
        registros = zip(*[leer_archivo(arch) for arch in archivos_personas.values()])
        print(f"{'DNI':<15} {'Nombre':<15} {'Apellido':<15}")
        for dni, nombre, apellido in registros:
            print(f"{dni:<15} {nombre:<15} {apellido:<15}")
    else:
        print("No hay registros disponibles.")

def todos_archivos_existen():
    """Verifica si los archivos de personas existen."""
    return all(os.path.exists(archivo) for archivo in archivos_personas.values())

def leer_archivo(ruta):
    """Lee el contenido de un archivo línea por línea."""
    with open(ruta, 'r') as f:
        return [line.strip() for line in f.readlines()]

def agregar_persona():
    """Agrega una nueva persona ingresando DNI, nombre y apellido."""
    datos = {
        'dni': input("Ingrese DNI: ").strip(),
        'nombre': input("Ingrese Nombres: ").strip(),
        'apellido': input("Ingrese Apellidos: ").strip()
    }
    
    for key, archivo in archivos_personas.items():
        with open(archivo, 'a') as f:
            f.write(f'{datos[key]}\n')
    
    print("Persona agregada exitosamente.")

def salir_del_menu():
    """Sale del menú sin cerrar el sistema."""
    print("Saliendo del menú principal.")
    return 'exit'

def mostrar_menu_principal():
    """Muestra el menú principal y ejecuta las acciones correspondientes."""
    opciones = {
        '1': ('Listar Personas', mostrar_personas),
        '2': ('Agregar Persona', agregar_persona),
        '3': ('Salir', salir_del_menu)
    }
    
    opcion_seleccionada = None
    
    while opcion_seleccionada != 'exit':
        print("\nMenú Principal:")
        for clave, (descripcion, _) in opciones.items():
            print(f"{clave}. {descripcion}")
        
        opcion = input("Seleccione una opción: ").strip()
        
        # Comprobamos si la opción es válida
        if opcion in opciones:
            _, accion = opciones[opcion]
            resultado = accion()
            # Verificamos si se seleccionó salir del menú
            if resultado == 'exit':
                opcion_seleccionada = 'exit'
        else:
            print("Opción no válida. Intente nuevamente.")

def main():
    """Función principal que ejecuta el programa."""
    if iniciar_sesion():
        mostrar_menu_principal()

# Ejecutar la función principal
main()