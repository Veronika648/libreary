from PyQt6.QtWidgets import *
from search import*


app = QApplication([])
window = QWidget()

mainline = QHBoxLayout()
v1 = QVBoxLayout()


name_lbl = QLabel("Введіть назву або автора книги")
name_input = QLineEdit()

search_btn = QPushButton('Пошук')

v1.addWidget(name_lbl)
v1.addWidget(name_input)
v1.addWidget(search_btn)
mainline.addLayout(v1)

mainline.addLayout(v1)
window.setLayout(mainline)

search_btn.clicked.connect(search_window)
window.show()
app.exec()