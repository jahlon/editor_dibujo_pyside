import pickle
from abc import ABC

from PySide2.QtCore import QPoint, Qt, QLine, QRect
from PySide2.QtGui import QColor, QPainter


class Figura(ABC):
    def __init__(self, p1: QPoint, p2: QPoint, color_linea: QColor, tipo_linea: Qt.PenStyle, ancho_linea: int):
        self.punto_1 = p1
        self.punto_2 = p2
        self.color_linea = color_linea
        self.tipo_linea = tipo_linea
        self.ancho_linea = ancho_linea


class Linea(Figura):
    def __init__(self, p1: QPoint, p2: QPoint, color_linea: QColor, tipo_linea: Qt.PenStyle, ancho_linea: int):
        Figura.__init__(p1, p2, color_linea, tipo_linea, ancho_linea)
        self.linea = QLine(p1, p2)


class FiguraConFondo(Figura, ABC):
    def __init__(self, p1: QPoint, p2: QPoint, color_linea: QColor, tipo_linea: Qt.PenStyle, ancho_linea: int,
                 color_fondo: QColor):
        Figura.__init__(p1, p2, color_linea, tipo_linea, ancho_linea)
        self.color_fondo = color_fondo
        self.rect = QRect(p1, p2)


class Rectangulo(FiguraConFondo):

    def __init__(self, p1: QPoint, p2: QPoint, color_linea: QColor, tipo_linea: Qt.PenStyle, ancho_linea: int,
                 color_fondo: QColor):
        super().__init__(p1, p2, color_linea, tipo_linea, ancho_linea, color_fondo)


class Ovalo(FiguraConFondo):
    def __init__(self, p1: QPoint, p2: QPoint, color_linea: QColor, tipo_linea: Qt.PenStyle, ancho_linea: int,
                 color_fondo: QColor):
        super().__init__(p1, p2, color_linea, tipo_linea, ancho_linea, color_fondo)


class Dibujo:
    def __init__(self):
        self.figuras = []
        self.seleccionada = None
        self.archivo = None
        self.modificado = False

    def esta_guardado(self):
        return self.archivo is not None

    def guardar(self, archivo=None):
        if archivo is not None:
            self.archivo = archivo

        with open(self.archivo, "wb") as f:
            pickle.dump(self, f)

        self.modificado = False

    def cargar(self, archivo):
        self.archivo = archivo

        with open(self.archivo, "rb") as f:
            d = pickle.load(f)
            self.figuras = d.figuras
            self.seleccionada = d.seleccionada
            self.archivo = d.archivo
            self.modificado = False

    def dibujar(self, qp: QPainter):
        for f in self.figuras:
            f.pintar(qp, f == self.seleccionada)
