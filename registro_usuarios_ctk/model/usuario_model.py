import csv
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

    def listar(self):
        # Devuelve la lista de usuarios
        return list(self._usuarios)


    def obtener_por_indice(self, indice: int):
        # Devuelve el usuario en el índice o None si índice inválido
        try:
            return self._usuarios[indice]
        except IndexError:
            return None

    # FASE 2
    def añadir(self, usuario: Usuario):
        # Añade un usuario a la lista
        self._usuarios.append(usuario)

    def eliminar(self, indice: int):
        # Elimina el usuario indicado por índice
        try:
            del self._usuarios[indice]
            return True
        except IndexError:
            return False

    def actualizar(self, indice: int, usuario: Usuario):
        # Reemplaza al usuario en un índice por otro nuevo
        try:
            self._usuarios[indice] = usuario
            return True
        except IndexError:
            return False

    # FASE 3
    def guardar_csv(self, ruta_csv):
        # Guarda los usuarios en 'usuarios.csv'
        with open(ruta_csv, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["nombre", "edad", "genero", "avatar"])
            for u in self._usuarios:
                writer.writerow([u.nombre, u.edad, u.genero, u.avatar])

    def cargar_csv(self, ruta_csv):
        # Carga los usuarios de 'usuarios.csv'
        try:
            with open(ruta_csv, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader, None)  # saltar cabecera

                self._usuarios.clear()

                for fila in reader:
                    try:
                        nombre, edad_str, genero, avatar = fila
                        self._usuarios.append(
                            Usuario(nombre, int(edad_str), genero, avatar)
                        )
                    except:
                        continue
        except FileNotFoundError:
            pass
