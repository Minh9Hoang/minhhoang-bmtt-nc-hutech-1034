import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnencrypt.clicked.connect(self.encrypt)
        self.ui.btndecrypt.clicked.connect(self.decrypt)
    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/caesar/encrypt"
        payload = {
            "plaintext": self.ui.txtplaintext.toPlainText(),
            "key": self.ui.txtkey.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                return response.json()
                self.ui.txtciphertext.setPlainText(data["encrypted.message"])

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encryption Successful")
                msg.exec_()
            else:
                print("Error:")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)