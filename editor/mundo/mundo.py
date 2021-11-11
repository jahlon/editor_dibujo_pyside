import pickle
from abc import ABC, abstractmethod, ABCMeta

from PySide2.QtCore import QPoint, Qt, QLine, QRect
from PySide2.QtGui import QColor, QPainter, QPen, QBrush


class IFigura(metaclass=ABCMeta):
    @abstractmethod
    def pintar(self, qp: QPainter, seleccionada: bool):
        raise NotImplementedError

    @abstractmethod
    def esta_dentro(self, x, y) -> bool:
        raise NotImplementedError


class Figura(IFigura, ABC):
    def __init__(self, p1: QPoint, p2: QPoint, color_linea: QColor, tipo_linea: Qt.PenStyle, ancho_linea: int):
        self.punto_1 = p1
        self.punto_2 = p2
        self.color_linea = color_linea
        self.tipo_linea = tipo_linea
        self.ancho_linea = ancho_linea


class Linea(Figura):
    def __init__(self, p1: QPoint, p2: QPoint, color_linea: QColor, tipo_linea: Qt.PenStyle, ancho_linea: int):
        super().__init__(p1, p2, color_linea, tipo_linea, ancho_linea)
        self.linea = QLine(p1, p2)

    def esta_dentro(self, x, y) -> bool:
        m = (self.punto_2.y() - self.punto_1.y()) / (self.punto_2.x() - self.punto_1.x())
        min_x = min(self.punto_1.x(), self.punto_2.x())
        max_x = max(self.punto_1.x(), self.punto_2.x())
        termino_y = m * (x - self.punto_1.x()) + self.punto_1.y()
        return (min_x <= x <= max_x) and (termino_y - 5 <= y <= termino_y + 5)

    def pintar(self, qp: QPainter, seleccionada: bool):
        pen = QPen()
        pen.setStyle(self.tipo_linea)
        pen.setColor(self.color_linea)
        pen.setWidth(self.ancho_linea)
        qp.setPen(pen)
        qp.drawLine(self.linea)

        if seleccionada:
            pen = QPen()
            pen.setColor(Qt.black)
            pen.setWidth(1)
            brush = QBrush()
            brush.setColor(Qt.green)
            brush.setStyle(Qt.SolidPattern)
            qp.setPen(pen)
            qp.setBrush(brush)
            qp.drawEllipse(self.punto_1.x() - 3, self.punto_1.y() - 3, 7, 7)
            qp.drawEllipse(self.punto_2.x() - 3, self.punto_2.y() - 3, 7, 7)


class FiguraConFondo(Figura, ABC):
    def __init__(self, p1: QPoint, p2: QPoint, color_linea: QColor, tipo_linea: Qt.PenStyle, ancho_linea: int,
                 color_fondo: QColor):
        super().__init__(p1, p2, color_linea, tipo_linea, ancho_linea)
        self.color_fondo = color_fondo
        self.rect = QRect(p1, p2)

    @abstractmethod
    def _pintar_figura(self, qp: QPainter):
        raise NotImplementedError

    def esta_dentro(self, x, y) -> bool:
        return self.rect.contains(x, y)

    def pintar(self, qp: QPainter, seleccionada: bool):
        pen = QPen()
        pen.setStyle(self.tipo_linea)
        pen.setColor(self.color_linea)
        pen.setWidth(self.ancho_linea)
        qp.setPen(pen)
        brush = QBrush()
        brush.setColor(self.color_fondo)
        brush.setStyle(Qt.SolidPattern)
        qp.setBrush(brush)
        self._pintar_figura(qp)

        if seleccionada:
            pen = QPen()
            pen.setColor(Qt.black)
            pen.setWidth(1)
            brush = QBrush()
            brush.setColor(Qt.green)
            brush.setStyle(Qt.SolidPattern)
            qp.setPen(pen)
            qp.setBrush(brush)
            qp.drawEllipse(self.punto_1.x() - 3, self.punto_1.y() - 3, 7, 7)
            qp.drawEllipse(self.punto_2.x() - 3, self.punto_1.y() - 3, 7, 7)
            qp.drawEllipse(self.punto_2.x() - 3, self.punto_2.y() - 3, 7, 7)
            qp.drawEllipse(self.punto_1.x() - 3, self.punto_2.y() - 3, 7, 7)


class Rectangulo(FiguraConFondo):

    def __init__(self, p1: QPoint, p2: QPoint, color_linea: QColor, tipo_linea: Qt.PenStyle, ancho_linea: int,
                 color_fondo: QColor):
        super().__init__(p1, p2, color_linea, tipo_linea, ancho_linea, color_fondo)

    def _pintar_figura(self, qp: QPainter):
        qp.drawRect(self.rect)


class Ovalo(FiguraConFondo):
    def __init__(self, p1: QPoint, p2: QPoint, color_linea: QColor, tipo_linea: Qt.PenStyle, ancho_linea: int,
                 color_fondo: QColor):
        super().__init__(p1, p2, color_linea, tipo_linea, ancho_linea, color_fondo)

    def _pintar_figura(self, qp: QPainter):
        qp.drawEllipse(self.rect)


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

    def agregar_figura(self, figura: IFigura):
        self.figuras.append(figura)
        self.modificado = True

    def intentar_seleccionar(self, x, y):
        self.seleccionada = None
        for f in self.figuras:
            if f.esta_dentro(x, y):
                self.seleccionada = f
                self.modificado = True
                break

    def dibujar(self, qp: QPainter):
        for f in self.figuras:
            f.pintar(qp, f == self.seleccionada)

    def borrar_figura_seleccionada(self):
        if self.seleccionada is not None:
            self.figuras.remove(self.seleccionada)
