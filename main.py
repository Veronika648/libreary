from PyQt6.QtWidgets import *
from search import*
import requests


app = QApplication([])
app.setStyleSheet("""
        QPushButton
        {
            border-style: groove;
            border-width: 5px;
            background-color: #735fff;
            border-color: #7500ff;
            border-radius: 7px;
            color: white;
            }
            
        QWidget
        {
            background: #9e6fff;
            }
        """)

window = QWidget()

mainline = QHBoxLayout()
v1 = QVBoxLayout()


name_lbl = QLabel("Введіть назву або автора книг")
name_input = QLineEdit()

search_btn = QPushButton('Пошук')

v1.addWidget(name_lbl)
v1.addWidget(name_input)
v1.addWidget(search_btn)
mainline.addLayout(v1)

mainline.addLayout(v1)
window.setLayout(mainline)



def open_window():
    print(name_input.text())
    search_window(name_input.text())
search_btn.clicked.connect(open_window)
window.show()
app.exec()