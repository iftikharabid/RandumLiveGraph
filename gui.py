from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_livePlot = QPushButton(self.centralwidget)
        self.pushButton_livePlot.setGeometry(QRect(50, 270, 241, 141))
        self.pushButton_livePlot.setObjectName("pushButton_livePlot")
        self.save_checkbox = QCheckBox(self.centralwidget)
        self.save_checkbox.setGeometry(QRect(340, 460, 97, 22))
        self.save_checkbox.setObjectName("save_checkbox")
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QRect(110, 0, 621, 91))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_manual_thresh = QLineEdit(self.centralwidget)
        self.lineEdit_manual_thresh.setGeometry(QRect(300, 120, 113, 27))
        self.lineEdit_manual_thresh.setText("")
        self.lineEdit_manual_thresh.setObjectName("lineEdit_manual_thresh")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setGeometry(QRect(290, 90, 251, 21))

 
        self.label_2.setObjectName("label_2")
        self.pushButton_setManual = QPushButton(self.centralwidget)
        self.pushButton_setManual.setGeometry(QRect(420, 120, 98, 27))
        self.pushButton_setManual.setObjectName("pushButton_setManual")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setGeometry(QRect(390, 160, 71, 17))
        self.label_3.setObjectName("label_3")
        self.pushButton_asst = QPushButton(self.centralwidget)
        self.pushButton_asst.setGeometry(QRect(300, 190, 221, 27))
        self.pushButton_asst.setObjectName("pushButton_asst")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setGeometry(QRect(50, 460, 271, 17))
        self.label_4.setObjectName("label_4")
        self.lineEdit_save_file = QLineEdit(self.centralwidget)
        self.lineEdit_save_file.setGeometry(QRect(50, 490, 191, 27))
        self.lineEdit_save_file.setObjectName("lineEdit_save_file")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setGeometry(QRect(250, 480, 441, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setGeometry(QRect(300, 310, 181, 51))
        self.label_6.setObjectName("label_6")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setGeometry(QRect(250, 510, 291, 16))
        self.label_7.setObjectName("label_7")
        self.pushButton_stopTracking = QPushButton(self.centralwidget)
        self.pushButton_stopTracking.setGeometry(QRect(520, 300, 161, 71))
        self.pushButton_stopTracking.setObjectName("pushButton_stopTracking")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("MainWindow")
        self.pushButton_livePlot.setText("Start Live Plot")
        self.save_checkbox.setText("Yes")
        self.label.setText("Random Live Graph")
        self.label_2.setText("Set Threshold Magnitude:")
        self.pushButton_setManual.setText("Set Manually")
        self.label_3.setText("OR")
        self.pushButton_asst.setText("Threshold Assistant")
        self.label_4.setText("Would you like to save this session\'s data?")
        self.label_5.setText("Filename to save to (will save in .txt format)")
        self.label_6.setText("*Opens in a new window")
        self.label_7.setText("Default filename: sessionData.txt")
        self.pushButton_stopTracking.setText("Stop Tracking")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

