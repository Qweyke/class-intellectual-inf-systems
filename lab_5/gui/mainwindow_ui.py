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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTabWidget, QVBoxLayout, QWidget)

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
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
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

        self.clear_btn = QPushButton(self.determine_tab)
        self.clear_btn.setObjectName(u"clear_btn")
        sizePolicy1.setHeightForWidth(self.clear_btn.sizePolicy().hasHeightForWidth())
        self.clear_btn.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.clear_btn)

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
        self.accept_btn = QPushButton(self.learn_tab)
        self.accept_btn.setObjectName(u"accept_btn")

        self.verticalLayout_2.addWidget(self.accept_btn)

        self.auto_check = QCheckBox(self.learn_tab)
        self.auto_check.setObjectName(u"auto_check")

        self.verticalLayout_2.addWidget(self.auto_check)

        self.tabWidget.addTab(self.learn_tab, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        self.canvas_frame = QFrame(self.centralwidget)
        self.canvas_frame.setObjectName(u"canvas_frame")
        sizePolicy.setHeightForWidth(self.canvas_frame.sizePolicy().hasHeightForWidth())
        self.canvas_frame.setSizePolicy(sizePolicy)
        self.canvas_frame.setFrameShape(QFrame.Shape.Box)

        self.horizontalLayout.addWidget(self.canvas_frame)

        MainWindow.setCentralWidget(self.centralwidget)

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
        self.clear_btn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.res_label.setText(QCoreApplication.translate("MainWindow", u"Result: None", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.determine_tab), QCoreApplication.translate("MainWindow", u"Identify", None))
        self.accept_btn.setText(QCoreApplication.translate("MainWindow", u"Accept drawing", None))
        self.auto_check.setText(QCoreApplication.translate("MainWindow", u"Auto confirm", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.learn_tab), QCoreApplication.translate("MainWindow", u"Teach", None))
    # retranslateUi

