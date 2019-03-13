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
        self.create_main_frame()
        
     def create_main_frame(self):
        self.main_frame = QWidget()

        plot_frame = QWidget()

        self.dpi = 100
        self.fig = Figure((6.0, 4.0), dpi=self.dpi)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self.main_frame)

        self.axes = self.fig.add_subplot(111)
        self.mpl_toolbar = NavigationToolbar(self.canvas, self.main_frame)

        log_label = QLabel("Data series:")
        self.series_list_view = QListView()
        self.series_list_view.setModel(self.series_list_model)

        spin_label1 = QLabel('X from')
        self.from_spin = QSpinBox()
        spin_label2 = QLabel('to')
        self.to_spin = QSpinBox()

        spins_hbox = QHBoxLayout()
        spins_hbox.addWidget(spin_label1)
        spins_hbox.addWidget(self.from_spin)
        spins_hbox.addWidget(spin_label2)
        spins_hbox.addWidget(self.to_spin)
        spins_hbox.addStretch(1)

        self.legend_cb = QCheckBox("Show L&egend")
        self.legend_cb.setChecked(False)

        self.show_button = QPushButton("&Show")
        # self.connect(self.show_button, SIGNAL('clicked()'), self.on_show)
        self.show_button.clicked.connect(self.on_show)

        left_vbox = QVBoxLayout()
        left_vbox.addWidget(self.canvas)
        left_vbox.addWidget(self.mpl_toolbar)

        right_vbox = QVBoxLayout()
        right_vbox.addWidget(log_label)
        right_vbox.addWidget(self.series_list_view)
        right_vbox.addLayout(spins_hbox)
        right_vbox.addWidget(self.legend_cb)
        right_vbox.addWidget(self.show_button)
        right_vbox.addStretch(1)

        hbox = QHBoxLayout()
        hbox.addLayout(left_vbox)
        hbox.addLayout(right_vbox)
        self.main_frame.setLayout(hbox)

        self.setCentralWidget(self.main_frame)
   
     
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
    
            
            