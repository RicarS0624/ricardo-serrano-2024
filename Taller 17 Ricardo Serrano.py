class Universidad:
    def _init_(self):
        self._nombre = "UNAB"
        self.ciudad = "Bucaramanga"

    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, nombre):
        self._nombre = nombre

    
class UniversidadPublica(Universidad):
    def _init_(self, en_paro):
        super()._init_()
        self.en_paro = en_paro

    def mostrar_datos(self):
        print(f"Nombre: {self.get_nombre()} - Ciudad: {self.ciudad} - En paro: {self.en_paro}")

def main():
    mi_universidad = UniversidadPublica(False)

    print(mi_universidad.get_nombre())
    mi_universidad.set_nombre("Universidad Autónoma de Bucaramanga")
    print(mi_universidad.get_nombre())

    mi_universidad.mostrar_datos()

if _name_ == "_main_":
    main()