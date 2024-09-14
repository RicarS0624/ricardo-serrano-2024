class Autor:
    def __init__(self, nombre, nacionalidad, fecha_nacimiento):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento

    def mostrar_info(self):
        return (f"Nombre: {self.nombre}\n"
                f"Nacionalidad: {self.nacionalidad}\n"
                f"Fecha de Nacimiento: {self.fecha_nacimiento}\n")


class Libro:
    def __init__(self, titulo, año_publicacion, autor):
        self.titulo = titulo
        self.año_publicacion = año_publicacion
        self.autor = autor

    def mostrar_info(self):
        return (f"Título: {self.titulo}\n"
                f"Año de Publicación: {self.año_publicacion}\n"
                f"Autor:\n{self.autor.mostrar_info()}")


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
        for libro in self.libros:
            resultado += f"\n{libro.mostrar_info()}\n"
        return resultado


autor1 = Autor("J.K. Rowling", "Británica", "1965-07-31")
autor2 = Autor("George R.R. Martin", "Estadounidense", "1948-09-20")

libro1 = Libro("Harry Potter y la piedra filosofal", 1997, autor1)
libro2 = Libro("Juego de tronos", 1996, autor2)

seccion1 = Seccion("Fantasía")
seccion2 = Seccion("Ciencia Ficción")

seccion1.agregar_libro(libro1)
seccion2.agregar_libro(libro2)

print(seccion1.mostrar_libros())
print(seccion2.mostrar_libros()) 