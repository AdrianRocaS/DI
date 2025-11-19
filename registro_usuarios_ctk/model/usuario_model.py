class Usuario:
    # Aquí definimos se utilizan los datos de los usuarios

    def __init__(self, nombre: str, edad: int, genero: str, avatar: str):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.avatar = avatar

    def __repr__(self):
        return f"Usuario(nombre='{self.nombre}', edad={self.edad}, genero='{self.genero}')"


class GestorUsuarios:
    # Clase encargada de gestionar a los usuarios

    # Iniciamos la lista vacía para que cargue los datos del archivo usuarios.csv
    def __init__(self):
        self._usuarios = []

    # Listamos a todos los usuarios
    def listar(self) -> list[Usuario]:
        return self._usuarios

    # Devuelve los usuarios por orden
    def obtener_usuario_por_indice(self, indice: int) -> Usuario | None:

        try:
            return self._usuarios[indice]
        except IndexError:
            return None