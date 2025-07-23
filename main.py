from PyQt6.QtWidgets import *


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
window.show()
app.exec()