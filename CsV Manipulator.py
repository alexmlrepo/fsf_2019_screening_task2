# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 09:32:54 2019

@author: fearlesssachin
"""
import sys
import os
import csv
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidget, QApplication, QMainWindow, QTableWidgetItem, QFileDialog,QPushButton
from PyQt5.QtWidgets import qApp, QAction
from mpl_qtwidgets import Form 

class MyTable(QTableWidget):
    def __init__(self, r, c):
        super().__init__(r, c)
        self.check_change = True
        self.init_ui()

    def init_ui(self):
        self.cellChanged.connect(self.c_current)
        self.show()

    def c_current(self):
        if self.check_change:
            row = self.currentRow()
            col = self.currentColumn()
            value = self.item(row, col)
            value = value.text()
            print("The current cell is ", row, ", ", col)
            print("In this cell we have: ", value)