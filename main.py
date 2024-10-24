import sys

from PySide6.QtWidgets import QApplication

from editor.vista.gui import VentanaEditorDibujo

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = VentanaEditorDibujo()
    sys.exit(app.exec())
