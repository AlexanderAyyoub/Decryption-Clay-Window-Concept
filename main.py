import sys
import os
from pictureButton import *
from vigenereCipher import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QGraphicsDropShadowEffect, QTextEdit, QPlainTextEdit
from PyQt5.QtGui import QPixmap, QFont, QFontDatabase
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtCore import QSize

class BackgroundWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window attributes
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Get list of image filenames
        self.image_files = self.get_image_files()

        # Set initial index for image list
        self.current_index = 0

        # Initialize label attribute
        self.label = QLabel(self)

        # Initialize window
        self.init_ui()

        # Start cycling through images
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.cycle_backgrounds)
        self.timer.start(400)  # Change image every 2 seconds


        #setting font 
        fontFile = QFontDatabase.addApplicationFont("CooperFiveOpti-Black.otf")
        font_family = QFontDatabase.applicationFontFamilies(fontFile)[0]
        font = QFont(font_family)

        #drop shadow effect 
        effectK = QGraphicsDropShadowEffect()
        effectK.setOffset(4, 2)
        effectK.setBlurRadius(8)

        effectL = QGraphicsDropShadowEffect()
        effectL.setOffset(4, 2)
        effectL.setBlurRadius(8)

        effectR = QGraphicsDropShadowEffect()
        effectR.setOffset(4, 2)
        effectR.setBlurRadius(8)

        #textBox key 
        self.textboxKey = QLineEdit(self)   
        self.textboxKey.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: rgb(77,145,145); border: none; font-size: 42px;")
        self.textboxKey.move(110, 105)
        self.textboxKey.resize(320,100)
        self.textboxKey.setGraphicsEffect(effectK)
        self.textboxKey.setFont(font)
        self.textboxKey.setMaxLength(8)
        self.textboxKey.setPlaceholderText("Key")
        #textBox Left
        self.textboxLeft = QTextEdit(self)   
        self.textboxLeft.move(110, 265)
        self.textboxLeft.resize(320,200)
        self.textboxLeft.setPlaceholderText("Encoded Message Here")
        self.textboxLeft.setAcceptRichText(False)  # Disable rich text (optional)
        self.textboxLeft.setLineWrapMode(QTextEdit.WidgetWidth)  # Wrap text to widget width
        self.textboxLeft.setHorizontalScrollBarPolicy(1)  # Show horizontal scrollbar as needed
        self.textboxLeft.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)  # Show horizontal scrollbar as needed
        self.textboxLeft.setGraphicsEffect(effectL)
        self.textboxLeft.setFont(font)
        self.textboxLeft.setStyleSheet("""
            QTextEdit {
                background-color: rgba(0, 0, 0, 0);  /* Transparent background */
                color: rgb(77,145,145);
                border: none;
                font-size: 18px;
                
            }

            QTextEdit QScrollBar:vertical {
                border: none;
                background: transparent;
                width: 10px;
                margin: 3px 0 3px 0;
                border-radius: 2px;
            }

            QTextEdit QScrollBar::handle:vertical {   
                background-color: rgb(105, 196, 196);
                min-height: 5px;
                border-radius: 5px;
            }
            QTextEdit QScrollBar::handle:vertical:hover {   
                background-color: rgb(101, 183, 163);
            }
            QTextEdit QScrollBar::handle:vertical:pressed {   
                background-color: rgb(101, 183, 163);
            }

            QTextEdit QScrollBar::sub-line:vertical {
                border: none;
                background-color: transparent;
                height: 15px;
                border-top-left-radius: 7px;
                border-top-right-radius: 7px;
                subcontrol-position: top;
                subcontrol-origin: margin;
            }
            QTextEdit QScrollBar::sub-line:vertical:hover {   
                background-color: rgba(137, 255, 207,0);
            }
            QTextEdit QScrollBar::sub-line:vertical:pressed {   
                background-color: rgba(137, 255, 207,0);
            }

            QTextEdit QScrollBar::add-line:vertical {
                border: none;
                background-color: rgba(59, 59, 90,0);
                height: 15px;
                border-bottom-left-radius: 7px;
                border-bottom-right-radius: 7px;
                subcontrol-position: bottom;
                subcontrol-origin: margin;
            }
            QTextEdit QScrollBar::add-line:vertical:hover {   
                background-color: rgba(137, 255, 207,0);
            }
            QTextEdit QScrollBar::add-line:vertical:pressed {   
                background-color: rgba(137, 255, 207,0);
            }
        """)

        #textBox Right
        self.textboxRight = QTextEdit(self)   
        self.textboxRight.move(530, 265)
        self.textboxRight.resize(320,200)
        self.textboxRight.setPlaceholderText("Unencoded Message Here")
        self.textboxRight.setAcceptRichText(False)  # Disable rich text (optional)
        self.textboxRight.setLineWrapMode(QTextEdit.WidgetWidth)  # Wrap text to widget width
        self.textboxRight.setHorizontalScrollBarPolicy(1)  # Show horizontal scrollbar as needed
        self.textboxRight.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)  # Show horizontal scrollbar as needed
        self.textboxRight.setGraphicsEffect(effectR)
        self.textboxRight.setFont(font)
        self.textboxRight.setReadOnly(True)
        self.textboxRight.setStyleSheet("""
            QTextEdit {
                background-color: rgba(0, 0, 0, 0);  /* Transparent background */
                color: rgb(77,145,145);
                border: none;
                font-size: 18px;
                
            }

            QTextEdit QScrollBar:vertical {
                border: none;
                background: transparent;
                width: 10px;
                margin: 3px 0 3px 0;
                border-radius: 2px;
            }

            QTextEdit QScrollBar::handle:vertical {   
                background-color: rgb(105, 196, 196);
                min-height: 5px;
                border-radius: 5px;
            }
            QTextEdit QScrollBar::handle:vertical:hover {   
                background-color: rgb(101, 183, 163);
            }
            QTextEdit QScrollBar::handle:vertical:pressed {   
                background-color: rgb(101, 183, 163);
            }

            QTextEdit QScrollBar::sub-line:vertical {
                border: none;
                background-color: transparent;
                height: 15px;
                border-top-left-radius: 7px;
                border-top-right-radius: 7px;
                subcontrol-position: top;
                subcontrol-origin: margin;
            }
            QTextEdit QScrollBar::sub-line:vertical:hover {   
                background-color: rgba(137, 255, 207,0);
            }
            QTextEdit QScrollBar::sub-line:vertical:pressed {   
                background-color: rgba(137, 255, 207,0);
            }

            QTextEdit QScrollBar::add-line:vertical {
                border: none;
                background-color: rgba(59, 59, 90,0);
                height: 15px;
                border-bottom-left-radius: 7px;
                border-bottom-right-radius: 7px;
                subcontrol-position: bottom;
                subcontrol-origin: margin;
            }
            QTextEdit QScrollBar::add-line:vertical:hover {   
                background-color: rgba(137, 255, 207,0);
            }
            QTextEdit QScrollBar::add-line:vertical:pressed {   
                background-color: rgba(137, 255, 207,0);
            }
        """)

        #decryptButton
        pixmap = QPixmap("clayButton/1v2.png")
        pixmap_hover = QPixmap("clayButton/2v2.png")
        pixmap_pressed = QPixmap("clayButton/3.png")
        decryptButton = pictureButton(pixmap,pixmap_hover,pixmap_pressed,parent=self)
        decryptButton.setGeometry(150, 150, 150, 75)
        decryptButton.move(410,175)
        decryptButton.show()
        
        
        #decrypting info 
        decryptButton.clicked.connect(self.decrypt)
        

    def init_ui(self):
        # Set background image
        self.set_background()

    def get_image_files(self):
        """
        Get list of image filenames from the 'clayWindow' folder.
        """
        image_files = []
        folder_path = "clayWindow"
        for filename in os.listdir(folder_path):
            if filename.endswith(".png"):
                image_files.append(os.path.join(folder_path, filename))
        return sorted(image_files)

    def set_background(self):
        """
        Set background image.
        """
        pixmap = QPixmap(self.image_files[self.current_index])
        pixmap = pixmap.scaled(pixmap.width() // 2, pixmap.height() // 2, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.setFixedSize(pixmap.size())  # Set window size based on scaled image size

        # Set background image
        self.label.setPixmap(pixmap)
        self.label.setGeometry(0, 0, self.width(), self.height())

    def cycle_backgrounds(self):
        """
        Cycle through background images in a loop.
        """
        #print("Cycling images")  

        # Increment index
        self.current_index += 1
        if self.current_index >= len(self.image_files):
            self.current_index = 0

        # Update background image
        self.set_background()

    def decrypt(self):
        Key = self.textboxKey.text()
        cipherText = self.textboxLeft.toPlainText()
        Key = vigenereCipher.generateKey(self,cipherText,Key)
        cipher_instance = vigenereCipher(cipherText, Key, None)
        originalText = cipher_instance.originalText(cipherText, str(Key))
        self.textboxRight.setPlainText(originalText)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BackgroundWindow()
    window.show()
    sys.exit(app.exec_())
