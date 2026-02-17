from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QMessageBox, QPushButton, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Qt6 Python Popup")
        self.resize(640, 360)

        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(16)

        label = QLabel("Pozdrav iz Qt6 aplikacije!")
        label.setStyleSheet("font-size: 22px;")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setMaximumWidth(420)

        popup_button = QPushButton("Otvori popup")
        popup_button.setStyleSheet("font-size: 18px; padding: 10px;")
        popup_button.setMaximumWidth(240)
        popup_button.clicked.connect(self.show_popup)

        layout.addWidget(label)
        layout.addWidget(popup_button)

        self.setCentralWidget(container)

    def show_popup(self) -> None:
        QMessageBox.information(self, "Popup", "Ovo je jednostavni Qt6 popup.")


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.showFullScreen()
    app.exec()
