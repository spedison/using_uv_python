# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "pyqt5",
#     "requests<3",
#     "rich",
# ]
# ///

import sys
import time
from rich.progress import track
from tkinter import Tk, ttk

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout

for i in track(range(100), description="Processando ... :"):
    time.sleep(0.01)


import requests
from rich.pretty import pprint

resp = requests.get("https://peps.python.org/api/peps.json")
data = resp.json()
pprint([(k, v["title"]) for k, v in data.items()][:10])

print(".".join(map(str, sys.version_info[:3])))

root = Tk()
root.title("uv")
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World").grid(column=0, row=0)
root.mainloop()


app = QApplication(sys.argv)
widget = QWidget()
grid = QGridLayout()

text_label = QLabel()
text_label.setText("Hello World!")
grid.addWidget(text_label)

widget.setLayout(grid)
widget.setGeometry(100, 100, 200, 50)
widget.setWindowTitle("uv")
widget.show()
sys.exit(app.exec_())

