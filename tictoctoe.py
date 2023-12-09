import sys
from functools import partial

from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader

player = 1
move = 0


def show_winner(game_board, symbol):
    global move
    winner = ""

    if winner == "":
        col1 = (
            game_board[0][0].text() + game_board[1][0].text() + game_board[2][0].text()
        )
        col2 = (
            game_board[0][1].text() + game_board[1][1].text() + game_board[2][1].text()
        )
        col3 = (
            game_board[0][2].text() + game_board[1][2].text() + game_board[2][2].text()
        )
        col4 = (
            game_board[0][0].text() + game_board[1][1].text() + game_board[2][2].text()
        )
        col5 = (
            game_board[0][2].text() + game_board[1][1].text() + game_board[2][0].text()
        )
        col6 = (
            game_board[0][0].text() + game_board[0][1].text() + game_board[0][2].text()
        )
        col7 = (
            game_board[1][0].text() + game_board[1][1].text() + game_board[1][2].text()
        )
        col8 = (
            game_board[2][0].text() + game_board[2][1].text() + game_board[2][2].text()
        )

        if (
            col1 == symbol * 3
            or col2 == symbol * 3
            or col3 == symbol * 3
            or col4 == symbol * 3
            or col5 == symbol * 3
            or col6 == symbol * 3
            or col7 == symbol * 3
            or col8 == symbol * 3
        ):
            winner = symbol

        elif move == 9:
            winner = "XO"

    return winner


def reset_game(game_board):
    for i in range(3):
        for j in range(3):
            game_board[i][j].setText("")
            game_board[i][j].setStyleSheet("background: #cacaca;color:transparent")
    window.xsign.setStyleSheet(
            "image: url(X.png);"
        )
    window.osign.setStyleSheet(
        "image: url(o1.png);"
    )


def play(i, j):
    global player
    global move
    move += 1

    if player == 1:
        buttons[i][j].setStyleSheet(
            "background: #cacaca url(X1.png) center center no-repeat;color:transparent"
        )
        window.xsign.setStyleSheet(
            "image: url(x1.png);"
        )
        window.osign.setStyleSheet(
            "image: url(O.png);"
        )
        buttons[i][j].setText("X")
        w = show_winner(buttons, "X")
        if w == "X":
            q = QMessageBox(text="برنده : بازیکن 1")
            q.show()
            q.exec()
            xscore = int(window.Xscore.text())
            xscore += 1
            window.Xscore.setText(str(xscore))
            reset_game(buttons)
        elif move == 9 and w == "XO":
            q = QMessageBox(text="مساوی")
            q.show()
            q.exec()
            reset_game(buttons)
        else:
            player = 2

    elif player == 2:
        buttons[i][j].setStyleSheet(
            "background: #cacaca url(O1.png) center center no-repeat;color:transparent"
        )
        window.xsign.setStyleSheet(
            "image: url(X.png);"
        )
        window.osign.setStyleSheet(
            "image: url(o1.png);"
        )
        buttons[i][j].setText("O")
        w = show_winner(buttons, "O")
        if w == "O":
            q = QMessageBox(text="برنده بازیکن 2")
            q.show()
            q.exec()
            oscore = int(window.Oscore.text())
            oscore += 1
            window.Oscore.setText(str(oscore))
            reset_game(buttons)
        elif move == 9 and w == "XO":
            q = QMessageBox(text="مساوی")
            q.show()
            q.exec()
            reset_game(buttons)
        else:
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
