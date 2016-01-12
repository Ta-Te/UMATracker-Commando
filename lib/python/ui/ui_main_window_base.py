# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_main_window_base.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindowBase(object):
    def setupUi(self, MainWindowBase):
        MainWindowBase.setObjectName("MainWindowBase")
        MainWindowBase.resize(902, 506)
        MainWindowBase.setAcceptDrops(True)
        self.centralwidget = QtWidgets.QWidget(MainWindowBase)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.inputGraphicsView = OverlaidGraphicsView(self.groupBox)
        self.inputGraphicsView.setAcceptDrops(False)
        self.inputGraphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.inputGraphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.inputGraphicsView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.inputGraphicsView.setObjectName("inputGraphicsView")
        self.verticalLayout.addWidget(self.inputGraphicsView)
        self.videoPlaybackWidget = VideoPlaybackWidget(self.groupBox)
        self.videoPlaybackWidget.setObjectName("videoPlaybackWidget")
        self.verticalLayout.addWidget(self.videoPlaybackWidget)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.zoomedGraphicsView = OverlaidGraphicsView(self.groupBox_2)
        self.zoomedGraphicsView.setObjectName("zoomedGraphicsView")
        self.verticalLayout_2.addWidget(self.zoomedGraphicsView)
        self.gridWidget = QtWidgets.QWidget(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridWidget.sizePolicy().hasHeightForWidth())
        self.gridWidget.setSizePolicy(sizePolicy)
        self.gridWidget.setObjectName("gridWidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.gridWidget)
        self.formLayout_2.setObjectName("formLayout_2")
        self.horizontalWidget = QtWidgets.QWidget(self.gridWidget)
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.horizontalWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.frameNoSpinBox = QtWidgets.QSpinBox(self.horizontalWidget)
        self.frameNoSpinBox.setMinimum(1)
        self.frameNoSpinBox.setMaximum(1000)
        self.frameNoSpinBox.setObjectName("frameNoSpinBox")
        self.horizontalLayout_5.addWidget(self.frameNoSpinBox)
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.horizontalWidget)
        self.overlayCheckBox = QtWidgets.QCheckBox(self.gridWidget)
        self.overlayCheckBox.setObjectName("overlayCheckBox")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.overlayCheckBox)
        self.verticalLayout_2.addWidget(self.gridWidget)
        self.formWidget = QtWidgets.QWidget(self.groupBox_2)
        self.formWidget.setObjectName("formWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formWidget)
        self.formLayout.setObjectName("formLayout")
        self.horizontalWidget1 = QtWidgets.QWidget(self.formWidget)
        self.horizontalWidget1.setObjectName("horizontalWidget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalWidget1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.horizontalWidget1)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.radiusSpinBox = QtWidgets.QDoubleSpinBox(self.horizontalWidget1)
        self.radiusSpinBox.setMinimum(5.0)
        self.radiusSpinBox.setObjectName("radiusSpinBox")
        self.horizontalLayout_3.addWidget(self.radiusSpinBox)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.horizontalWidget1)
        self.lineCheckBox = QtWidgets.QCheckBox(self.formWidget)
        self.lineCheckBox.setChecked(True)
        self.lineCheckBox.setObjectName("lineCheckBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lineCheckBox)
        self.circleCheckBox = QtWidgets.QCheckBox(self.formWidget)
        self.circleCheckBox.setChecked(True)
        self.circleCheckBox.setObjectName("circleCheckBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.circleCheckBox)
        self.horizontalWidget2 = QtWidgets.QWidget(self.formWidget)
        self.horizontalWidget2.setObjectName("horizontalWidget2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalWidget2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.horizontalWidget2)
        self.verticalLayout_2.addWidget(self.formWidget)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.groupBox_2)
        MainWindowBase.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindowBase)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 902, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindowBase.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindowBase)
        self.statusbar.setObjectName("statusbar")
        MainWindowBase.setStatusBar(self.statusbar)
        self.actionOpenCSVFile = QtWidgets.QAction(MainWindowBase)
        self.actionOpenCSVFile.setObjectName("actionOpenCSVFile")
        self.actionSaveCSVFile = QtWidgets.QAction(MainWindowBase)
        self.actionSaveCSVFile.setObjectName("actionSaveCSVFile")
        self.menuFile.addAction(self.actionOpenCSVFile)
        self.menuFile.addAction(self.actionSaveCSVFile)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindowBase)
        QtCore.QMetaObject.connectSlotsByName(MainWindowBase)

    def retranslateUi(self, MainWindowBase):
        _translate = QtCore.QCoreApplication.translate
        MainWindowBase.setWindowTitle(_translate("MainWindowBase", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindowBase", "Tracking"))
        self.groupBox_2.setTitle(_translate("MainWindowBase", "Zoom"))
        self.label_2.setText(_translate("MainWindowBase", "# of frames:"))
        self.overlayCheckBox.setText(_translate("MainWindowBase", "Overlay"))
        self.label.setText(_translate("MainWindowBase", "Radius:"))
        self.lineCheckBox.setText(_translate("MainWindowBase", "Line"))
        self.circleCheckBox.setText(_translate("MainWindowBase", "Circle"))
        self.menuFile.setTitle(_translate("MainWindowBase", "File"))
        self.actionOpenCSVFile.setText(_translate("MainWindowBase", "Open CSV File"))
        self.actionSaveCSVFile.setText(_translate("MainWindowBase", "Save CSV FIle"))

from .overlaid_graphics_view import OverlaidGraphicsView
from .video_playback_widget import VideoPlaybackWidget
