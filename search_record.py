# delete_data.py

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QFormLayout

class InputWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Input Window")
        self.setGeometry(100, 100, 400, 200)

        self.DocID_label = QLabel("Enter DocID Search Criteria:")
        self.DocID_input = QLineEdit()
        self.submit_button = QPushButton("Submit")

        layout = QFormLayout()
        layout.addRow(self.DocID_label, self.DocID_input)
        layout.addRow(self.submit_button)

        self.setLayout(layout)

        self.submit_button.clicked.connect(self._query)

    def _query(self):
        docID = self.DocID_input.text()
        table = "Emp" 
        q = f"select * from {table} where DocID={docID};"

        #cr.execute(q)
        #data = cr.fetchall()
        #if data:
            #print("Entry Found!")
            #print(data)
        #else:
            #print("Entry Not found!")

        print(q)
        self.close()  # Close the window after saving the data

def main():
    app = QApplication(sys.argv)
    window = InputWindow()
    window.show()
    app.exec_()  # Do not use sys.exit(app.exec_()) to allow the main program to continue

if __name__ == "__main__":
    main()

