import os
from PyQt5.QtCore import QObject, pyqtSignal


class Funciones(QObject):

    emisor_opciones = pyqtSignal(list)
    emisor_data = pyqtSignal(list)

    def data_horarios(self) -> list:
        self.emisor_opciones.emit(os.listdir("horarios"))

    def cargar_horario(self, file: str) -> list:
        path = os.path.join("horarios", file)
        horario = []
        with open(path, "r") as file:
            for linea in file:
                horario.append(linea.strip("\n").split(";"))
        return horario

    def horas_libres(self, horario: list) -> list:
        libres = []
        for i in range(len(horario)):
            for j in range(len(horario[i])):
                if horario[i][j] == "":
                    libres.append((i, j))
        return libres

    def disponibilidad(self, nombres: list) -> list:
        data = []
        for nombre in nombres:
            horario = self.cargar_horario(nombre + ".txt")
            horas = self.horas_libres(horario)
            data.append((nombre, horas))
        self.emisor_data.emit(data)


if __name__ == '__main__':
    a = Funciones()
