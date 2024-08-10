import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QVBoxLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        
        self.line_edit = QLineEdit(self)
        self.line_edit.setPlaceholderText('Nhập tên của bạn')
        
        self.button = QPushButton('Hiển thị', self)
        self.button.clicked.connect(self.show_name)
        self.label = QLabel('', self)

        layout = QVBoxLayout()
        layout.addWidget(self.line_edit)
        layout.addWidget(self.button)
        layout.addWidget(self.label)

        self.setLayout(layout)

        
        self.setWindowTitle('Hiển Thị Tên')
        self.setGeometry(100, 100, 300, 200)

    def show_name(self):
       
        name = self.line_edit.text()
        self.label.setText(f'Tên của bạn là: {name}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())