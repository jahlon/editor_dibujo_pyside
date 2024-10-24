# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowEditorDibujodymQzk.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLayout,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)
import editor.vista.ui.resources

class Ui_MainWindowEditorDibujo(object):
    def setupUi(self, MainWindowEditorDibujo):
        if not MainWindowEditorDibujo.objectName():
            MainWindowEditorDibujo.setObjectName(u"MainWindowEditorDibujo")
        MainWindowEditorDibujo.resize(800, 600)
        icon = QIcon()
        icon.addFile(u":/images/img/paint.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindowEditorDibujo.setWindowIcon(icon)
        self.accion_guardar = QAction(MainWindowEditorDibujo)
        self.accion_guardar.setObjectName(u"accion_guardar")
        icon1 = QIcon()
        icon1.addFile(u":/images/img/save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.accion_guardar.setIcon(icon1)
        self.accion_abrir = QAction(MainWindowEditorDibujo)
        self.accion_abrir.setObjectName(u"accion_abrir")
        icon2 = QIcon()
        icon2.addFile(u":/images/img/open.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.accion_abrir.setIcon(icon2)
        self.accion_salir = QAction(MainWindowEditorDibujo)
        self.accion_salir.setObjectName(u"accion_salir")
        icon3 = QIcon()
        icon3.addFile(u":/images/img/exit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.accion_salir.setIcon(icon3)
        self.container = QWidget(MainWindowEditorDibujo)
        self.container.setObjectName(u"container")
        self.horizontalLayout = QHBoxLayout(self.container)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.container)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setMaximumSize(QSize(70, 16777215))
        self.frame.setBaseSize(QSize(0, 0))
        self.frame.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Plain)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.pbutton_borrar = QPushButton(self.frame)
        self.pbutton_borrar.setObjectName(u"pbutton_borrar")
        icon4 = QIcon()
        icon4.addFile(u":/images/img/delete.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pbutton_borrar.setIcon(icon4)

        self.gridLayout.addWidget(self.pbutton_borrar, 10, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 9, 0, 1, 1)

        self.pbutton_linea = QPushButton(self.frame)
        self.buttonGroup = QButtonGroup(MainWindowEditorDibujo)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.pbutton_linea)
        self.pbutton_linea.setObjectName(u"pbutton_linea")
        self.pbutton_linea.setMaximumSize(QSize(16777215, 16777215))
        icon5 = QIcon()
        icon5.addFile(u":/images/img/linea.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pbutton_linea.setIcon(icon5)
        self.pbutton_linea.setCheckable(True)

        self.gridLayout.addWidget(self.pbutton_linea, 5, 0, 1, 1)

        self.spin_ancho_linea = QSpinBox(self.frame)
        self.spin_ancho_linea.setObjectName(u"spin_ancho_linea")
        self.spin_ancho_linea.setMaximum(10)

        self.gridLayout.addWidget(self.spin_ancho_linea, 14, 0, 1, 1)

        self.label_color_linea = QLabel(self.frame)
        self.label_color_linea.setObjectName(u"label_color_linea")
        self.label_color_linea.setMinimumSize(QSize(28, 29))
        self.label_color_linea.setAutoFillBackground(True)
        self.label_color_linea.setStyleSheet(u"")
        self.label_color_linea.setFrameShape(QFrame.Shape.Box)

        self.gridLayout.addWidget(self.label_color_linea, 13, 0, 1, 1)

        self.pbutton_seleccionar = QPushButton(self.frame)
        self.buttonGroup.addButton(self.pbutton_seleccionar)
        self.pbutton_seleccionar.setObjectName(u"pbutton_seleccionar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pbutton_seleccionar.sizePolicy().hasHeightForWidth())
        self.pbutton_seleccionar.setSizePolicy(sizePolicy1)
        self.pbutton_seleccionar.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        icon6 = QIcon()
        icon6.addFile(u":/images/img/cursor.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pbutton_seleccionar.setIcon(icon6)
        self.pbutton_seleccionar.setCheckable(True)
        self.pbutton_seleccionar.setChecked(True)

        self.gridLayout.addWidget(self.pbutton_seleccionar, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 11, 0, 1, 1)

        self.pbutton_ovalo = QPushButton(self.frame)
        self.buttonGroup.addButton(self.pbutton_ovalo)
        self.pbutton_ovalo.setObjectName(u"pbutton_ovalo")
        icon7 = QIcon()
        icon7.addFile(u":/images/img/circle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pbutton_ovalo.setIcon(icon7)
        self.pbutton_ovalo.setCheckable(True)

        self.gridLayout.addWidget(self.pbutton_ovalo, 7, 0, 1, 1)

        self.combo_tipo_linea = QComboBox(self.frame)
        self.combo_tipo_linea.addItem(icon5, "")
        icon8 = QIcon()
        icon8.addFile(u":/images/img/dashed.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.combo_tipo_linea.addItem(icon8, "")
        icon9 = QIcon()
        icon9.addFile(u":/images/img/puntos.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.combo_tipo_linea.addItem(icon9, "")
        self.combo_tipo_linea.setObjectName(u"combo_tipo_linea")

        self.gridLayout.addWidget(self.combo_tipo_linea, 15, 0, 1, 1)

        self.pbutton_rect = QPushButton(self.frame)
        self.buttonGroup.addButton(self.pbutton_rect)
        self.pbutton_rect.setObjectName(u"pbutton_rect")
        icon10 = QIcon()
        icon10.addFile(u":/images/img/rectangle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pbutton_rect.setIcon(icon10)
        self.pbutton_rect.setCheckable(True)

        self.gridLayout.addWidget(self.pbutton_rect, 6, 0, 1, 1)

        self.label_color_fondo = QLabel(self.frame)
        self.label_color_fondo.setObjectName(u"label_color_fondo")
        self.label_color_fondo.setMinimumSize(QSize(28, 29))
        self.label_color_fondo.setAutoFillBackground(True)
        self.label_color_fondo.setStyleSheet(u"")
        self.label_color_fondo.setFrameShape(QFrame.Shape.Box)

        self.gridLayout.addWidget(self.label_color_fondo, 12, 0, 1, 1)

        self.pbutton_triangulo = QPushButton(self.frame)
        self.buttonGroup.addButton(self.pbutton_triangulo)
        self.pbutton_triangulo.setObjectName(u"pbutton_triangulo")
        icon11 = QIcon()
        icon11.addFile(u":/images/img/triangle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pbutton_triangulo.setIcon(icon11)
        self.pbutton_triangulo.setCheckable(True)

        self.gridLayout.addWidget(self.pbutton_triangulo, 8, 0, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)

        self.horizontalLayout.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignTop)

        self.canvas_container = QFrame(self.container)
        self.canvas_container.setObjectName(u"canvas_container")
        self.canvas_container.setAutoFillBackground(False)
        self.canvas_container.setStyleSheet(u"")
        self.canvas_container.setFrameShape(QFrame.Shape.Panel)
        self.canvas_container.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout = QVBoxLayout(self.canvas_container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.canvas_container)

        MainWindowEditorDibujo.setCentralWidget(self.container)
        self.menuBar = QMenuBar(MainWindowEditorDibujo)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 800, 22))
        self.menuArchivo = QMenu(self.menuBar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindowEditorDibujo.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.accion_guardar)
        self.menuArchivo.addAction(self.accion_abrir)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.accion_salir)

        self.retranslateUi(MainWindowEditorDibujo)

        QMetaObject.connectSlotsByName(MainWindowEditorDibujo)
    # setupUi

    def retranslateUi(self, MainWindowEditorDibujo):
        MainWindowEditorDibujo.setWindowTitle(QCoreApplication.translate("MainWindowEditorDibujo", u"Editor de dibujo", None))
        self.accion_guardar.setText(QCoreApplication.translate("MainWindowEditorDibujo", u"Guardar dibujo", None))
        self.accion_abrir.setText(QCoreApplication.translate("MainWindowEditorDibujo", u"Abrir dibujo", None))
        self.accion_salir.setText(QCoreApplication.translate("MainWindowEditorDibujo", u"Salir", None))
#if QT_CONFIG(tooltip)
        self.pbutton_borrar.setToolTip(QCoreApplication.translate("MainWindowEditorDibujo", u"Borrar figura seleccionada", None))
#endif // QT_CONFIG(tooltip)
        self.pbutton_borrar.setText("")
#if QT_CONFIG(tooltip)
        self.pbutton_linea.setToolTip(QCoreApplication.translate("MainWindowEditorDibujo", u"L\u00ednea", None))
#endif // QT_CONFIG(tooltip)
        self.pbutton_linea.setText("")
#if QT_CONFIG(tooltip)
        self.spin_ancho_linea.setToolTip(QCoreApplication.translate("MainWindowEditorDibujo", u"Ancho de l\u00ednea", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_color_linea.setToolTip(QCoreApplication.translate("MainWindowEditorDibujo", u"Color de l\u00ednea", None))
#endif // QT_CONFIG(tooltip)
        self.label_color_linea.setText("")
#if QT_CONFIG(tooltip)
        self.pbutton_seleccionar.setToolTip(QCoreApplication.translate("MainWindowEditorDibujo", u"Seleccionar", None))
#endif // QT_CONFIG(tooltip)
        self.pbutton_seleccionar.setText("")
#if QT_CONFIG(tooltip)
        self.pbutton_ovalo.setToolTip(QCoreApplication.translate("MainWindowEditorDibujo", u"\u00d3valo", None))
#endif // QT_CONFIG(tooltip)
        self.pbutton_ovalo.setText("")
        self.combo_tipo_linea.setItemText(0, "")
        self.combo_tipo_linea.setItemText(1, "")
        self.combo_tipo_linea.setItemText(2, "")

#if QT_CONFIG(tooltip)
        self.combo_tipo_linea.setToolTip(QCoreApplication.translate("MainWindowEditorDibujo", u"Tipo de l\u00ednea", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbutton_rect.setToolTip(QCoreApplication.translate("MainWindowEditorDibujo", u"Rect\u00e1ngulo", None))
#endif // QT_CONFIG(tooltip)
        self.pbutton_rect.setText("")
#if QT_CONFIG(tooltip)
        self.label_color_fondo.setToolTip(QCoreApplication.translate("MainWindowEditorDibujo", u"Color de fondo", None))
#endif // QT_CONFIG(tooltip)
        self.label_color_fondo.setText("")
        self.pbutton_triangulo.setText("")
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindowEditorDibujo", u"Archivo", None))
    # retranslateUi

