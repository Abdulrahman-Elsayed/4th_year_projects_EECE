import sys
import os
from os import path, listdir
import random
from PyQt5.QtGui import QPalette, QColor, QPixmap, QImage, QIcon
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, 
    QPushButton, QVBoxLayout, QFileDialog, QProgressBar, QListWidget,
    QLabel, QMenuBar, QMenu, QListWidgetItem)
import qdarkstyle
from playsound import playsound
from PIL import Image
from PIL.ImageQt import ImageQt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() 
        self.resize(600, 700)
        self.setWindowTitle("Words Checker")
        self.setWindowIcon(QIcon('logo.png'))
        self.label1 = QLabel("Click select to select a test speaker and start.")     
        self.btn1 = QPushButton("Select")    
        self.btn2 = QPushButton("Reset")
        self.btn2.setEnabled(False)
        self.progressBar = QProgressBar()
        self.progressBar.setProperty("value", 0)
        self.listWidget = QListWidget()
        default_image = Image.new("RGB", (400, 400), (68, 83, 101))
        imageqt = ImageQt(default_image)
        self.pixmap = QPixmap.fromImage(imageqt)
        self.pixmap = self.pixmap.scaled(600, 280)
        self.label2 = QLabel()
        self.label2.setPixmap(self.pixmap)

        layout = QVBoxLayout()	
        layout.addWidget(self.label1) 		   
        layout.addWidget(self.btn1)       
        layout.addWidget(self.btn2)      
        layout.addWidget(self.progressBar)
        layout.addWidget(self.listWidget)
        layout.addWidget(self.label2)
        widget = QWidget()                        
        widget.setLayout(layout)                
        self.setCentralWidget(widget)

        self.btn1.clicked.connect(self.select)
        self.btn2.clicked.connect(self.reset)
        self.show()

    def select(self):
        directory_path = QFileDialog.getExistingDirectory(self)         
        directory_name = path.basename(directory_path)

        file_pathes = [path.join(os.getcwd(), file_path) 
            for file_path in listdir(directory_path)]
        file_names = [file_path
            for file_path in listdir(directory_path)]
        pairs_words = [(file_name[10:12], file_name[13]) for file_name in file_names]

        self.label1.setText(f'The test speaker is {directory_name}, click Reset to try again.')   
        self.btn1.setEnabled(False)
        self.btn2.setEnabled(True)

        for i in range(123):
            print(directory_path+'/'+file_names[i])


        ###############
        # this area is for the implementation code
        #
        # here you have access on those variables:
        # directory_path: string for the directory path that have the 123 segmentied .wav files
        # directory_name: string for the directory name that have the 123 segmentied .wav files
        # file_pathes:    list of strings of the pathes for the 123 segmentied .wav files
        # file_pathes:    list of strings of the names for the 123 segmentied .wav files
        # 
        # you must do the reference and test comparison here and produce a list
        # (named: self.correct) of 123 elements. each element is either a one or
        # a zero indicating whether the word was correct or wrong
        #
        # comment the below line and write your own code
        self.correct = [random.randrange(0, 2) for i in range(123)]
        ###############

        self.progressBar.setProperty("value", 100)

        for pair_word, c in zip(pairs_words, self.correct):
            if c:
                #item_text = f"Pair {pair_word[0]} word {pair_word[1]}\t\t\tCorrect       \U00002705"
                item_text = f"Pair {pair_word[0]} word {pair_word[1]}\t\t\t\U00002705 Correct"  
            else:
                #item_text = f"Pair {pair_word[0]} word {pair_word[1]}\t\t\tNot correct \U0000274C"
                item_text = f"Pair {pair_word[0]} word {pair_word[1]}\t\t\t\U0000274C Not correct"

            self.listWidget.addItem(QListWidgetItem(item_text))

        self.listWidget.itemClicked.connect(self.item_clicked)

    def item_clicked(self, item):
        print(item.text())
        correct_or_not = item.text()[19]
        if correct_or_not == 'C':   # the word is correct, display a white image
            default_image = Image.new("RGB", (400, 400), (68, 83, 101))
            imageqt = ImageQt(default_image)
        else:   # the word is not correct, display the distance image 
            pair = item.text()[5:7]
            word = item.text()[13]
            # function that takes pair and word and return image to display
            distance_image = self.getting_distance_image(pair, word)
            imageqt = ImageQt(distance_image) 
 
        self.pixmap = QPixmap.fromImage(imageqt)
        self.pixmap = self.pixmap.scaled(600, 280)
        self.label2.setPixmap(self.pixmap)

    def reset(self):   
        self.close()
        self.__init__()

    def getting_distance_image(self, pair, word):  
        ###############
        # to write by the implementation team
        # this function takes the pair and word of the wrong word
        # and return the distance image as a PIL Image object
        #
        # comment the below line and write your own.
        return Image.new("RGB", (400, 400))
        ###############

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
    sys.exit(app.exec_())
