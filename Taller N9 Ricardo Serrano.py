import os

class Autor:
    def __init__(self, nombre, nacionalidad, fecha_nacimiento):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento

    def mostrar_info(self):
        return (f"Nombre: {self.nombre}\n"
                f"Nacionalidad: {self.nacionalidad}\n"
                f"Fecha de Nacimiento: {self.fecha_nacimiento}\n")

    def to_string(self):
        return f"{self.nombre};{self.nacionalidad};{self.fecha_nacimiento}\n"

class Libro:
    def __init__(self, titulo, año_publicacion, autor):
        self.titulo = titulo
        self.año_publicacion = año_publicacion
        self.autor = autor

    def mostrar_info(self):
        return (f"Título: {self.titulo}\n"
                f"Año de Publicación: {self.año_publicacion}\n"
                f"Autor:\n{self.autor.mostrar_info()}")

    def to_string(self):
        return f"{self.titulo};{self.año_publicacion};{self.autor.nombre}\n"

class Seccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_libros(self):
        if not self.libros:
            return "No hay libros en esta sección."
        
        resultado = f"Sección: {self.nombre}\n"
        for idx, libro in enumerate(self.libros, 1):
            resultado += f"\n{idx}. {libro.mostrar_info()}\n"
        return resultado

    def to_string(self):
        return f"{self.nombre}\n" + "\n".join(libro.to_string() for libro in self.libros)

class Biblioteca:
    def __init__(self):
        self.secciones = []
        self.autores = []

    def cargar_autores(self):
        if os.path.exists('autores.txt'):
            with open('autores.txt', 'r') as f:
                for linea in f:
                    nombre, nacionalidad, fecha_nacimiento = linea.strip().split(';')
                    self.autores.append(Autor(nombre, nacionalidad, fecha_nacimiento))

    def cargar_secciones(self):
        if os.path.exists('secciones.txt'):
            with open('secciones.txt', 'r') as f:
                for linea in f:
                    nombre = linea.strip()
                    nueva_seccion = Seccion(nombre)
                    self.secciones.append(nueva_seccion)

    def cargar_libros(self):
        if os.path.exists('libros.txt'):
            with open('libros.txt', 'r') as f:
                for linea in f:
                    titulo, año_publicacion, autor_nombre = linea.strip().split(';')
                    autor = next((a for a in self.autores if a.nombre == autor_nombre), None)
                    if autor:
                        libro = Libro(titulo, int(año_publicacion), autor)
                        seccion = self.secciones[-1]  # Suponiendo que el libro pertenece a la última sección cargada
                        seccion.agregar_libro(libro)

    def guardar_autores(self):
        with open('autores.txt', 'w') as f:
            for autor in self.autores:
                f.write(autor.to_string())

    def guardar_secciones(self):
        with open('secciones.txt', 'w') as f:
            for seccion in self.secciones:
                f.write(seccion.to_string())

    def guardar_libros(self):
        with open('libros.txt', 'w') as f:
            for seccion in self.secciones:
                for libro in seccion.libros:
                    f.write(libro.to_string())

    def mostrar_secciones(self):
        if not self.secciones:
            return "No hay secciones en la biblioteca."
        
        resultado = "Secciones:\n"
        for idx, seccion in enumerate(self.secciones, 1):
            resultado += f"{idx}. {seccion.nombre}\n"
        return resultado

    def crear_seccion(self):
        nombre = input("Ingrese el nombre de la nueva sección: ")
        nueva_seccion = Seccion(nombre)
        self.secciones.append(nueva_seccion)
        print(f"Sección '{nombre}' creada exitosamente.")
        self.guardar_secciones()

    def mostrar_autores(self):
        if not self.autores:
            return "No hay autores en la biblioteca."
        
        resultado = "Autores:\n"
        for idx, autor in enumerate(self.autores, 1):
            resultado += f"{idx}. {autor.nombre}\n"
        return resultado

    def registrar_autor(self):
        nombre = input("Ingrese el nombre del autor: ")
        nacionalidad = input("Ingrese la nacionalidad del autor: ")
        fecha_nacimiento = input("Ingrese la fecha de nacimiento del autor (YYYY-MM-DD): ")
        nuevo_autor = Autor(nombre, nacionalidad, fecha_nacimiento)
        self.autores.append(nuevo_autor)
        print(f"Autor '{nombre}' registrado exitosamente.")
        self.guardar_autores()

    def registrar_libro(self):
        self.mostrar_autores()
        autor_idx = int(input("Ingrese el número del autor: ")) - 1
        if autor_idx < 0 or autor_idx >= len(self.autores):
            print("Número de autor inválido.")
            return
        
        titulo = input("Ingrese el título del libro: ")
        año_publicacion = int(input("Ingrese el año de publicación del libro: "))
        libro = Libro(titulo, año_publicacion, self.autores[autor_idx])
        print(f"Libro '{titulo}' registrado exitosamente.")
        self.guardar_libros()
        return libro

    def agregar_libro_a_seccion(self):
        if not self.secciones:
            print("No hay secciones disponibles.")
            return
        
        self.mostrar_secciones()
        seccion_idx = int(input("Ingrese el número de la sección: ")) - 1
        if seccion_idx < 0 or seccion_idx >= len(self.secciones):
            print("Número de sección inválido.")
            return
        
        libro = self.registrar_libro()
        if libro:
            self.secciones[seccion_idx].agregar_libro(libro)
            print(f"Libro agregado a la sección '{self.secciones[seccion_idx].nombre}'.")
            self.guardar_libros()

    def ver_libros_de_seccion(self):
        if not self.secciones:
            print("No hay secciones disponibles.")
            return
        
        self.mostrar_secciones()
        seccion_idx = int(input("Ingrese el número de la sección: ")) - 1
        if seccion_idx < 0 or seccion_idx >= len(self.secciones):
            print("Número de sección inválido.")
            return
        
        print(self.secciones[seccion_idx].mostrar_libros())


def menu():
    biblioteca = Biblioteca()
    biblioteca.cargar_autores()
    biblioteca.cargar_secciones()
    biblioteca.cargar_libros()
    
    while True:
        print("\n--- Menú Principal ---")
        print("1. Ver secciones existentes")
        print("2. Crear una nueva sección")
        print("3. Ver libros de una sección")
        print("4. Ver autores existentes")
        print("5. Registrar un nuevo autor")
        print("6. Registrar un nuevo libro")
        print("7. Agregar un libro a una sección")
        print("8. Salir")

        opcion = int(input("Ingrese el número de la opción deseada: "))

        if opcion == 1:
            print(biblioteca.mostrar_secciones())
        elif opcion == 2:
            biblioteca.crear_seccion()
        elif opcion == 3:
            biblioteca.ver_libros_de_seccion()
        elif opcion == 4:
            print(biblioteca.mostrar_autores())
        elif opcion == 5:
            biblioteca.registrar_autor()
        elif opcion == 6:
            biblioteca.registrar_libro()
        elif opcion == 7:
            biblioteca.agregar_libro_a_seccion()
        elif opcion == 8:
            print("Guardando datos y saliendo del programa...")
            biblioteca.guardar_autores()
            biblioteca.guardar_secciones()
            biblioteca.guardar_libros()
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()