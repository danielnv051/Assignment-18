import sys
from functools import partial

from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

player = 1


def play(i, j):
    global player
    if player == 1:
        buttons[i][j].setText("X")
        player = 2
    elif player == 2:
        buttons[i][j].setText("O")
        player = 1


loader = QUiLoader()
app = QApplication([])
window = loader.load("ui.ui")

buttons = [
    [
        window.btn_1,
        window.btn_2,
        window.btn_3,
    ],
    [
        window.btn_4,
        window.btn_5,
        window.btn_6,
    ],
    [
        window.btn_7,
        window.btn_8,
        window.btn_9,
    ],
]

for i in range(3):
    for j in range(3):
        buttons[i][j].clicked.connect(partial(play, i, j))

window.show()
app.exec()
