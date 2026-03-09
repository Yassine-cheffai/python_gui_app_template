import sys
import time
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QProgressBar, QLabel
from PySide6.QtCore import QThread, Signal, QObject, Qt


# --- 1. THE WORKER (Business Logic) ---
class RetrievalWorker(QObject):
    finished = Signal()  # Signal when done
    progress = Signal(int)  # Signal to update UI bar

    def run(self):
        """Simulates retrieving data from cameras without freezing the UI."""
        for i in range(101):
            time.sleep(0.03)  # Simulate a delay (e.g., network request)
            self.progress.emit(i)
        self.finished.emit()


# --- 2. THE VIEW (UI Logic) ---
class CameraDashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Multi-Threaded Retrieval")
        self.resize(400, 200)
        layout = QVBoxLayout(self)

        self.btn_retrieve = QPushButton("Retrieve Data")
        self.pbar = QProgressBar()
        self.status_label = QLabel("Idle")

        layout.addWidget(self.btn_retrieve)
        layout.addWidget(self.pbar)
        layout.addWidget(self.status_label)

        # Connect button to the thread starter
        self.btn_retrieve.clicked.connect(self.start_retrieval)

    def start_retrieval(self):
        # Disable button so user doesn't click twice
        self.btn_retrieve.setEnabled(False)
        self.status_label.setText("Retrieving...")

        # --- 3. THREADING SETUP ---
        self.thread = QThread()
        self.worker = RetrievalWorker()

        # Move worker to the new thread
        self.worker.moveToThread(self.thread)

        # Connect Signals
        self.thread.started.connect(self.worker.run)
        self.worker.progress.connect(self.pbar.setValue)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.finished.connect(self.on_finished)

        # Start the thread
        self.thread.start()

    def on_finished(self):
        self.btn_retrieve.setEnabled(True)
        self.status_label.setText("Data Retrieval Complete!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CameraDashboard()
    window.show()
    sys.exit(app.exec())