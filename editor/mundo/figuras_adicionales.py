from PySide2.QtCore import QPoint
from PySide2.QtGui import QColor, Qt, QPainter, QPolygon

from editor.mundo.mundo import FiguraConFondo


class Triangulo(FiguraConFondo):
    def __init__(self, p1: QPoint, p2: QPoint, color_linea: QColor, tipo_linea: Qt.PenStyle, ancho_linea: int,
                 color_fondo: QColor):
        super().__init__(p1, p2, color_linea, tipo_linea, ancho_linea, color_fondo)
        self.poligono = QPolygon()
        punto_1 = QPoint(p1.x(), p2.y())
        punto_2 = p2
        d = abs(p2.x() - p1.x())
        x3 = min(p1.x(), p2.x()) + d/2
        y3 = min(p1.y(), p2.y())
        punto_3 = QPoint(x3, y3)
        self.poligono << punto_1 << punto_2 << punto_3

    def _pintar_figura(self, qp: QPainter):
        qp.drawPolygon(self.poligono)