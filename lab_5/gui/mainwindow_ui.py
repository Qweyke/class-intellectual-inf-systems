# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(918, 476)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.determine_tab = QWidget()
        self.determine_tab.setObjectName(u"determine_tab")
        self.verticalLayout = QVBoxLayout(self.determine_tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.determine_btn = QPushButton(self.determine_tab)
        self.determine_btn.setObjectName(u"determine_btn")
        sizePolicy1.setHeightForWidth(self.determine_btn.sizePolicy().hasHeightForWidth())
        self.determine_btn.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.determine_btn)

        self.res_label = QLabel(self.determine_tab)
        self.res_label.setObjectName(u"res_label")
        sizePolicy1.setHeightForWidth(self.res_label.sizePolicy().hasHeightForWidth())
        self.res_label.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.res_label)

        self.tabWidget.addTab(self.determine_tab, "")
        self.learn_tab = QWidget()
        self.learn_tab.setObjectName(u"learn_tab")
        self.verticalLayout_2 = QVBoxLayout(self.learn_tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.obj_box = QComboBox(self.learn_tab)
        self.obj_box.setObjectName(u"obj_box")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.obj_box.sizePolicy().hasHeightForWidth())
        self.obj_box.setSizePolicy(sizePolicy2)

        self.verticalLayout_2.addWidget(self.obj_box)

        self.accept_btn = QPushButton(self.learn_tab)
        self.accept_btn.setObjectName(u"accept_btn")
        self.accept_btn.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.accept_btn.sizePolicy().hasHeightForWidth())
        self.accept_btn.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.accept_btn)

        self.teach_btn = QPushButton(self.learn_tab)
        self.teach_btn.setObjectName(u"teach_btn")
        sizePolicy1.setHeightForWidth(self.teach_btn.sizePolicy().hasHeightForWidth())
        self.teach_btn.setSizePolicy(sizePolicy1)
        self.teach_btn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);")

        self.verticalLayout_2.addWidget(self.teach_btn)

        self.accuracy_btn = QPushButton(self.learn_tab)
        self.accuracy_btn.setObjectName(u"accuracy_btn")
        sizePolicy1.setHeightForWidth(self.accuracy_btn.sizePolicy().hasHeightForWidth())
        self.accuracy_btn.setSizePolicy(sizePolicy1)
        self.accuracy_btn.setStyleSheet(u"background-color: rgb(85, 170, 127);\n"
"color: rgb(255, 255, 255);\n"
"")

        self.verticalLayout_2.addWidget(self.accuracy_btn)

        self.display_btn = QPushButton(self.learn_tab)
        self.display_btn.setObjectName(u"display_btn")
        sizePolicy1.setHeightForWidth(self.display_btn.sizePolicy().hasHeightForWidth())
        self.display_btn.setSizePolicy(sizePolicy1)
        self.display_btn.setStyleSheet(u"background-color: rgb(85, 85, 255);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.display_btn)

        self.tabWidget.addTab(self.learn_tab, "")

        self.verticalLayout_3.addWidget(self.tabWidget)

        self.clear_btn = QPushButton(self.centralwidget)
        self.clear_btn.setObjectName(u"clear_btn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.clear_btn.sizePolicy().hasHeightForWidth())
        self.clear_btn.setSizePolicy(sizePolicy3)

        self.verticalLayout_3.addWidget(self.clear_btn)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.canvas_frame = QFrame(self.centralwidget)
        self.canvas_frame.setObjectName(u"canvas_frame")
        sizePolicy.setHeightForWidth(self.canvas_frame.sizePolicy().hasHeightForWidth())
        self.canvas_frame.setSizePolicy(sizePolicy)
        self.canvas_frame.setFrameShape(QFrame.Shape.Box)

        self.horizontalLayout.addWidget(self.canvas_frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"NEURONet", None))
#if QT_CONFIG(whatsthis)
        self.determine_btn.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Press to plot chosen function</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.determine_btn.setText(QCoreApplication.translate("MainWindow", u"Identify", None))
        self.res_label.setText(QCoreApplication.translate("MainWindow", u"Result: None", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.determine_tab), QCoreApplication.translate("MainWindow", u"Identify", None))
        self.accept_btn.setText(QCoreApplication.translate("MainWindow", u"Accept drawing", None))
        self.teach_btn.setText(QCoreApplication.translate("MainWindow", u"Reteach model", None))
        self.accuracy_btn.setText(QCoreApplication.translate("MainWindow", u"Check accuracy", None))
        self.display_btn.setText(QCoreApplication.translate("MainWindow", u"Display samples", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.learn_tab), QCoreApplication.translate("MainWindow", u"Learning", None))
        self.clear_btn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
    # retranslateUi

