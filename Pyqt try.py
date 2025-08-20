import sys
from PyQt6 import QApplication, QWidget

class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle('Password Generator')

        self.generateButton = QPushButton('Generate Password', self)
        self.generateButton.clicked.connect(self.generate_password)

        self.passwordLabel = QLabel(self)
        self.passwordLabel.setWordWrap(True)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.generateButton)
        self.layout.addWidget(self.passwordLabel)

        self.setLayout(self.layout)

    def generate_password(self):
        password = generate_password(12)
        self.passwordLabel.setText(f'Generated Password: {password}')

def generate_password(length=12):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    if length < 12:
        print("Password length should be at least 12")
        return None

    password = ''.join(random.choice(all_characters) for i in range(length))
    
    return password

if __name__ == '__main__':
    app = QApplication(sys.argv)
    generator = PasswordGenerator()
    generator.show()
    sys.exit(app.exec_())

