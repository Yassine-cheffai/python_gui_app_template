import sys
from PySide6.QtWidgets import QApplication
from src.screens.dashboard import  DashboardScreen

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DashboardScreen()
    window.show()
    sys.exit(app.exec())