from PyQt6.QtWidgets import *
import requests

def search_window(q):

    window = QDialog()
    #result = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={q}")
    #print(result.json())



    mainline = QHBoxLayout()
    v1 = QVBoxLayout()
    h1 = QVBoxLayout()
    h2 = QVBoxLayout()
    h3 = QVBoxLayout()
    h4 = QVBoxLayout()

    title_lbl = QLabel("Назва:")
    authors_lbl = QLabel("Автор:")
    page_lbl = QLabel("Кількість сторінок:")
    description_lbl = QLabel("Опис:")
    title_output = QLineEdit()
    authors_output = QLineEdit()
    page_output = QLineEdit()
    description = QTextEdit()


    v1.addWidget(h1, h2, h3, h4)
    h1.addWidget(title_lbl)
    h2.addWidget(authors_lbl)
    h3.addWidget(page_lbl)
    h4.addWidget(description_lbl)
    mainline.addLayout(v1)

    mainline.addLayout(v1)
    window.setLayout(mainline)





    window.show()

    window.exec()