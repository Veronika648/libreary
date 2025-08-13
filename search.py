from PyQt6.QtWidgets import *
import requests

def search_window(q):

    window = QDialog()
    

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


    v1.addLayout(h1)
    v1.addLayout(h2)
    v1.addLayout(h3)
    v1.addLayout(h4)
    h1.addWidget(title_lbl)
    h1.addWidget(title_output)
    h2.addWidget(authors_lbl)
    h2.addWidget(authors_output)
    h3.addWidget(page_lbl)
    h3.addWidget(page_output)
    h4.addWidget(description_lbl)
    h4.addWidget(description)
    mainline.addLayout(v1)

    mainline.addLayout(v1)
    window.setLayout(mainline)
    print(q)
    result = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={q}")
    result = result.json()

    films = result["items"]
    print(films[0])
    title_output.setText(films[0]["volumeInfo"]["title"])
    authors_output.setText(", ".join(films[0]["volumeInfo"]["authors"]))
    page_output.setText(str(films[0]["volumeInfo"]["pageCount"]))
    if "description" in films[0]["volumeInfo"]:
        description.setText(films[0]["volumeInfo"]["description"])




    window.show()

    window.exec()