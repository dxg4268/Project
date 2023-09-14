import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QMessageBox

class OptionPrompt(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Clinic')
        self.setGeometry(100, 100, 400, 300)

        # Create a central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create a layout for the central widget
        layout = QVBoxLayout()

        # Create buttons for each option
        options = {1:'Display', 2:'Search Record', 3:'Add Record', 4:'Delete Record', 5:'Modify Record', 6:'Graph'}
        for op,option in options.items():
            button = QPushButton(option)
            button.clicked.connect(lambda _, opt=op: self.perform_task(opt))
            layout.addWidget(button)

        # Set the layout for the central widget
        central_widget.setLayout(layout)

    def perform_task(self, opt):
        # Perform the task based on the selected option
        #QMessageBox.information(self, 'Task Result', f'Task for {option} has been performed.')
        if opt == 1:
            pass

        elif opt == 2:
            pass


def main():
    app = QApplication(sys.argv)
    window = OptionPrompt()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
