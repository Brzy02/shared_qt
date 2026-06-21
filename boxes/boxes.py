from PySide6.QtWidgets import *
from PySide6.QtCore import *
from pydantic import BaseModel, ConfigDict
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


class SelectorOption(BaseModel, frozen=True):
    ConfigDict(frozen=True)
    name: str
    value: str | int


class SelectorBox(QWidget):
    def __init__(self, title: str = "") -> None:
        super().__init__()
        self.box = QGroupBox(title)
        self.box_layout = QHBoxLayout()
        self.box.setLayout(self.box_layout)
        self.frame = QFrame()
        self.frame.setFrameStyle(QFrame.StyledPanel | QFrame.Raised)
        self.frame.setLineWidth(3)
        self.frame.setMidLineWidth(3)
        self.frame_layout = QVBoxLayout()
        self.frame.setLayout(self.frame_layout)
        self.box_layout.addWidget(self.frame)

        # Widgets for this box
        self.select_all_button = QPushButton("Select All")
        self.select_all_button.clicked.connect(self.select_all)

        self.select_none_button = QPushButton("Select None")
        self.select_none_button.clicked.connect(self.select_none)

        self.select_list = QListWidget()

        self.frame_layout.addWidget(self.select_all_button)
        self.frame_layout.addWidget(self.select_none_button)
        self.frame_layout.addWidget(self.select_list)

        self.selectors: set[SelectorOption] = set()
        self.setLayout(self.box_layout)

    def add_selectors(self, options: list[SelectorOption]) -> None:
        for option in options:
            item = QListWidgetItem(option.name)
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            item.setCheckState(Qt.CheckState.Unchecked)
            self.select_list.addItem(item)
            self.selectors.add(option)

    def get_selected(self) -> set[SelectorOption]:
        if len(self.selectors) == 0:
            return [""]
        checked: set[SelectorOption] = set()
        selected = [
            self.select_list.item(i).text()
            for i in range(self.select_list.count())
            if self.select_list.item(i).checkState() == Qt.CheckState.Checked
        ]
        for selector in self.selectors:
            if selector.name in selected:
                checked.add(selector)

        print(checked)
        return checked

    def select_none(self) -> None:
        if len(self.selectors) == 0:
            return

        for i in range(self.select_list.count()):
            self.select_list.item(i).setCheckState(Qt.CheckState.Unchecked)

    def select_all(self) -> None:
        if len(self.selectors) == 0:
            return

        for i in range(self.select_list.count()):
            self.select_list.item(i).setCheckState(Qt.CheckState.Checked)


class SelectorDialog(QDialog):
    def __init__(self, options: list[SelectorOption], title: str = "Select") -> None:
        super().__init__()
        self.setWindowTitle(title)

        self.selector = SelectorBox(title)
        self.selector.add_selectors(options)

        self.buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)

        layout = QVBoxLayout()
        layout.addWidget(self.selector)
        layout.addWidget(self.buttons)
        self.setLayout(layout)

    def selected(self) -> set[SelectorOption]:
        return self.selector.get_selected()


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

        selector = SelectorDialog(
            options=[
                SelectorOption(name="Jeff", value=9),
                SelectorOption(name="Polly", value=4),
            ]
        )
        result = selector.exec()

        if result == QDialog.Accepted:
            selector.selected()

        main_layout.addWidget(selector)
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
