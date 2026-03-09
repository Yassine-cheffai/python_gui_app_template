### start qt designer
```bash
uv run pyside6-designer  
```

### convert qt designer ui file to python file
```bash
uv run pyside6-uic dashboard.ui -o dashboard_ui.py
```

### build the app
```bash
uv run python -m nuitka --standalone \
                 --onefile \
                 --plugin-enable=pyside6 \
                 --include-qt-plugins=all \
                 --windows-disable-console \
                 --output-dir=dist \
                 src/main.py
```
