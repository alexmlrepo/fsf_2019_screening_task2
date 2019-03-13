# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 00:33:32 2019

@author: fearlesssachin
"""

import sys, os, csv
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

class Form(QMainWindow):
     def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle('CSV Data plotting')
        self.create_menu()
     
     def create_menu(self):
        self.file_menu = self.menuBar().addMenu("&File")
        load_action = self.create_action("&Load file",
        shortcut="Ctrl+L", slot=self.load_file, tip="Load a file")
        quit_action = self.create_action("&Quit", slot=self.close,
        shortcut="Ctrl+Q", tip="Close the application")
    
        self.add_actions(self.file_menu,
        (load_action, None, quit_action))
    
        self.help_menu = self.menuBar().addMenu("&Help")
        about_action = self.create_action("&About",
        shortcut='F1', slot=self.on_about,
        tip='About the demo')
    
        self.add_actions(self.help_menu, (about_action,))
        
def main():
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()


if __name__ == "__main__":
    main()
    
            
            