from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image, ImageGrab
from tkinter import filedialog
from tkinter import *
import sys
import os
import PIL.Image
import pytesseract
import numpy as np
import clipboard
import random
from pynput import mouse
from pynput.keyboard import Key, Listener

themes = ['#2EDAA1', '#31BBD7', '#4D5BE1', '#EA4282', '#9D4AE2']
theme_color = random.choice(themes)
x = 1
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\SATISH SHAH\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        #MAIN WINDOW
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 490)
        MainWindow.setStyleSheet("background-color: white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setWindowIcon(QtGui.QIcon(r'C:\Users\SATISH SHAH\Desktop\Gaurav Shah\Projects\Coding\icon.png'))

        #IMAGE PREVIEW BOX
        self.Image_Preview = QtWidgets.QLabel(self.centralwidget)
        self.Image_Preview.setGeometry(QtCore.QRect(20, 59, 441, 271))
        self.Image_Preview.setCursor(QtGui.QCursor(QtCore.Qt.SizeAllCursor))
        self.Image_Preview.setStyleSheet("background-color: #eeeeee;")
        self.Image_Preview.setText("")
        self.Image_Preview.setObjectName("Image_Preview")

        #FILE PATH TEXT EDIT
        self.File_path = QtWidgets.QLineEdit(self.centralwidget)
        self.File_path.setGeometry(QtCore.QRect(20, 20, 371, 21))
        #self.File_path.setStyleSheet("border-radius:1px;")
        font = QtGui.QFont()
        font.setFamily("Montserrat Thin")
        font.setPointSize(7)
        self.File_path.setFont(font)
        self.File_path.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.File_path.setObjectName("File_path")

        # OPEN FILE PATH
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 20, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Thin")
        font.setPointSize(7)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border-radius: 1px;\n"
        "background-color: #f4f4f4;")
        self.pushButton.setObjectName("pushButton")

        #COPY TEXT BUTTON
        self.Copy_Text_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Copy_Text_Button.setGeometry(QtCore.QRect(350, 440, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(9)
        self.Copy_Text_Button.setFont(font)
        self.Copy_Text_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Copy_Text_Button.setStyleSheet("border-radius: 15px;\n"
        "background-color: "+theme_color+";\n"
        "color: white;")
        self.Copy_Text_Button.setObjectName("Copy_Text_Button")

        #CLEAR BUTTON
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(270, 440, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat Light")
        font.setPointSize(9)
        self.clear_button.setFont(font)
        self.clear_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clear_button.setStyleSheet("border-radius: 15px;\n"
        "background-color: #f4f4f4;")
        self.clear_button.setObjectName("clear_button")

        #DO NOT SAVE IMAGE CHECKBOX
        self.Save_image_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.Save_image_checkbox.setGeometry(QtCore.QRect(20, 440, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(9)
        self.Save_image_checkbox.setFont(font)
        self.Save_image_checkbox.setObjectName("Save_image_checkbox")


        #SETS PREVIEW IMAGE_____________________________________________
        
        
        

        #_______________________________________________________________        
        

        #EXTRACTED TEXT
        self.Extracted_text = QtWidgets.QTextEdit(self.centralwidget)
        self.Extracted_text.setGeometry(QtCore.QRect(480, 20, 500, 451))
        self.Extracted_text.setStyleSheet("padding: 5px;")
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(10)
        self.Extracted_text.setFont(font)
        self.Extracted_text.setAutoFormatting(QtWidgets.QTextEdit.AutoAll)
        self.Extracted_text.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.Extracted_text.setObjectName("Extracted_text")

        #EXTRACTED TEXT LABEL
        self.Extracted_text_label = QtWidgets.QLabel(self.centralwidget)
        self.Extracted_text_label.setGeometry(QtCore.QRect(30, 70, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Avenir LT Std 35 Light")
        font.setPointSize(9)
        self.Extracted_text_label.setFont(font)
        self.Extracted_text_label.setStyleSheet("color:  "+theme_color+"; padding-left: 5px;")
        self.Extracted_text_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Extracted_text_label.setObjectName("Extracted_text_label")

        #MESSAGES FROM PROGRAM
        self.Messages = QtWidgets.QTextEdit(self.centralwidget)
        self.Messages.setGeometry(QtCore.QRect(20, 350, 441, 71))
        font = QtGui.QFont()
        font.setFamily("Montserrat Light")
        font.setPointSize(10)
        self.Messages.setFont(font)
        self.Messages.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.Messages.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.Messages.setStyleSheet("color:  "+theme_color+";")
        self.Messages.setAcceptRichText(False)
        self.Messages.setObjectName("Messages")

        #PASTE IMAGE BUTTON
        self.Paste_Image_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Paste_Image_Button.setGeometry(QtCore.QRect(390, 70, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(9)
        self.Paste_Image_Button.setFont(font)
        self.Paste_Image_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Paste_Image_Button.setStyleSheet("border-radius: 15px;\n"  
        "background-color: "+theme_color+"; color: white;")
        self.Paste_Image_Button.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Paste_Image_Button.setObjectName("Paste_Image_Button")

        #.PNG BUTTON
        self.png_label = QtWidgets.QPushButton(self.centralwidget)
        self.png_label.setGeometry(QtCore.QRect(920, 440, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(9)
        self.png_label.setFont(font)
        self.png_label.setStyleSheet("border-radius: 15px;\n"
        "background-color: white; color:  "+theme_color+";")
        self.png_label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Extracted_text_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.png_label.setObjectName("png_label")

        #RANDOM STUFF
        self.pushButton.raise_()
        self.File_path.raise_()
        self.Save_image_checkbox.raise_()
        self.Image_Preview.raise_()
        self.Extracted_text.raise_()
        self.Copy_Text_Button.raise_()
        self.Extracted_text_label.raise_()
        self.Messages.raise_()
        self.Paste_Image_Button.raise_()
        self.png_label.raise_()
        self.clear_button.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def paste_image(self):
        global x

        #VARIABLES
        filepath = self.File_path.text()
        
        self.Messages.setStyleSheet("color:  "+theme_color+";")
        save_name = str(x)+'.png'

        #IN CASE FILE PATH IS NOT ENTERED
        if filepath == "No File Path Selected":
            filepath = r'C:\Users\SATISH SHAH\Desktop\Gaurav Shah\Projects\OCR resources\Misc'
            self.Messages.setText("A file path has not been entered. By default, the image and text will not be saved.")
            

        #FOR NORMAL CASES
        else:
            pass

        try:
            if self.Messages.toPlainText() == "An error has occured.":
                self.png_label.setText('')
                self.Extracted_text.setText('')
                self.Messages.setText('')
                self.Image_Preview.clear()
            else:
                pass
            
            self.Messages.setText("")
            def getPostion():
                def on_click(x, y, button, pressed):
                    global Click_x, Click_y, Release_x, Release_y, STOP
                    if pressed:
                        Click_x = x
                        Click_y = y
                    else:
                        Keyboardlistener.stop()
                        Release_x = x
                        Release_y = y
                        STOP = False
                        return False

                def on_release(key):
                    global STOP
                    if key == Key.esc:
                        Mouselistener.stop()
                        STOP = True
                        return False

                with mouse.Listener(on_click=on_click) as Mouselistener, Listener(on_release=on_release) as Keyboardlistener:
                    Mouselistener.join()
                    Keyboardlistener.join()

            getPostion()
            print(Click_x, Click_y, Release_x, Release_y)
            im = ImageGrab.grab(bbox =(Click_x, Click_y, Release_x, Release_y))
            filepath = filepath.replace('\\', '/')
            image_path = filepath+'/'+str(save_name)
            im.save(image_path,'PNG')
            img_open = PIL.Image.open(image_path)

            #SET PREVIEW IMAGE
            
            self.Image_Preview.setPixmap(QtGui.QPixmap(image_path))
            self.Image_Preview.setScaledContents(True)

            #OCR
            
            np_img = np.array(img_open)
            text = pytesseract.image_to_string(np_img)

            #PREVENT NEXT LINE
            text = text.replace('\n\n', '&&&')
            text = text.replace('\n', ' ')
            text = text.replace('&&&', '\n\n')
            
            self.Extracted_text.setText(text[:-1])

            #COPY TEXT
            clipboard.copy(text[:-1])
            self.Copy_Text_Button.setText('Copied!')
            self.Messages.setText("OCR Complete.\nText Copied. Click clear.")



            #UPDATING SAVE INFORMATION             
            x = int(x)+ 1            

            if self.Save_image_checkbox.isChecked():
                os.remove(image_path) 
            else:
                self.png_label.setText(str(x - 1)+'.png')

        except:
            self.Messages.setText("An error has occured.")
            self.Messages.setStyleSheet("color:  #DD0000;")

    def clear(self):
        filepath = self.File_path.text()
        if filepath != "No File Path Selected":
            filepath = filepath.replace('\\', '/')

            text = self.Extracted_text.toPlainText()
            
            #APPEND TO TEXT FILE FOR SAFE KEEPING
            file_object = open(filepath+'/Notes.txt', 'a')
            file_object.write(text+'\n_____________________________________________________________________________________\n')
            file_object.close()
        else:
            self.Messages.setText("An error has occured.")
                
        self.png_label.setText('')
        self.Extracted_text.setText('')
        self.Messages.setText('')
        self.Image_Preview.clear()

    def open_image(self):
        if self.Save_image_checkbox.isChecked():
            pass
        else:
            filepath = self.File_path.text()
            save_name = str(x-1)+'.png'
            filepath = filepath.replace('\\', '/')
            image_path = filepath+'/'+str(save_name)
            im = PIL.Image.open(image_path)
            im.show()
        

    def copy(self):
        text = self.Extracted_text.toPlainText()
        if text != "":
            clipboard.copy(text[:-1])
            self.Messages.setText("Text Copied.")
        else:
            self.Messages.setText("Text has not been extracted.")

    def open_folder(self):
        self.Save_image_checkbox.setChecked(False)
        root = Tk()
        root.withdraw()
        file = filedialog.askdirectory()
        self.File_path.setText(file)

    def change_x(self):
        global x
        file_numbers = []
        try:
            filepath = self.File_path.text()
            files = os.listdir(filepath)
            for file in files:
                if '.png' in file:
                    file = int(file.replace('.png', ''))
                    file_numbers.append(file)
                else:
                    files.remove(file)
            file_numbers.sort()
            print(file_numbers)
            x = file_numbers[-1]
            x = x+1
            print(x)
        except:
            print('hi')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OCR - By Gaurav Shah"))
        self.Copy_Text_Button.setText(_translate("MainWindow", "Copy Text"))
        self.Save_image_checkbox.setText(_translate("MainWindow", "Do not save image"))
        self.Save_image_checkbox.setChecked(True)
        self.File_path.setText(_translate("MainWindow", "No File Path Selected")) #Text also used on line 183
        self.pushButton.setText(_translate("MainWindow", "Open"))
        self.Extracted_text.setText(_translate("MainWindow", ""))
        self.Extracted_text_label.setText(_translate("MainWindow", "Image Preview:"))
        self.Messages.setToolTip(_translate("MainWindow", "Messages"))
        self.Messages.setWhatsThis(_translate("MainWindow", "Messages"))
        self.Messages.setText(_translate("MainWindow", ""))
        self.Paste_Image_Button.setText(_translate("MainWindow", "Snip"))
        self.clear_button.setText(_translate("MainWindow", "Save"))

        self.Paste_Image_Button.clicked.connect(self.clear)
        self.Paste_Image_Button.clicked.connect(self.paste_image)
        self.png_label.clicked.connect(self.open_image)
        self.Copy_Text_Button.clicked.connect(self.copy)
        self.clear_button.clicked.connect(self.clear)
        self.pushButton.clicked.connect(self.open_folder)
        self.pushButton.clicked.connect(self.change_x)

        print('functions')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6 )  
