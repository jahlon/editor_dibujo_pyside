from PySide6.QtCore import QPoint
from PySide6.QtGui import QColor, Qt, QPainter, QPolygon

from editor.mundo.mundo import FiguraConFondo


class Triangulo(FiguraConFondo):
    def __init__(self, p1: QPoint, p2: QPoint, color_linea: QColor, tipo_linea: Qt.PenStyle, ancho_linea: int,
                 color_fondo: QColor):
        super().__init__(p1, p2, color_linea, tipo_linea, ancho_linea, color_fondo)
        self.poligono = QPolygon()
        punto_1: QPoint = p1
        punto_2: QPoint = QPoint(p2.x(), p1.y())
        d = abs(p2.x() - p1.x()) / 2
        if p1.x() > p2.x():
            d = -d
        # convert to int
        x3 = int(p1.x() + d)
        y3 = p2.y()
        punto_3: QPoint = QPoint(x3, y3)
        self.poligono << punto_1 << punto_2 << punto_3

    def _pintar_figura(self, qp: QPainter):
        qp.drawPolygon(self.poligono)