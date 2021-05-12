import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Button(QPushButton):

    def __init__(self, color, *args, **kwargs):
        super().__init__(*args, **kwargs)
        color = QColor(color)
        shadow = color.darker(115).name()
        text = 'black' if color.value() > 186 else 'white'
        self.setStyleSheet(f'''
        QPushButton {{
            color: {text};
            background-color: {color.name()};
            padding: 12px;
            border-radius: 4px;
            border-bottom: 4px solid {shadow};
        }}''')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QScrollArea(widgetResizable=True)
    w = QWidget(); window.setWidget(w)
    grid = QGridLayout(w, spacing=40)
    colors = QColor.colorNames(); colors.remove('transparent')
    for i, v in enumerate(colors):
        grid.addWidget(Button(v, f'{v} button'.title()), *divmod(i, 7))
    window.show()
    sys.exit(app.exec_())