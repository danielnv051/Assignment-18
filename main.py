from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

def play():
    window.btn_1.setText("X")


loader = QUiLoader()
app = QApplication([])
window = loader.load("ui.ui")

window.btn_1.clicked.connect(play)

window.show()
app.exec()