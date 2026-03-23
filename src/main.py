import sys
from PySide6.QtWidgets import QApplication
import qdarktheme

from src.screens.dashboard import  DashboardScreen

if __name__ == "__main__":
    app = QApplication(sys.argv)
    qdarktheme.setup_theme()
    window = DashboardScreen()
    window.show()
    sys.exit(app.exec())