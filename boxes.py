from PySide6.QtWidgets import *
from PySide6.QtCore import *

import sys
class VerticalBox(QWidget):
    def __init__(self):
        super().__init__()
        
        self.box= QGroupBox()
        self.box_layout= QVBoxLayout()
        self.frame = QFrame()
        self.frame_layout = QVBoxLayout()
        self.frame.setLayout(self.frame_layout)
        self.box_layout.addWidget(self.frame)
        self.box.setLayout(self.box_layout)
        
    def add_widgets(self, widgets:list[QWidget])-> None:
        
        for widget in widgets:
            self.frame_layout.addWidget(widget)
    
    def get_box(self)->QGroupBox:
        return self.box
        
class HorizontalBox(QWidget):
    def __init__(self):
        super().__init__()
        
        self.box= QGroupBox()
        self.box_layout= QHBoxLayout()
        self.frame = QFrame()
        self.frame_layout = QHBoxLayout()
        self.frame.setLayout(self.frame_layout)
        self.box_layout.addWidget(self.frame)
        self.box.setLayout(self.box_layout)
        
    def add_widgets(self, widgets:list[QWidget])-> None:
        
        for widget in widgets:
            self.frame_layout.addWidget(widget)
    
    def get_box(self)->QGroupBox:
        return self.box
    