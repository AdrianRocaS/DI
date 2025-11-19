from dataclasses import dataclass
from typing import List


@dataclass
class Usuario:
    nombre: str
    edad: int
    genero: str
    avatar: str = ""


class GestorUsuarios:
    def __init__(self):
        # Lista privada de usuarios
        self._usuarios: List[Usuario] = []
        # Cargamos datos de ejemplo para fase 1
        self._cargar_datos_de_ejemplo()


    def _cargar_datos_de_ejemplo(self):
        # Añade 3 usuarios de ejemplo
        self._usuarios.append(Usuario("Ana", 28, "Femenino", "assets/avatar1.png"))
        self._usuarios.append(Usuario("Luis", 34, "Masculino", "assets/avatar2.png"))
        self._usuarios.append(Usuario("María", 22, "Femenino", "assets/avatar3.png"))


    def listar(self):
        # Devuelve la lista de usuarios
        return list(self._usuarios)


    def obtener_por_indice(self, indice: int):
        # Devuelve el usuario en el índice o None si índice inválido
        try:
            return self._usuarios[indice]
        except IndexError:
            return None

