from PySide6.QtCore import Qt, QCoreApplication, QPoint
from PySide6.QtGui import QMouseEvent, QPaintEvent, QPainter, QBrush, QPalette
from PySide6.QtWidgets import QWidget, QMainWindow, QFrame, QFileDialog, QColorDialog

from editor.mundo.figuras_adicionales import Triangulo
from editor.mundo.mundo import Linea, Rectangulo, Ovalo, Dibujo
from editor.vista.ui.ui_MainWindowEditorDibujo import Ui_MainWindowEditorDibujo


class Canvas(QWidget):
    """
    Esta clase representa el lienzo donde se van a dibujar las figuras
    """

    def __init__(self, main_window):
        """
        Inicializa el lienzo de dibujo

        :param main_window: Referencia a la ventana principal que contiene el lienzo
        """
        QWidget.__init__(self)
        self.main_window: VentanaEditorDibujo = main_window
        self.setAutoFillBackground(True)

        # Pintar el fondo del widget de blanco
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.GlobalColor.white)
        self.setPalette(p)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            self.main_window.hacer_click(event.x(), event.y())

    def paintEvent(self, event: QPaintEvent) -> None:
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        self.main_window.dibujar(qp)

        # Pintar el punto seleccionado
        if self.main_window.hay_punto_seleccionado():
            x_sel = self.main_window.x_seleccionado
            y_sel = self.main_window.y_seleccionado
            brush = QBrush()
            brush.setColor(Qt.GlobalColor.green)
            brush.setStyle(Qt.BrushStyle.SolidPattern)
            qp.setBrush(brush)
            qp.drawEllipse(x_sel - 2, y_sel - 2, 3, 3)

        qp.end()


class VentanaEditorDibujo(QMainWindow):

    SELECCIONAR = 1
    DIBUJAR = 2
    NINGUNA = 0
    SIN_SELECCION = -1

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindowEditorDibujo()
        self.ui.setupUi(self)
        self.dibujo = Dibujo()
        self.canvas = Canvas(self)
        self.x_seleccionado = VentanaEditorDibujo.SIN_SELECCION
        self.y_seleccionado = VentanaEditorDibujo.SIN_SELECCION
        self.guardado = False
        self.configurar()
        self.show()

    def configurar(self):
        self.actualizar_titulo()

        # Agregar el lienzo a la ventana
        self.ui.canvas_container.setFrameStyle(QFrame.Shape.Panel | QFrame.Shadow.Sunken)
        self.ui.canvas_container.layout().addWidget(self.canvas)

        # Asignar el color por defecto para el fondo de las figuras
        paleta_fondo = self.ui.label_color_fondo.palette()
        paleta_fondo.setColor(QPalette.ColorRole.Window, Qt.GlobalColor.blue)
        self.ui.label_color_fondo.setPalette(paleta_fondo)

        # Asignar el color por defecto para la línea de las figuras
        paleta_linea = self.ui.label_color_linea.palette()
        paleta_linea.setColor(QPalette.ColorRole.Window, Qt.GlobalColor.black)
        self.ui.label_color_linea.setPalette(paleta_linea)

        # Enlazar eventos y señales de los controles
        self.ui.label_color_linea.mousePressEvent = self.seleccionar_color_linea
        self.ui.label_color_fondo.mousePressEvent = self.seleccionar_color_fondo
        self.ui.pbutton_borrar.clicked.connect(self.borrar_figura)
        self.ui.accion_guardar.triggered.connect(self.guardar_dibujo)
        self.ui.accion_abrir.triggered.connect(self.abrir_dibujo)
        self.ui.accion_salir.triggered.connect(lambda: QCoreApplication.exit(0))

    def actualizar_titulo(self):
        mod = "*" if self.dibujo.modificado else ""
        if self.dibujo.esta_guardado():
            titulo = f"Editor de dibujo - {self.dibujo.archivo} {mod}"
        else:
            titulo = f"Editor de dibujo - Sin nombre {mod}"

        self.setWindowTitle(titulo)

    def guardar_dibujo(self):
        if not self.dibujo.esta_guardado():
            file_name, _ = QFileDialog.getSaveFileName(self, "Guardar dibujo", "", "Dibujo (*.dibujo)",
                                                       "Dibujo (*.dibujo)")

            if file_name:
                self.dibujo.guardar(file_name)
        else:
            self.dibujo.guardar()
        self.actualizar_titulo()

    def abrir_dibujo(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Abrir dibujo", "", "Dibujo (*.dibujo)",
                                                   "Dibujo (*.dibujo)")
        if file_name:
            self.dibujo.cargar(file_name)

        self.actualizar_titulo()

    def hacer_click(self, x: int, y: int):
        acc = self.accion()
        if acc == VentanaEditorDibujo.SELECCIONAR:
            self.seleccionar(x, y)
        elif acc == VentanaEditorDibujo.DIBUJAR:
            if (self.x_seleccionado == VentanaEditorDibujo.SIN_SELECCION and
               self.y_seleccionado == VentanaEditorDibujo.SIN_SELECCION):
                self.x_seleccionado = x
                self.y_seleccionado = y
            else:
                self.agregar_figura(self.x_seleccionado, self.y_seleccionado, x, y)
                self.x_seleccionado = VentanaEditorDibujo.SIN_SELECCION
                self.y_seleccionado = VentanaEditorDibujo.SIN_SELECCION
        self.canvas.repaint()

    def accion(self):
        if self.ui.pbutton_seleccionar.isChecked():
            return VentanaEditorDibujo.SELECCIONAR
        elif self.ui.pbutton_linea.isChecked() or self.ui.pbutton_rect.isChecked() or self.ui.pbutton_ovalo.isChecked()\
                or self.ui.pbutton_triangulo.isChecked():
            return VentanaEditorDibujo.DIBUJAR
        else:
            return VentanaEditorDibujo.NINGUNA

    def tipo_linea(self):
        index = self.ui.combo_tipo_linea.currentIndex()
        if index == 0:
            return Qt.PenStyle.SolidLine
        elif index == 1:
            return Qt.PenStyle.DashLine
        else:
            return Qt.PenStyle.DotLine

    def borrar_figura(self):
        self.dibujo.borrar_figura_seleccionada()
        self.canvas.repaint()
        self.actualizar_titulo()

    def seleccionar(self, x: int, y: int):
        self.dibujo.intentar_seleccionar(x, y)
        self.canvas.repaint()
        self.actualizar_titulo()

    def seleccionar_color_fondo(self, event):
        paleta = self.ui.label_color_fondo.palette()
        color = QColorDialog.getColor(paleta.color(QPalette.ColorRole.Window))
        paleta.setColor(QPalette.ColorRole.Window, color)
        self.ui.label_color_fondo.setPalette(paleta)

    def seleccionar_color_linea(self, event):
        paleta = self.ui.label_color_linea.palette()
        color = QColorDialog.getColor(paleta.color(QPalette.ColorRole.Window))
        paleta.setColor(QPalette.ColorRole.Window, color)
        self.ui.label_color_linea.setPalette(paleta)

    def agregar_figura(self, x1: int, y1: int, x2: int, y2: int):
        p1 = QPoint(x1, y1)
        p2 = QPoint(x2, y2)
        c_linea = self.ui.label_color_linea.palette().color(QPalette.ColorRole.Window)
        c_fondo = self.ui.label_color_fondo.palette().color(QPalette.ColorRole.Window)
        ancho = self.ui.spin_ancho_linea.value()
        t_linea = self.tipo_linea()
        figura = None
        if self.ui.pbutton_linea.isChecked():
            figura = Linea(p1, p2, c_linea, t_linea, ancho)
        elif self.ui.pbutton_rect.isChecked():
            figura = Rectangulo(p1, p2, c_linea, t_linea, ancho, c_fondo)
        elif self.ui.pbutton_ovalo.isChecked():
            figura = Ovalo(p1, p2, c_linea, t_linea, ancho, c_fondo)
        elif self.ui.pbutton_triangulo.isChecked():
            figura = Triangulo(p1, p2, c_linea, t_linea, ancho, c_fondo)

        self.dibujo.agregar_figura(figura)
        self.canvas.repaint()
        self.actualizar_titulo()

    def dibujar(self, qp: QPainter):
        self.dibujo.dibujar(qp)

    def hay_punto_seleccionado(self) -> bool:
        return self.x_seleccionado != VentanaEditorDibujo.SIN_SELECCION \
               and self.y_seleccionado != VentanaEditorDibujo.SIN_SELECCION
