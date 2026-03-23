from PySide6.QtCore import Qt

from src.screens.dashboard import DashboardScreen  # Import your class


def test_retrieval_button_updates_progress(qtbot):
    """
    :param qtbot:
    :return:
    """
    widget = DashboardScreen()
    qtbot.addWidget(widget)
    assert widget.progressBar.value() == 0
    qtbot.mouseClick(widget.btn_retrieve, Qt.LeftButton)

    # Wait: The thread takes time. We wait until the progress bar hits 100.
    # timeout is in milliseconds (e.g., 5000ms = 5s)
    qtbot.waitUntil(lambda: widget.progressBar.value() == 100, timeout=5000)
    assert widget.progressBar.value() == 100
    assert widget.btn_retrieve.text() == "Retrieval Done!"