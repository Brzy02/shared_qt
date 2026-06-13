from PySide6.QtWidgets import *
from PySide6.QtCore import *

import sys


class VerticalBox(QWidget):
    def __init__(self, title: str = ""):
        super().__init__()

        self.box = QGroupBox(title)
        self.box_layout = QVBoxLayout()
        self.box.setLayout(self.box_layout)

        self.frame = QFrame()
        self.frame_layout = QVBoxLayout()
        self.frame.setLayout(self.frame_layout)

        self.box_layout.addWidget(self.frame)

        main = QVBoxLayout(self)
        main.addWidget(self.box)

    def add_widgets(self, widgets: list[QWidget]) -> None:

        for widget in widgets:
            self.frame_layout.addWidget(widget)


class HorizontalBox(QWidget):
    def __init__(self, title: str = ""):
        super().__init__()

        self.box = QGroupBox(title)
        self.box_layout = QVBoxLayout()
        self.box.setLayout(self.box_layout)

        self.frame = QFrame()
        self.frame_layout = QHBoxLayout()
        self.frame.setLayout(self.frame_layout)

        self.box_layout.addWidget(self.frame)

        # set the main widget that is passed
        main = QVBoxLayout(self)
        main.addWidget(self.box)

    def add_widgets(self, widgets: list[QWidget]) -> None:

        for widget in widgets:
            self.frame_layout.addWidget(widget)


class GridBox(QWidget):
    def __init__(self, title: str = ""):
        super().__init__()

        self.box = QGroupBox(title)
        self.box_layout = QVBoxLayout()
        self.box.setLayout(self.box_layout)

        # This will be the main stuff where the Widgets will be placed.
        self.frame = QFrame()
        self.frame_layout = QGridLayout()
        self.frame.setLayout(self.frame_layout)

        # Add the frame to the GroupBox. This will also add the layout.
        self.box_layout.addWidget(self.frame)

        # Set the main widget that will be passed.
        main = QVBoxLayout(self)
        main.addWidget(self.box)

    def add_widget(self, widget: QWidget, widget_row: int, widget_col: int) -> None:
        self.frame_layout.addWidget(widget, widget_row, widget_col)


# Example use cases for the boxes. Only example use cases
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        main_layout = QVBoxLayout()

        vertical_box = VerticalBox("Vertical box")
        vertical_box.add_widgets([QPushButton(), QLineEdit()])
        main_layout.addWidget(vertical_box)

        horizontal_box = HorizontalBox("Horizontal box")
        horizontal_box.add_widgets([QPushButton(), QLineEdit()])
        main_layout.addWidget(horizontal_box)

        grid_box = GridBox("Grid box")
        grid_box.add_widget(QPushButton(), 0, 4)
        grid_box.add_widget(QLineEdit(), 3, 0)
        main_layout.addWidget(grid_box)

        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
