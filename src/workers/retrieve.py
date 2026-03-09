from src.services.retrieve import  retrieve
from PySide6.QtCore import Signal, QObject

class RetrievalWorker(QObject):
    finished = Signal()  # Signal when done
    progress = Signal(int)  # Signal to update UI bar

    def run(self):
        """Simulates retrieving data from cameras without freezing the UI."""
        for i in range(101):
            retrieve()
            self.progress.emit(i)
        self.finished.emit()
