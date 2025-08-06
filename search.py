from PyQt6.QtWidgets import *
import requests

def search_window(q):

    window = QDialog()
    result = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={q}")
    print(result.json())
    window.show()

    window.exec()