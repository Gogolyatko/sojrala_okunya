from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMessageBox, QRadioButton
app = QApplication([])
win = QWidget()


win.setWindowTitle("гусь усрусь")
win.resize(500, 200)
q = QLabel(win)
q.setText("Кого я схавала уже")
q.move(200,10)
b = QRadioButton(win)
b.setText("Окуня")
b.move(150,60)
bb = QRadioButton(win)
bb.setText("bbb")
bb.move(300, 60)
bbbb = QRadioButton(win)
bbbb.setText("Карпа")
bbbb.move(150, 100)
bbbbb = QRadioButton(win)
bbbbb.setText("Крысу")
bbbbb.move(300, 100)

def show_win():
    win2 = QMessageBox()
    win2.setText("Нет, я всех сожрала. Вы выиграли труп Сигмы в виде окуня.")
    win2.exec_()

b.clicked.connect(show_win)
bb.clicked.connect(show_win)
bbbb.clicked.connect(show_win)
bbbbb.clicked.connect(show_win)

win.show()
app.exec_()