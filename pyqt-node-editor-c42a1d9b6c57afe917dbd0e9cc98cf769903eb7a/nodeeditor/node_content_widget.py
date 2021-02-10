from collections import OrderedDict
from nodeeditor.node_serializable import Serializable
from PyQt5.QtWidgets import *


class QDMNodeContentWidget(QWidget, Serializable):
    height_pp = 0  # 需要增加得高度

    def __init__(self, node, parent=None):
        self.node = node
        super().__init__(parent)

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        self.wdg_label = QLabel("Some Title")
        self.layout.addWidget(self.wdg_label)
        self.layout.addWidget(QDMTextEdit("foo"))

    def setEditingFlag(self, value):
        self.node.scene.getView().editingFlag = value

    def serialize(self):
        return OrderedDict([

        ])

    def deserialize(self, data, hashmap={}):
        return True


class QDMNodeContentWidgetInnerLayout(QDMNodeContentWidget):
    height_pp = 0  # 需要增加得高度
    m_input_sockets = {}
    m_output_sockets = {}
    inner_Layout=None

    def __init__(self, node, parent=None):
        self.m_input_sockets = {}
        self.m_output_sockets = {}
        self.inner_layout = QVBoxLayout()
        super().__init__(node, parent)
        self.setLayout(self.inner_layout)

    def getInnerWidgetPos(self, idx):
        posHeight = 60
        for i in range(idx):
            posHeight += self.inner_layout.itemAt(i).geometry().height() + self.inner_layout.spacing()
        return posHeight

    def configWidget(self, widget):
        # setcolor
        if self.inner_layout.count() % 2 == 0:
            widget.setStyleSheet("background-color:#4B4B4B;")
        else:
            widget.setStyleSheet("background-color:#242424;")
        height = widget.geometry().height()
        self.height_pp += height
        self.inner_layout.addWidget(widget)

    def selectionchange(self, i):
        self.node.id_matric = i


class QDMTextEdit(QTextEdit):
    def focusInEvent(self, event):
        self.parentWidget().setEditingFlag(True)
        super().focusInEvent(event)

    def focusOutEvent(self, event):
        self.parentWidget().setEditingFlag(False)
        super().focusOutEvent(event)
