from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    """
    Main UI class that defines the structure and layout of the image processing application window.
    This class is typically auto-generated by Qt Designer and contains all UI element definitions.
    """
    def setupUi(self, MainWindow):
        """
        Sets up the main user interface of the application.
        
        Args:
            MainWindow: The main window widget to set up
        """
        # Configure main window properties
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)  # Set initial window size
        
        # Configure default font settings for the main window
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        
        # Create central widget (main container)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Image loading buttons
        # Button for loading the first image
        self.load_img1_ui = QtWidgets.QPushButton(self.centralwidget)
        self.load_img1_ui.setGeometry(QtCore.QRect(60, 180, 151, 61))
        self.load_img1_ui.setObjectName("load_img1_ui")
        
        # Button for loading the second image
        self.load_img2_ui = QtWidgets.QPushButton(self.centralwidget)
        self.load_img2_ui.setGeometry(QtCore.QRect(60, 330, 151, 61))
        self.load_img2_ui.setObjectName("load_img2_ui")
        
        # Setup vertical layout for image processing buttons
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(280, 140, 241, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        # Image Processing Buttons (Section 1)
        # Color separation button
        self.color_seperation_ui = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.color_seperation_ui.setObjectName("color_seperation_ui")
        self.verticalLayout.addWidget(self.color_seperation_ui)
        
        # Color transformation button
        self.color_transformation_ui = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.color_transformation_ui.setObjectName("color_transformation_ui")
        self.verticalLayout.addWidget(self.color_transformation_ui)
        
        # Color detection button
        self.color_detection_ui = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.color_detection_ui.setObjectName("color_detection_ui")
        self.verticalLayout.addWidget(self.color_detection_ui)
        
        # Image blending button
        self.blending_ui = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.blending_ui.setObjectName("blending_ui")
        self.verticalLayout.addWidget(self.blending_ui)
        
        # Setup vertical layout for image smoothing buttons
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(540, 140, 241, 311))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        # Image Smoothing Buttons (Section 2)
        # Gaussian blur button
        self.Gaussian_blur_ui = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.Gaussian_blur_ui.setObjectName("Gaussian_blur_ui")
        self.verticalLayout_2.addWidget(self.Gaussian_blur_ui)
        
        # Bilateral filter button
        self.Bilateral_filter_ui = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.Bilateral_filter_ui.setObjectName("Bilateral_filter_ui")
        self.verticalLayout_2.addWidget(self.Bilateral_filter_ui)
        
        # Median filter button
        self.Median_filter_ui = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.Median_filter_ui.setObjectName("Median_filter_ui")
        self.verticalLayout_2.addWidget(self.Median_filter_ui)
        
        # Section Labels
        # Image Processing section label
        self.image_processing = QtWidgets.QLabel(self.centralwidget)
        self.image_processing.setGeometry(QtCore.QRect(280, 110, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.image_processing.setFont(font)
        self.image_processing.setObjectName("image_processing")
        
        # Image Smoothing section label
        self.image_smoothing = QtWidgets.QLabel(self.centralwidget)
        self.image_smoothing.setGeometry(QtCore.QRect(540, 110, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.image_smoothing.setFont(font)
        self.image_smoothing.setObjectName("image_smoothing")
        
        # Labels for displaying image paths
        # Path display for Image 1
        self.img1_path = QtWidgets.QLabel(self.centralwidget)
        self.img1_path.setGeometry(QtCore.QRect(60, 250, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.img1_path.setFont(font)
        self.img1_path.setText("")
        self.img1_path.setObjectName("img1_path")
        
        # Path display for Image 2
        self.img2_path = QtWidgets.QLabel(self.centralwidget)
        self.img2_path.setGeometry(QtCore.QRect(60, 400, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.img2_path.setFont(font)
        self.img2_path.setText("")
        self.img2_path.setObjectName("img2_path")
        
        # Set up the central widget, menu bar, and status bar
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Connect signals and slots, and set up text translations
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """
        Sets up all the text elements in the UI.
        This method is used for internationalization support.
        
        Args:
            MainWindow: The main window widget containing all elements
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "2022 Opencvdl Hw1"))
        # Set text for image loading buttons
        self.load_img1_ui.setText(_translate("MainWindow", "Load Image 1"))
        self.load_img2_ui.setText(_translate("MainWindow", "Load Image 2"))
        # Set text for image processing buttons
        self.color_seperation_ui.setText(_translate("MainWindow", "1.1 Color Seperation"))
        self.color_transformation_ui.setText(_translate("MainWindow", "1.2 Color Transformation"))
        self.color_detection_ui.setText(_translate("MainWindow", "1.3 Color Detection"))
        self.blending_ui.setText(_translate("MainWindow", "1.4 Blending"))
        # Set text for image smoothing buttons
        self.Gaussian_blur_ui.setText(_translate("MainWindow", "2.1 Gaussian blur"))
        self.Bilateral_filter_ui.setText(_translate("MainWindow", "2.2 Bilateral filter"))
        self.Median_filter_ui.setText(_translate("MainWindow", "2.3 Median filter"))
        # Set text for section labels
        self.image_processing.setText(_translate("MainWindow", "1. Image Processing"))
        self.image_smoothing.setText(_translate("MainWindow", "2. Image Smoothing"))