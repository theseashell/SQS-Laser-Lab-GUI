# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LaserLabGUI3000.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import numpy as np
from time import sleep

from ThreadClasses.cpclaserpowerscanThread import cpclaserpowerscanThread
from ThreadClasses.leclaserpowerscanThread import leclaserpowerscanThread
from ThreadClasses.cpcstagepositionscanThread import cpcstagepositionscanThread
from ThreadClasses.lecstagepositionscanThread import lecstagepositionscanThread


class Ui_LazerLabGUI(object):
    def setupUi(self, LazerLabGUI):
        LazerLabGUI.setObjectName("LazerLabGUI")
        LazerLabGUI.resize(567, 518)
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        LazerLabGUI.setFont(font)
        LazerLabGUI.setStyleSheet("")
        self.tabWidget = QtWidgets.QTabWidget(LazerLabGUI)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 531, 391))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(False)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("background: rgb(221,221,221)")
        self.tabWidget.setObjectName("tabWidget")
        self.powerdelayTab = QtWidgets.QWidget()
        self.powerdelayTab.setObjectName("powerdelayTab")
        self.laserpowergroupBox = QtWidgets.QGroupBox(self.powerdelayTab)
        self.laserpowergroupBox.setEnabled(True)
        self.laserpowergroupBox.setGeometry(QtCore.QRect(30, 20, 191, 281))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.laserpowergroupBox.setFont(font)
        self.laserpowergroupBox.setStyleSheet("QGroupBox { \n"
"     border: 2px solid gray; \n"
"     border-radius: 3px; \n"
" }")
        self.laserpowergroupBox.setObjectName("laserpowergroupBox")
        self.layoutWidget = QtWidgets.QWidget(self.laserpowergroupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 120, 135, 73))
        self.layoutWidget.setObjectName("layoutWidget")
        self.adjustlaserpowerLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.adjustlaserpowerLayout.setContentsMargins(0, 0, 0, 0)
        self.adjustlaserpowerLayout.setObjectName("adjustlaserpowerLayout")
        self.newlaserpowerLabel = QtWidgets.QLabel(self.layoutWidget)
        self.newlaserpowerLabel.setObjectName("newlaserpowerLabel")
        self.adjustlaserpowerLayout.addWidget(self.newlaserpowerLabel)
        self.newlaserpowerLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.newlaserpowerLineEdit.setStyleSheet("border-radius: 5px;\n"
"border: 2px solid grey;")
        self.newlaserpowerLineEdit.setObjectName("newlaserpowerLineEdit")
        self.adjustlaserpowerLayout.addWidget(self.newlaserpowerLineEdit)
        self.newlaserpowersetButton = QtWidgets.QPushButton(self.layoutWidget)
        self.newlaserpowersetButton.setEnabled(False)
        self.newlaserpowersetButton.setStyleSheet("QPushButton:pressed {\n"
"border-radius: 5px;\n"
"border: 4px solid grey;\n"
"background-color:rgb(87, 103, 122);\n"
"font-size:10px\n"
"}\n"
"QPushButton {\n"
"border-radius: 5px;\n"
"border: 4px solid grey;\n"
"background-color: rgb(87, 103, 122)\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"border-radius: 5px;\n"
"border: 4px solid grey;\n"
"background-color: rgb(170, 170, 127)\n"
"}")
        self.newlaserpowersetButton.setCheckable(False)
        self.newlaserpowersetButton.setObjectName("newlaserpowersetButton")
        self.adjustlaserpowerLayout.addWidget(self.newlaserpowersetButton)
        self.layoutWidget1 = QtWidgets.QWidget(self.laserpowergroupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 30, 141, 69))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.laserconnectLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.laserconnectLayout.setContentsMargins(0, 0, 0, 0)
        self.laserconnectLayout.setObjectName("laserconnectLayout")
        self.connectwaveplatetextLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.connectwaveplatetextLabel.setObjectName("connectwaveplatetextLabel")
        self.laserconnectLayout.addWidget(self.connectwaveplatetextLabel)
        self.connecttowaveplateButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.connecttowaveplateButton.setAutoFillBackground(False)
        self.connecttowaveplateButton.setStyleSheet("QPushButton:pressed {\n"
"border-radius: 5px;\n"
"border: 4px solid grey;\n"
"background-color: rgb(23, 255, 96);\n"
"font-size:10px\n"
"}\n"
"QPushButton {\n"
"border-radius: 5px;\n"
"border: 4px solid grey;\n"
"background-color: rgb(23, 255, 96)\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"border-radius: 5px;\n"
"border: 4px solid grey;\n"
"background-color: rgb(170, 170, 127)\n"
"}")
        self.connecttowaveplateButton.setAutoDefault(True)
        self.connecttowaveplateButton.setFlat(False)
        self.connecttowaveplateButton.setObjectName("connecttowaveplateButton")
        self.laserconnectLayout.addWidget(self.connecttowaveplateButton)
        self.iswaveplateconnectedCheckBox = QtWidgets.QCheckBox(self.layoutWidget1)
        self.iswaveplateconnectedCheckBox.setEnabled(False)
        self.iswaveplateconnectedCheckBox.setObjectName("iswaveplateconnectedCheckBox")
        self.laserconnectLayout.addWidget(self.iswaveplateconnectedCheckBox)
        self.layoutWidget2 = QtWidgets.QWidget(self.laserpowergroupBox)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 220, 171, 50))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.laserpowerprogressbarLayout = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.laserpowerprogressbarLayout.setContentsMargins(0, 0, 0, 0)
        self.laserpowerprogressbarLayout.setObjectName("laserpowerprogressbarLayout")
        self.currentlaserpowerLabel = QtWidgets.QLabel(self.layoutWidget2)
        self.currentlaserpowerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.currentlaserpowerLabel.setObjectName("currentlaserpowerLabel")
        self.laserpowerprogressbarLayout.addWidget(self.currentlaserpowerLabel)
        self.laserpowerprogressBar = QtWidgets.QProgressBar(self.layoutWidget2)
        self.laserpowerprogressBar.setStyleSheet("QProgressBar{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(23, 255, 96);\n"
"    width: 1px;\n"
"    margin: 0px;\n"
"}")
        self.laserpowerprogressBar.setProperty("value", "0")
        self.laserpowerprogressBar.setObjectName("laserpowerprogressBar")
        self.laserpowerprogressbarLayout.addWidget(self.laserpowerprogressBar)
        self.stagepositiongroupBox = QtWidgets.QGroupBox(self.powerdelayTab)
        self.stagepositiongroupBox.setGeometry(QtCore.QRect(300, 20, 191, 281))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.stagepositiongroupBox.setFont(font)
        self.stagepositiongroupBox.setStyleSheet("QGroupBox { \n"
"     border: 2px solid gray; \n"
"     border-radius: 3px; \n"
" }")
        self.stagepositiongroupBox.setObjectName("stagepositiongroupBox")
        self.layoutWidget3 = QtWidgets.QWidget(self.stagepositiongroupBox)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 30, 141, 65))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.connecttostageLayout = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.connecttostageLayout.setContentsMargins(0, 0, 0, 0)
        self.connecttostageLayout.setObjectName("connecttostageLayout")
        self.connectstagetextLabel = QtWidgets.QLabel(self.layoutWidget3)
        self.connectstagetextLabel.setObjectName("connectstagetextLabel")
        self.connecttostageLayout.addWidget(self.connectstagetextLabel)
        self.connecttostageButton = QtWidgets.QPushButton(self.layoutWidget3)
        self.connecttostageButton.setStyleSheet("QPushButton:pressed {\n"
"border-radius: 5px;\n"
"border: 4px solid grey;\n"
"background-color: rgb(23, 255, 96);\n"
"font-size:10px\n"
"}\n"
"QPushButton {\n"
"border-radius: 5px;\n"
"border: 4px solid grey;\n"
"background-color: rgb(23, 255, 96)\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"border-radius: 5px;\n"
"border: 4px solid grey;\n"
"background-color: rgb(170, 170, 127)\n"
"}")
        self.connecttostageButton.setAutoDefault(True)
        self.connecttostageButton.setDefault(False)
        self.connecttostageButton.setObjectName("connecttostageButton")
        self.connecttostageLayout.addWidget(self.connecttostageButton)
        self.isstageconnectedCheckBox = QtWidgets.QCheckBox(self.layoutWidget3)
        self.isstageconnectedCheckBox.setEnabled(False)
        self.isstageconnectedCheckBox.setObjectName("isstageconnectedCheckBox")
        self.connecttostageLayout.addWidget(self.isstageconnectedCheckBox)
        self.layoutWidget_2 = QtWidgets.QWidget(self.stagepositiongroupBox)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 120, 135, 73))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.newstagepositionLabel = QtWidgets.QLabel(self.layoutWidget_2)
        self.newstagepositionLabel.setObjectName("newstagepositionLabel")
        self.verticalLayout_5.addWidget(self.newstagepositionLabel)
        self.newstagepositionLineEdit = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.newstagepositionLineEdit.setStyleSheet("border-radius: 5px;\n"
"border: 2px solid grey;")
        self.newstagepositionLineEdit.setObjectName("newstagepositionLineEdit")
        self.newstagepositionLineEdit.setAlignment(QtCore.Qt.AlignRight)

        self.verticalLayout_5.addWidget(self.newstagepositionLineEdit)
        self.newstagepositionsetButton = QtWidgets.QPushButton(self.layoutWidget_2)
        self.newstagepositionsetButton.setEnabled(False)
        self.newstagepositionsetButton.setStyleSheet("QPushButton:pressed {\n"
"border-radius: 5px;\n"
"border: 4px solid grey;\n"
"background-color:rgb(87, 103, 122);\n"
"font-size:10px\n"
"}\n"
"QPushButton {\n"
"border-radius: 5px;\n"
"border: 4px solid grey;\n"
"background-color: rgb(87, 103, 122)\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"border-radius: 5px;\n"
"border: 4px solid grey;\n"
"background-color: rgb(170, 170, 127)\n"
"}")
        self.newstagepositionsetButton.setObjectName("newstagepositionsetButton")
        self.verticalLayout_5.addWidget(self.newstagepositionsetButton)
        self.layoutWidget4 = QtWidgets.QWidget(self.stagepositiongroupBox)
        self.layoutWidget4.setGeometry(QtCore.QRect(10, 228, 161, 41))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.currentstagepositionLayout = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.currentstagepositionLayout.setContentsMargins(0, 0, 0, 0)
        self.currentstagepositionLayout.setObjectName("currentstagepositionLayout")
        self.currentstagepositionLabel = QtWidgets.QLabel(self.layoutWidget4)
        self.currentstagepositionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.currentstagepositionLabel.setObjectName("currentstagepositionLabel")
        self.currentstagepositionLayout.addWidget(self.currentstagepositionLabel)
        self.displaycurrentstagepostitionLineEdit = QtWidgets.QLineEdit(self.layoutWidget4)
        self.displaycurrentstagepostitionLineEdit.setStyleSheet("border-radius: 5px;\n"
"border: 2px solid grey;")
        self.displaycurrentstagepostitionLineEdit.setObjectName("displaycurrentstagepostitionLineEdit")
        self.displaycurrentstagepostitionLineEdit.setReadOnly(True)       
        self.currentstagepositionLayout.addWidget(self.displaycurrentstagepostitionLineEdit)
        self.tabWidget.addTab(self.powerdelayTab, "")
        self.coboldscanTab = QtWidgets.QWidget()
        self.coboldscanTab.setObjectName("coboldscanTab")
        self.cpclaserpowerscanGroupBox = QtWidgets.QGroupBox(self.coboldscanTab)
        self.cpclaserpowerscanGroupBox.setEnabled(True)
        self.cpclaserpowerscanGroupBox.setGeometry(QtCore.QRect(30, 20, 191, 271))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cpclaserpowerscanGroupBox.setFont(font)
        self.cpclaserpowerscanGroupBox.setStyleSheet("QGroupBox { \n"
"     border: 2px solid gray; \n"
"     border-radius: 3px; \n"
" }")
        self.cpclaserpowerscanGroupBox.setObjectName("cpclaserpowerscanGroupBox")
        self.layoutWidget_3 = QtWidgets.QWidget(self.cpclaserpowerscanGroupBox)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 30, 135, 45))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.cpcfirstpowerLayout = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.cpcfirstpowerLayout.setContentsMargins(0, 0, 0, 0)
        self.cpcfirstpowerLayout.setObjectName("cpcfirstpowerLayout")
        self.cpcfirstpowerLabel = QtWidgets.QLabel(self.layoutWidget_3)
        self.cpcfirstpowerLabel.setObjectName("cpcfirstpowerLabel")
        self.cpcfirstpowerLayout.addWidget(self.cpcfirstpowerLabel)
        self.cpcfirstpowerLineEdit = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.cpcfirstpowerLineEdit.setStyleSheet("border-radius: 5px;\n"
"border: 2px solid grey;")
        self.cpcfirstpowerLineEdit.setObjectName("cpcfirstpowerLineEdit")
        self.cpcfirstpowerLayout.addWidget(self.cpcfirstpowerLineEdit)
        self.layoutWidget_4 = QtWidgets.QWidget(self.cpclaserpowerscanGroupBox)
        self.layoutWidget_4.setGeometry(QtCore.QRect(10, 80, 135, 45))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.cpclastpowerLayout = QtWidgets.QVBoxLayout(self.layoutWidget_4)
        self.cpclastpowerLayout.setContentsMargins(0, 0, 0, 0)
        self.cpclastpowerLayout.setObjectName("cpclastpowerLayout")
        self.cpclastpowerLabel = QtWidgets.QLabel(self.layoutWidget_4)
        self.cpclastpowerLabel.setObjectName("cpclastpowerLabel")
        self.cpclastpowerLayout.addWidget(self.cpclastpowerLabel)
        self.cpclastpowerLineEdit = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.cpclastpowerLineEdit.setStyleSheet("border-radius: 5px;\n"
"border: 2px solid grey;")
        self.cpclastpowerLineEdit.setObjectName("cpclastpowerLineEdit")
        self.cpclastpowerLayout.addWidget(self.cpclastpowerLineEdit)
        self.layoutWidget_5 = QtWidgets.QWidget(self.cpclaserpowerscanGroupBox)
        self.layoutWidget_5.setGeometry(QtCore.QRect(10, 130, 135, 45))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.cpclaserpowerstepsLayout = QtWidgets.QVBoxLayout(self.layoutWidget_5)
        self.cpclaserpowerstepsLayout.setContentsMargins(0, 0, 0, 0)
        self.cpclaserpowerstepsLayout.setObjectName("cpclaserpowerstepsLayout")
        self.cpclaserpowerstepsLabel = QtWidgets.QLabel(self.layoutWidget_5)
        self.cpclaserpowerstepsLabel.setObjectName("cpclaserpowerstepsLabel")
        self.cpclaserpowerstepsLayout.addWidget(self.cpclaserpowerstepsLabel)
        self.cpclaserpowerstepsLineEdit = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.cpclaserpowerstepsLineEdit.setStyleSheet("border-radius: 5px;\n"
"border: 2px solid grey;")
        self.cpclaserpowerstepsLineEdit.setObjectName("cpclaserpowerstepsLineEdit")
        self.cpclaserpowerstepsLayout.addWidget(self.cpclaserpowerstepsLineEdit)
        self.layoutWidget_6 = QtWidgets.QWidget(self.cpclaserpowerscanGroupBox)
        self.layoutWidget_6.setGeometry(QtCore.QRect(10, 180, 135, 45))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.cpclaserpowerinttimeLayout = QtWidgets.QVBoxLayout(self.layoutWidget_6)
        self.cpclaserpowerinttimeLayout.setContentsMargins(0, 0, 0, 0)
        self.cpclaserpowerinttimeLayout.setObjectName("cpclaserpowerinttimeLayout")
        self.cpclaserpowerinttimeLabel = QtWidgets.QLabel(self.layoutWidget_6)
        self.cpclaserpowerinttimeLabel.setObjectName("cpclaserpowerinttimeLabel")
        self.cpclaserpowerinttimeLayout.addWidget(self.cpclaserpowerinttimeLabel)
        self.cpclaserpowerinttimeLineEdit = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.cpclaserpowerinttimeLineEdit.setStyleSheet("border-radius: 5px;\n"
"border: 2px solid grey;")
        self.cpclaserpowerinttimeLineEdit.setObjectName("cpclaserpowerinttimeLineEdit")
        self.cpclaserpowerinttimeLayout.addWidget(self.cpclaserpowerinttimeLineEdit)
        self.layoutWidget5 = QtWidgets.QWidget(self.cpclaserpowerscanGroupBox)
        self.layoutWidget5.setGeometry(QtCore.QRect(17, 236, 158, 25))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.cpclaserpowerstartstopLayout = QtWidgets.QHBoxLayout(self.layoutWidget5)
        self.cpclaserpowerstartstopLayout.setContentsMargins(0, 0, 0, 0)
        self.cpclaserpowerstartstopLayout.setObjectName("cpclaserpowerstartstopLayout")
        self.cpclaserpowerstartPushButton = QtWidgets.QPushButton(self.layoutWidget5)
        self.cpclaserpowerstartPushButton.setEnabled(False)
        self.cpclaserpowerstartPushButton.setStyleSheet("QPushButton:pressed {\n"
"border-radius: 5px;\n"
"border: 4px solid grey;\n"
"background-color: rgb(23, 255, 96);\n"
"font-size:10px\n"
"}\n"
"QPushButton {\n"
"border-radius: 5px;\n"
"border: 4px solid grey;\n"
"background-color: rgb(23, 255, 96)\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"border-radius: 5px;\n"
"border: 4px solid grey;\n"
"background-color: rgb(170, 170, 127)\n"
"}")
        self.cpclaserpowerstartPushButton.setObjectName("cpclaserpowerstartPushButton")
        self.cpclaserpowerstartstopLayout.addWidget(self.cpclaserpowerstartPushButton)
        self.cpclaserpowerstopPushButton = QtWidgets.QPushButton(self.layoutWidget5)
        self.cpclaserpowerstopPushButton.setEnabled(False)
        self.cpclaserpowerstopPushButton.setStyleSheet("QPushButton:pressed {\n"
"border-radius: 5px;\n"
"border: 4px solid grey;\n"
"background-color: rgb(255, 93, 0);\n"
"font-size:10px\n"
"}\n"
"QPushButton {\n"
"border-radius: 5px;\n"
"border: 4px solid grey;\n"
"background-color: rgb(255, 93, 0)\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"border-radius: 5px;\n"
"border: 4px solid grey;\n"
"background-color: rgb(170, 170, 127)\n"
"}")
        self.cpclaserpowerstopPushButton.setObjectName("cpclaserpowerstopPushButton")
        self.cpclaserpowerstartstopLayout.addWidget(self.cpclaserpowerstopPushButton)
        self.cpcstagescanGroupBox = QtWidgets.QGroupBox(self.coboldscanTab)
        self.cpcstagescanGroupBox.setGeometry(QtCore.QRect(300, 20, 191, 271))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cpcstagescanGroupBox.setFont(font)
        self.cpcstagescanGroupBox.setStyleSheet("QGroupBox { \n"
"     border: 2px solid gray; \n"
"     border-radius: 3px; \n"
" }")
        self.cpcstagescanGroupBox.setObjectName("cpcstagescanGroupBox")
        self.layoutWidget_11 = QtWidgets.QWidget(self.cpcstagescanGroupBox)
        self.layoutWidget_11.setGeometry(QtCore.QRect(10, 30, 135, 45))
        self.layoutWidget_11.setObjectName("layoutWidget_11")
        self.cpcfirstpositionLayout = QtWidgets.QVBoxLayout(self.layoutWidget_11)
        self.cpcfirstpositionLayout.setContentsMargins(0, 0, 0, 0)
        self.cpcfirstpositionLayout.setObjectName("cpcfirstpositionLayout")
        self.cpcfirstpositionLabel = QtWidgets.QLabel(self.layoutWidget_11)
        self.cpcfirstpositionLabel.setObjectName("cpcfirstpositionLabel")
        self.cpcfirstpositionLayout.addWidget(self.cpcfirstpositionLabel)
        self.cpcfirstpositionLineEdit = QtWidgets.QLineEdit(self.layoutWidget_11)
        self.cpcfirstpositionLineEdit.setStyleSheet("border-radius: 5px;\n"
"border: 2px solid grey;")
        self.cpcfirstpositionLineEdit.setObjectName("cpcfirstpositionLineEdit")
        self.cpcfirstpositionLayout.addWidget(self.cpcfirstpositionLineEdit)
        self.layoutWidget_12 = QtWidgets.QWidget(self.cpcstagescanGroupBox)
        self.layoutWidget_12.setGeometry(QtCore.QRect(10, 80, 135, 45))
        self.layoutWidget_12.setObjectName("layoutWidget_12")
        self.cpclastpositionLayout = QtWidgets.QVBoxLayout(self.layoutWidget_12)
        self.cpclastpositionLayout.setContentsMargins(0, 0, 0, 0)
        self.cpclastpositionLayout.setObjectName("cpclastpositionLayout")
        self.cpclastpositionLabel = QtWidgets.QLabel(self.layoutWidget_12)
        self.cpclastpositionLabel.setObjectName("cpclastpositionLabel")
        self.cpclastpositionLayout.addWidget(self.cpclastpositionLabel)
        self.cpclastpositionLineEdit = QtWidgets.QLineEdit(self.layoutWidget_12)
        self.cpclastpositionLineEdit.setStyleSheet("border-radius: 5px;\n"
"border: 2px solid grey;")
        self.cpclastpositionLineEdit.setObjectName("cpclastpositionLineEdit")
        self.cpclastpositionLayout.addWidget(self.cpclastpositionLineEdit)
        self.layoutWidget_13 = QtWidgets.QWidget(self.cpcstagescanGroupBox)
        self.layoutWidget_13.setGeometry(QtCore.QRect(10, 130, 135, 45))
        self.layoutWidget_13.setObjectName("layoutWidget_13")
        self.cpcstagepositionstepsLayout = QtWidgets.QVBoxLayout(self.layoutWidget_13)
        self.cpcstagepositionstepsLayout.setContentsMargins(0, 0, 0, 0)
        self.cpcstagepositionstepsLayout.setObjectName("cpcstagepositionstepsLayout")
        self.cpcstagepositionstepsLabel = QtWidgets.QLabel(self.layoutWidget_13)
        self.cpcstagepositionstepsLabel.setObjectName("cpcstagepositionstepsLabel")
        self.cpcstagepositionstepsLayout.addWidget(self.cpcstagepositionstepsLabel)
        self.cpcstagepositionstepsLineEdit = QtWidgets.QLineEdit(self.layoutWidget_13)
        self.cpcstagepositionstepsLineEdit.setStyleSheet("border-radius: 5px;\n"
"border: 2px solid grey;")
        self.cpcstagepositionstepsLineEdit.setObjectName("cpcstagepositionstepsLineEdit")
        self.cpcstagepositionstepsLayout.addWidget(self.cpcstagepositionstepsLineEdit)
        self.layoutWidget_14 = QtWidgets.QWidget(self.cpcstagescanGroupBox)
        self.layoutWidget_14.setGeometry(QtCore.QRect(10, 180, 135, 45))
        self.layoutWidget_14.setObjectName("layoutWidget_14")
        self.cpcstagepositioninttimeLayout = QtWidgets.QVBoxLayout(self.layoutWidget_14)
        self.cpcstagepositioninttimeLayout.setContentsMargins(0, 0, 0, 0)
        self.cpcstagepositioninttimeLayout.setObjectName("cpcstagepositioninttimeLayout")
        self.cpcstagepositioninttimeLabel = QtWidgets.QLabel(self.layoutWidget_14)
        self.cpcstagepositioninttimeLabel.setObjectName("cpcstagepositioninttimeLabel")
        self.cpcstagepositioninttimeLayout.addWidget(self.cpcstagepositioninttimeLabel)
        self.cpcstagepositioninttimeLineEdit = QtWidgets.QLineEdit(self.layoutWidget_14)
        self.cpcstagepositioninttimeLineEdit.setStyleSheet("border-radius: 5px;\n"
"border: 2px solid grey;")
        self.cpcstagepositioninttimeLineEdit.setObjectName("cpcstagepositioninttimeLineEdit")
        self.cpcstagepositioninttimeLayout.addWidget(self.cpcstagepositioninttimeLineEdit)
        self.layoutWidget_19 = QtWidgets.QWidget(self.cpcstagescanGroupBox)
        self.layoutWidget_19.setGeometry(QtCore.QRect(17, 235, 158, 25))
        self.layoutWidget_19.setObjectName("layoutWidget_19")
        self.cpcstagepositionstartstopLayout = QtWidgets.QHBoxLayout(self.layoutWidget_19)
        self.cpcstagepositionstartstopLayout.setContentsMargins(0, 0, 0, 0)
        self.cpcstagepositionstartstopLayout.setObjectName("cpcstagepositionstartstopLayout")
        self.cpcstagepositionstartPushButton = QtWidgets.QPushButton(self.layoutWidget_19)
        self.cpcstagepositionstartPushButton.setEnabled(False)
        self.cpcstagepositionstartPushButton.setStyleSheet("QPushButton:pressed {\n"
"border-radius: 5px;\n"
"border: 4px solid grey;\n"
"background-color: rgb(23, 255, 96);\n"
"font-size:10px\n"
"}\n"
"QPushButton {\n"
"border-radius: 5px;\n"
"border: 4px solid grey;\n"
"background-color: rgb(23, 255, 96)\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"border-radius: 5px;\n"
"border: 4px solid grey;\n"
"background-color: rgb(170, 170, 127)\n"
"}")
        self.cpcstagepositionstartPushButton.setObjectName("cpcstagepositionstartPushButton")
        self.cpcstagepositionstartstopLayout.addWidget(self.cpcstagepositionstartPushButton)
        self.cpcstagepositionstopPushButton = QtWidgets.QPushButton(self.layoutWidget_19)
        self.cpcstagepositionstopPushButton.setEnabled(False)
        self.cpcstagepositionstopPushButton.setStyleSheet("QPushButton:pressed {\n"
"border-radius: 5px;\n"
"border: 4px solid grey;\n"
"background-color: rgb(255, 93, 0);\n"
"font-size:10px\n"
"}\n"
"QPushButton {\n"
"border-radius: 5px;\n"
"border: 4px solid grey;\n"
"background-color: rgb(255, 93, 0)\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"border-radius: 5px;\n"
"border: 4px solid grey;\n"
"background-color: rgb(170, 170, 127)\n"
"}")
        self.cpcstagepositionstopPushButton.setObjectName("cpcstagepositionstopPushButton")
        self.cpcstagepositionstartstopLayout.addWidget(self.cpcstagepositionstopPushButton)
        self.layoutWidget6 = QtWidgets.QWidget(self.coboldscanTab)
        self.layoutWidget6.setGeometry(QtCore.QRect(10, 300, 501, 50))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.cpcscanprogressLayout = QtWidgets.QVBoxLayout(self.layoutWidget6)
        self.cpcscanprogressLayout.setContentsMargins(0, 0, 0, 0)
        self.cpcscanprogressLayout.setObjectName("cpcscanprogressLayout")
        self.cpcscanprogressLabel = QtWidgets.QLabel(self.layoutWidget6)
        self.cpcscanprogressLabel.setObjectName("cpcscanprogressLabel")
        self.cpcscanprogressLayout.addWidget(self.cpcscanprogressLabel)
        self.cpcscanprogressProgressBar = QtWidgets.QProgressBar(self.layoutWidget6)
        self.cpcscanprogressProgressBar.setStyleSheet("QProgressBar{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(23, 255, 96);\n"
"    width: 10px;\n"
"    margin: 1px;\n"
"}")
        self.cpcscanprogressProgressBar.setProperty("value", "0")
        self.cpcscanprogressProgressBar.setObjectName("cpcscanprogressProgressBar")
        self.cpcscanprogressLayout.addWidget(self.cpcscanprogressProgressBar)
        self.tabWidget.addTab(self.coboldscanTab, "")
        self.lecroyscanTab = QtWidgets.QWidget()
        self.lecroyscanTab.setObjectName("lecroyscanTab")
        self.leclaserpowerscanGroupBox = QtWidgets.QGroupBox(self.lecroyscanTab)
        self.leclaserpowerscanGroupBox.setGeometry(QtCore.QRect(30, 20, 191, 271))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.leclaserpowerscanGroupBox.setFont(font)
        self.leclaserpowerscanGroupBox.setStyleSheet("QGroupBox { \n"
"     border: 2px solid gray; \n"
"     border-radius: 3px; \n"
" }")
        self.leclaserpowerscanGroupBox.setObjectName("leclaserpowerscanGroupBox")
        self.layoutWidget_20 = QtWidgets.QWidget(self.leclaserpowerscanGroupBox)
        self.layoutWidget_20.setGeometry(QtCore.QRect(10, 30, 135, 45))
        self.layoutWidget_20.setObjectName("layoutWidget_20")
        self.lecfirstpowerLayout = QtWidgets.QVBoxLayout(self.layoutWidget_20)
        self.lecfirstpowerLayout.setContentsMargins(0, 0, 0, 0)
        self.lecfirstpowerLayout.setObjectName("lecfirstpowerLayout")
        self.lecfirstpowerLabel = QtWidgets.QLabel(self.layoutWidget_20)
        self.lecfirstpowerLabel.setObjectName("lecfirstpowerLabel")
        self.lecfirstpowerLayout.addWidget(self.lecfirstpowerLabel)
        self.lecfirstpowerLineEdit = QtWidgets.QLineEdit(self.layoutWidget_20)
        self.lecfirstpowerLineEdit.setStyleSheet("border-radius: 5px;\n"
"border: 2px solid grey;")
        self.lecfirstpowerLineEdit.setObjectName("lecfirstpowerLineEdit")
        self.lecfirstpowerLayout.addWidget(self.lecfirstpowerLineEdit)
        self.layoutWidget_21 = QtWidgets.QWidget(self.leclaserpowerscanGroupBox)
        self.layoutWidget_21.setGeometry(QtCore.QRect(10, 80, 135, 45))
        self.layoutWidget_21.setObjectName("layoutWidget_21")
        self.leclastpowerLayout = QtWidgets.QVBoxLayout(self.layoutWidget_21)
        self.leclastpowerLayout.setContentsMargins(0, 0, 0, 0)
        self.leclastpowerLayout.setObjectName("leclastpowerLayout")
        self.leclastpowerLabel = QtWidgets.QLabel(self.layoutWidget_21)
        self.leclastpowerLabel.setObjectName("leclastpowerLabel")
        self.leclastpowerLayout.addWidget(self.leclastpowerLabel)
        self.leclastpowerLineEdit = QtWidgets.QLineEdit(self.layoutWidget_21)
        self.leclastpowerLineEdit.setStyleSheet("border-radius: 5px;\n"
"border: 2px solid grey;")
        self.leclastpowerLineEdit.setObjectName("leclastpowerLineEdit")
        self.leclastpowerLayout.addWidget(self.leclastpowerLineEdit)
        self.layoutWidget_22 = QtWidgets.QWidget(self.leclaserpowerscanGroupBox)
        self.layoutWidget_22.setGeometry(QtCore.QRect(10, 130, 135, 45))
        self.layoutWidget_22.setObjectName("layoutWidget_22")
        self.leclaserpowerstepsLayout = QtWidgets.QVBoxLayout(self.layoutWidget_22)
        self.leclaserpowerstepsLayout.setContentsMargins(0, 0, 0, 0)
        self.leclaserpowerstepsLayout.setObjectName("leclaserpowerstepsLayout")
        self.leclaserpowerstepsLabel = QtWidgets.QLabel(self.layoutWidget_22)
        self.leclaserpowerstepsLabel.setObjectName("leclaserpowerstepsLabel")
        self.leclaserpowerstepsLayout.addWidget(self.leclaserpowerstepsLabel)
        self.leclaserpowerstepsLineEdit = QtWidgets.QLineEdit(self.layoutWidget_22)
        self.leclaserpowerstepsLineEdit.setStyleSheet("border-radius: 5px;\n"
"border: 2px solid grey;")
        self.leclaserpowerstepsLineEdit.setObjectName("leclaserpowerstepsLineEdit")
        self.leclaserpowerstepsLayout.addWidget(self.leclaserpowerstepsLineEdit)
        self.layoutWidget_23 = QtWidgets.QWidget(self.leclaserpowerscanGroupBox)
        self.layoutWidget_23.setGeometry(QtCore.QRect(10, 180, 135, 45))
        self.layoutWidget_23.setObjectName("layoutWidget_23")
        self.leclaserpowerinttimeLayout = QtWidgets.QVBoxLayout(self.layoutWidget_23)
        self.leclaserpowerinttimeLayout.setContentsMargins(0, 0, 0, 0)
        self.leclaserpowerinttimeLayout.setObjectName("leclaserpowerinttimeLayout")
        self.leclaserpowerinttimeLabel = QtWidgets.QLabel(self.layoutWidget_23)
        self.leclaserpowerinttimeLabel.setObjectName("leclaserpowerinttimeLabel")
        self.leclaserpowerinttimeLayout.addWidget(self.leclaserpowerinttimeLabel)
        self.leclaserpowerinttimeLineEdit = QtWidgets.QLineEdit(self.layoutWidget_23)
        self.leclaserpowerinttimeLineEdit.setStyleSheet("border-radius: 5px;\n"
"border: 2px solid grey;")
        self.leclaserpowerinttimeLineEdit.setObjectName("leclaserpowerinttimeLineEdit")
        self.leclaserpowerinttimeLayout.addWidget(self.leclaserpowerinttimeLineEdit)
        self.layoutWidget_28 = QtWidgets.QWidget(self.leclaserpowerscanGroupBox)
        self.layoutWidget_28.setGeometry(QtCore.QRect(17, 236, 158, 25))
        self.layoutWidget_28.setObjectName("layoutWidget_28")
        self.leclaserpowerstartstopLayout = QtWidgets.QHBoxLayout(self.layoutWidget_28)
        self.leclaserpowerstartstopLayout.setContentsMargins(0, 0, 0, 0)
        self.leclaserpowerstartstopLayout.setObjectName("leclaserpowerstartstopLayout")
        self.leclaserpowerstartPushButton = QtWidgets.QPushButton(self.layoutWidget_28)
        self.leclaserpowerstartPushButton.setEnabled(False)
        self.leclaserpowerstartPushButton.setStyleSheet("QPushButton:pressed {\n"
"border-radius: 5px;\n"
"border: 4px solid grey;\n"
"background-color: rgb(23, 255, 96);\n"
"font-size:10px\n"
"}\n"
"QPushButton {\n"
"border-radius: 5px;\n"
"border: 4px solid grey;\n"
"background-color: rgb(23, 255, 96)\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"border-radius: 5px;\n"
"border: 4px solid grey;\n"
"background-color: rgb(170, 170, 127)\n"
"}")
        self.leclaserpowerstartPushButton.setObjectName("leclaserpowerstartPushButton")
        self.leclaserpowerstartstopLayout.addWidget(self.leclaserpowerstartPushButton)
        self.leclaserpowerstopPushButton = QtWidgets.QPushButton(self.layoutWidget_28)
        self.leclaserpowerstopPushButton.setEnabled(False)
        self.leclaserpowerstopPushButton.setStyleSheet("QPushButton:pressed {\n"
"border-radius: 5px;\n"
"border: 4px solid grey;\n"
"background-color: rgb(255, 93, 0);\n"
"font-size:10px\n"
"}\n"
"QPushButton {\n"
"border-radius: 5px;\n"
"border: 4px solid grey;\n"
"background-color: rgb(255, 93, 0)\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"border-radius: 5px;\n"
"border: 4px solid grey;\n"
"background-color: rgb(170, 170, 127)\n"
"}")
        self.leclaserpowerstopPushButton.setObjectName("leclaserpowerstopPushButton")
        self.leclaserpowerstartstopLayout.addWidget(self.leclaserpowerstopPushButton)
        self.lecstagepositionGroupBox = QtWidgets.QGroupBox(self.lecroyscanTab)
        self.lecstagepositionGroupBox.setGeometry(QtCore.QRect(300, 20, 191, 271))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lecstagepositionGroupBox.setFont(font)
        self.lecstagepositionGroupBox.setStyleSheet("QGroupBox { \n"
"     border: 2px solid gray; \n"
"     border-radius: 3px; \n"
" }")
        self.lecstagepositionGroupBox.setObjectName("lecstagepositionGroupBox")
        self.layoutWidget_63 = QtWidgets.QWidget(self.lecstagepositionGroupBox)
        self.layoutWidget_63.setGeometry(QtCore.QRect(10, 30, 135, 45))
        self.layoutWidget_63.setObjectName("layoutWidget_63")
        self.lecfirstpositionLayout = QtWidgets.QVBoxLayout(self.layoutWidget_63)
        self.lecfirstpositionLayout.setContentsMargins(0, 0, 0, 0)
        self.lecfirstpositionLayout.setObjectName("lecfirstpositionLayout")
        self.lecfirstpositionLabel_2 = QtWidgets.QLabel(self.layoutWidget_63)
        self.lecfirstpositionLabel_2.setObjectName("lecfirstpositionLabel_2")
        self.lecfirstpositionLayout.addWidget(self.lecfirstpositionLabel_2)
        self.lecfirstpositionLineEdit = QtWidgets.QLineEdit(self.layoutWidget_63)
        self.lecfirstpositionLineEdit.setStyleSheet("border-radius: 5px;\n"
"border: 2px solid grey;")
        self.lecfirstpositionLineEdit.setObjectName("lecfirstpositionLineEdit")
        self.lecfirstpositionLayout.addWidget(self.lecfirstpositionLineEdit)
        self.layoutWidget_64 = QtWidgets.QWidget(self.lecstagepositionGroupBox)
        self.layoutWidget_64.setGeometry(QtCore.QRect(10, 80, 135, 45))
        self.layoutWidget_64.setObjectName("layoutWidget_64")
        self.leclastpositionLayout = QtWidgets.QVBoxLayout(self.layoutWidget_64)
        self.leclastpositionLayout.setContentsMargins(0, 0, 0, 0)
        self.leclastpositionLayout.setObjectName("leclastpositionLayout")
        self.leclastpositionLabel = QtWidgets.QLabel(self.layoutWidget_64)
        self.leclastpositionLabel.setObjectName("leclastpositionLabel")
        self.leclastpositionLayout.addWidget(self.leclastpositionLabel)
        self.leclastpositionLineEdit = QtWidgets.QLineEdit(self.layoutWidget_64)
        self.leclastpositionLineEdit.setStyleSheet("border-radius: 5px;\n"
"border: 2px solid grey;")
        self.leclastpositionLineEdit.setObjectName("leclastpositionLineEdit")
        self.leclastpositionLayout.addWidget(self.leclastpositionLineEdit)
        self.layoutWidget_65 = QtWidgets.QWidget(self.lecstagepositionGroupBox)
        self.layoutWidget_65.setGeometry(QtCore.QRect(10, 130, 135, 45))
        self.layoutWidget_65.setObjectName("layoutWidget_65")
        self.lecstagepositionstepsLayout = QtWidgets.QVBoxLayout(self.layoutWidget_65)
        self.lecstagepositionstepsLayout.setContentsMargins(0, 0, 0, 0)
        self.lecstagepositionstepsLayout.setObjectName("lecstagepositionstepsLayout")
        self.lecstagepositionstepsLabel = QtWidgets.QLabel(self.layoutWidget_65)
        self.lecstagepositionstepsLabel.setObjectName("lecstagepositionstepsLabel")
        self.lecstagepositionstepsLayout.addWidget(self.lecstagepositionstepsLabel)
        self.lecstagepositionstepsLineEdit = QtWidgets.QLineEdit(self.layoutWidget_65)
        self.lecstagepositionstepsLineEdit.setStyleSheet("border-radius: 5px;\n"
"border: 2px solid grey;")
        self.lecstagepositionstepsLineEdit.setObjectName("lecstagepositionstepsLineEdit")
        self.lecstagepositionstepsLayout.addWidget(self.lecstagepositionstepsLineEdit)
        self.layoutWidget_66 = QtWidgets.QWidget(self.lecstagepositionGroupBox)
        self.layoutWidget_66.setGeometry(QtCore.QRect(10, 180, 135, 45))
        self.layoutWidget_66.setObjectName("layoutWidget_66")
        self.lecstagepositioninttimeLayout = QtWidgets.QVBoxLayout(self.layoutWidget_66)
        self.lecstagepositioninttimeLayout.setContentsMargins(0, 0, 0, 0)
        self.lecstagepositioninttimeLayout.setObjectName("lecstagepositioninttimeLayout")
        self.lecstagepositioninttimeLabel = QtWidgets.QLabel(self.layoutWidget_66)
        self.lecstagepositioninttimeLabel.setObjectName("lecstagepositioninttimeLabel")
        self.lecstagepositioninttimeLayout.addWidget(self.lecstagepositioninttimeLabel)
        self.lecstagepositioninttimeLineEdit = QtWidgets.QLineEdit(self.layoutWidget_66)
        self.lecstagepositioninttimeLineEdit.setStyleSheet("border-radius: 5px;\n"
"border: 2px solid grey;")
        self.lecstagepositioninttimeLineEdit.setObjectName("lecstagepositioninttimeLineEdit")
        self.lecstagepositioninttimeLayout.addWidget(self.lecstagepositioninttimeLineEdit)
        self.layoutWidget_71 = QtWidgets.QWidget(self.lecstagepositionGroupBox)
        self.layoutWidget_71.setGeometry(QtCore.QRect(17, 235, 158, 25))
        self.layoutWidget_71.setObjectName("layoutWidget_71")
        self.lecstagepositionstartstopLayout = QtWidgets.QHBoxLayout(self.layoutWidget_71)
        self.lecstagepositionstartstopLayout.setContentsMargins(0, 0, 0, 0)
        self.lecstagepositionstartstopLayout.setObjectName("lecstagepositionstartstopLayout")
        self.lecstagepositionstartPushButton = QtWidgets.QPushButton(self.layoutWidget_71)
        self.lecstagepositionstartPushButton.setEnabled(False)
        self.lecstagepositionstartPushButton.setStyleSheet("QPushButton:pressed {\n"
"border-radius: 5px;\n"
"border: 4px solid grey;\n"
"background-color: rgb(23, 255, 96);\n"
"font-size:10px\n"
"}\n"
"QPushButton {\n"
"border-radius: 5px;\n"
"border: 4px solid grey;\n"
"background-color: rgb(23, 255, 96)\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"border-radius: 5px;\n"
"border: 4px solid grey;\n"
"background-color: rgb(170, 170, 127)\n"
"}")
        self.lecstagepositionstartPushButton.setObjectName("lecstagepositionstartPushButton")
        self.lecstagepositionstartstopLayout.addWidget(self.lecstagepositionstartPushButton)
        self.lecstagepositionstopPushButton = QtWidgets.QPushButton(self.layoutWidget_71)
        self.lecstagepositionstopPushButton.setEnabled(False)
        self.lecstagepositionstopPushButton.setStyleSheet("QPushButton:pressed {\n"
"border-radius: 5px;\n"
"border: 4px solid grey;\n"
"background-color: rgb(255, 93, 0);\n"
"font-size:10px\n"
"}\n"
"QPushButton {\n"
"border-radius: 5px;\n"
"border: 4px solid grey;\n"
"background-color: rgb(255, 93, 0)\n"
"}\n"
"QPushButton:disabled {\n"
"border-radius: 5px;\n"
"border: 4px solid grey;\n"
"background-color: rgb(170, 170, 127)\n"
"}")
        self.lecstagepositionstopPushButton.setObjectName("lecstagepositionstopPushButton")
        self.lecstagepositionstartstopLayout.addWidget(self.lecstagepositionstopPushButton)
        self.layoutWidget_72 = QtWidgets.QWidget(self.lecroyscanTab)
        self.layoutWidget_72.setGeometry(QtCore.QRect(10, 300, 501, 50))
        self.layoutWidget_72.setObjectName("layoutWidget_72")
        self.lecscanprogressLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_72)
        self.lecscanprogressLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lecscanprogressLayout_2.setObjectName("lecscanprogressLayout_2")
        self.lecscanprogressLabel = QtWidgets.QLabel(self.layoutWidget_72)
        self.lecscanprogressLabel.setObjectName("lecscanprogressLabel")
        self.lecscanprogressLayout_2.addWidget(self.lecscanprogressLabel)
        self.lecscanprogressProgressBar = QtWidgets.QProgressBar(self.layoutWidget_72)
        self.lecscanprogressProgressBar.setStyleSheet("QProgressBar{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(23, 255, 96);\n"
"    width: 10px;\n"
"    margin: 1px;\n"
"}")
        self.lecscanprogressProgressBar.setProperty("value", 0)
        self.lecscanprogressProgressBar.setObjectName("lecscanprogressProgressBar")
        self.lecscanprogressLayout_2.addWidget(self.lecscanprogressProgressBar)
        self.layoutWidget7 = QtWidgets.QWidget(self.lecroyscanTab)
        self.layoutWidget7.setGeometry(QtCore.QRect(240, 130, 41, 41))
        self.layoutWidget7.setObjectName("layoutWidget7")
        self.oscchannelLayout = QtWidgets.QVBoxLayout(self.layoutWidget7)
        self.oscchannelLayout.setContentsMargins(0, 0, 0, 0)
        self.oscchannelLayout.setObjectName("oscchannelLayout")
        self.oscchannelLabel = QtWidgets.QLabel(self.layoutWidget7)
        self.oscchannelLabel.setObjectName("oscchannelLabel")
        self.oscchannelLayout.addWidget(self.oscchannelLabel)
        self.oscchannelSpinBox = QtWidgets.QSpinBox(self.layoutWidget7)
        self.oscchannelSpinBox.setStyleSheet("border: 2px solid gray; \n"
"border-radius: 3px; \n"
" ")
        self.oscchannelSpinBox.setMinimum(1)
        self.oscchannelSpinBox.setMaximum(4)
        self.oscchannelSpinBox.setObjectName("oscchannelSpinBox")
        self.oscchannelLayout.addWidget(self.oscchannelSpinBox)
        self.tabWidget.addTab(self.lecroyscanTab, "")
        self.layoutWidget8 = QtWidgets.QWidget(LazerLabGUI)
        self.layoutWidget8.setGeometry(QtCore.QRect(20, 410, 531, 98))
        self.layoutWidget8.setObjectName("layoutWidget8")
        self.infoboxLayout = QtWidgets.QVBoxLayout(self.layoutWidget8)
        self.infoboxLayout.setContentsMargins(0, 0, 0, 0)
        self.infoboxLayout.setObjectName("infoboxLayout")
        self.infoLabel = QtWidgets.QLabel(self.layoutWidget8)
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.infoLabel.setFont(font)
        self.infoLabel.setAutoFillBackground(False)
        self.infoLabel.setObjectName("infoLabel")
        self.infoboxLayout.addWidget(self.infoLabel)
        self.infoTextBrowser = QtWidgets.QTextBrowser(self.layoutWidget8)
        self.infoTextBrowser.setObjectName("infoTextBrowser")
        self.infoboxLayout.addWidget(self.infoTextBrowser)

        self.retranslateUi(LazerLabGUI)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(LazerLabGUI)

    def retranslateUi(self, LazerLabGUI):
        _translate = QtCore.QCoreApplication.translate
        LazerLabGUI.setWindowTitle(_translate("LazerLabGUI", "LazerLab GUI 3000"))
        self.laserpowergroupBox.setTitle(_translate("LazerLabGUI", "Laser Power"))
        self.newlaserpowerLabel.setText(_translate("LazerLabGUI", "New laser power [%]"))
        self.newlaserpowersetButton.setText(_translate("LazerLabGUI", "Adjust"))
        self.connectwaveplatetextLabel.setText(_translate("LazerLabGUI", "Connect to waveplate"))
        self.connecttowaveplateButton.setText(_translate("LazerLabGUI", "Connect"))
        self.iswaveplateconnectedCheckBox.setText(_translate("LazerLabGUI", "Connection established"))
        self.currentlaserpowerLabel.setText(_translate("LazerLabGUI", "Current laser power"))
        self.stagepositiongroupBox.setTitle(_translate("LazerLabGUI", "Beam Delay"))
        self.connectstagetextLabel.setText(_translate("LazerLabGUI", "Connect to delay-stage"))
        self.connecttostageButton.setText(_translate("LazerLabGUI", "Connect"))
        self.isstageconnectedCheckBox.setText(_translate("LazerLabGUI", "Connection established"))
        self.newstagepositionLabel.setText(_translate("LazerLabGUI", "New stage position [mm]"))
        self.newstagepositionsetButton.setText(_translate("LazerLabGUI", "Move"))
        self.currentstagepositionLabel.setText(_translate("LazerLabGUI", "Current stage position [mm]"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.powerdelayTab), _translate("LazerLabGUI", "Power / Delay"))
        self.cpclaserpowerscanGroupBox.setTitle(_translate("LazerLabGUI", "Laser Power Scan"))
        self.cpcfirstpowerLabel.setText(_translate("LazerLabGUI", "First power [%]"))
        self.cpclastpowerLabel.setText(_translate("LazerLabGUI", "Last power [%]"))
        self.cpclaserpowerstepsLabel.setText(_translate("LazerLabGUI", "Steps"))
        self.cpclaserpowerinttimeLabel.setText(_translate("LazerLabGUI", "Integration time [s]"))
        self.cpclaserpowerstartPushButton.setText(_translate("LazerLabGUI", "Start scan"))
        self.cpclaserpowerstopPushButton.setText(_translate("LazerLabGUI", "Stop scan"))
        self.cpcstagescanGroupBox.setTitle(_translate("LazerLabGUI", "Beam Delay Scan"))
        self.cpcfirstpositionLabel.setText(_translate("LazerLabGUI", "Starting position [mm]"))
        self.cpclastpositionLabel.setText(_translate("LazerLabGUI", "End position [mm]"))
        self.cpcstagepositionstepsLabel.setText(_translate("LazerLabGUI", "Steps"))
        self.cpcstagepositioninttimeLabel.setText(_translate("LazerLabGUI", "Integration time [s]"))
        self.cpcstagepositionstartPushButton.setText(_translate("LazerLabGUI", "Start scan"))
        self.cpcstagepositionstopPushButton.setText(_translate("LazerLabGUI", "Stop scan"))
        self.cpcscanprogressLabel.setText(_translate("LazerLabGUI", "Scan progress"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.coboldscanTab), _translate("LazerLabGUI", "Cobold Scan"))
        self.leclaserpowerscanGroupBox.setTitle(_translate("LazerLabGUI", "Laser Power Scan"))
        self.lecfirstpowerLabel.setText(_translate("LazerLabGUI", "First power [%]"))
        self.leclastpowerLabel.setText(_translate("LazerLabGUI", "Last power [%]"))
        self.leclaserpowerstepsLabel.setText(_translate("LazerLabGUI", "Steps"))
        self.leclaserpowerinttimeLabel.setText(_translate("LazerLabGUI", "Integration time [s]"))
        self.leclaserpowerstartPushButton.setText(_translate("LazerLabGUI", "Start scan"))
        self.leclaserpowerstopPushButton.setText(_translate("LazerLabGUI", "Stop scan"))
        self.lecstagepositionGroupBox.setTitle(_translate("LazerLabGUI", "Beam Delay Scan"))
        self.lecfirstpositionLabel_2.setText(_translate("LazerLabGUI", "Starting position [mm]"))
        self.leclastpositionLabel.setText(_translate("LazerLabGUI", "End position [mm]"))
        self.lecstagepositionstepsLabel.setText(_translate("LazerLabGUI", "Steps"))
        self.lecstagepositioninttimeLabel.setText(_translate("LazerLabGUI", "Integration time [s]"))
        self.lecstagepositionstartPushButton.setText(_translate("LazerLabGUI", "Start scan"))
        self.lecstagepositionstopPushButton.setText(_translate("LazerLabGUI", "Stop scan"))
        self.lecscanprogressLabel.setText(_translate("LazerLabGUI", "Scan progress"))
        self.oscchannelLabel.setText(_translate("LazerLabGUI", "Channel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.lecroyscanTab), _translate("LazerLabGUI", "LeCroy Scan"))
        self.infoLabel.setText(_translate("LazerLabGUI", "Info"))



        #--------------------------------------------------------------------------------------#
        #--------------------------POWER/DELAY TAB---------------------------------------------#
        #--------------------------------------------------------------------------------------#

        #waveplate functionality
        self.connecttowaveplateButton.clicked.connect(self.connecttowaveplateEvent)
        self.newlaserpowersetButton.clicked.connect(self.newlaserpowersetEvent)

        #newport stage functionality
        self.connecttostageButton.clicked.connect(self.connecttostageEvent)
        self.newstagepositionsetButton.clicked.connect(self.newstagepositionsetEvent)

        #--------------------------------------------------------------------------------------#
        #--------------------------COBOLDSCANTAB-----------------------------------------------#
        #--------------------------------------------------------------------------------------#

        #Cobold PC Scan tool functionality - waveplate
        self.cpclaserpowerstartPushButton.clicked.connect(self.cpclaserpowerstartEvent)
        self.cpclaserpowerstopPushButton.clicked.connect(self.cpclaserpowerstopEvent)
        #Thread for the scan and functionality for emitting signals to main UI thread
        self.cpclaserpowerscanThread = cpclaserpowerscanThread()
        self.cpclaserpowerscanThread.T_cpcPBval.connect(self.cpcscanprogressProgressBar.setValue)
        self.cpclaserpowerscanThread.T_infoTextBrowser.connect(self.infoTextBrowser.append)
        self.cpclaserpowerscanThread.T_laserpowerprogressBar.connect(self.laserpowerprogressBar.setValue)

        #Cobold PC Scan tool functionality - stage
        self.cpcstagepositionstartPushButton.clicked.connect(self.cpcstagepositionstartEvent)
        self.cpcstagepositionstopPushButton.clicked.connect(self.cpcstagepositionstopEvent)
        #Thread for the scan and functionality for emitting signals to main UI thread
        self.cpcstagepositionscanThread = cpcstagepositionscanThread()
        self.cpcstagepositionscanThread.T_cpcPBval.connect(self.cpcscanprogressProgressBar.setValue)
        self.cpcstagepositionscanThread.T_infoTextBrowser.connect(self.infoTextBrowser.append)

        #--------------------------------------------------------------------------------------#
        #--------------------------LECROYSCANTAB-----------------------------------------------#
        #--------------------------------------------------------------------------------------#

        #LeCroy PC Scan tool functionality - waveplate
        self.leclaserpowerstartPushButton.clicked.connect(self.leclaserpowerstartEvent)
        self.leclaserpowerstopPushButton.clicked.connect(self.leclaserpowerstopEvent)
        #Thread for the scan and functionality for emitting signals to main UI thread
        self.leclaserpowerscanThread = leclaserpowerscanThread()
        self.leclaserpowerscanThread.T_lecPBval.connect(self.lecscanprogressProgressBar.setValue)
        self.leclaserpowerscanThread.T_infoTextBrowser.connect(self.infoTextBrowser.append)
        self.leclaserpowerscanThread.T_laserpowerprogressBar.connect(self.laserpowerprogressBar.setValue)

        #LeCroy PC Scan tool functionality - stage
        self.lecstagepositionstartPushButton.clicked.connect(self.lecstagepositionstartEvent)
        self.lecstagepositionstopPushButton.clicked.connect(self.lecstagepositionstopEvent)
        #Thread for the scan and functionality for emitting signals to main UI thread
        self.lecstagepositionscanThread = lecstagepositionscanThread()
        self.lecstagepositionscanThread.T_lecPBval.connect(self.lecscanprogressProgressBar.setValue)
        self.lecstagepositionscanThread.T_infoTextBrowser.connect(self.infoTextBrowser.append)

    #--------------------------------------------------------------------------------------#
    #--------------------------POWER/DELAY TAB FUNCTIONS-----------------------------------#
    #--------------------------------------------------------------------------------------#

    #WAVEPLATE
    def connecttowaveplateEvent(self):
        try:
            ## initial text for infobox
            self.infoTextBrowser.append('Trying to connect to waveplate ...')

            #<<--function that is connecting to the waveplate
            self.iswaveplateconnectedCheckBox.setChecked(True)
            #<<--function that reads current power setting & sets it in the window

            ## enable buttons that are related to changing the laser intensity
            self.newlaserpowersetButton.setEnabled(True)
            self.cpclaserpowerstartPushButton.setEnabled(True)
            self.cpclaserpowerstopPushButton.setEnabled(True)
            self.leclaserpowerstartPushButton.setEnabled(True)
            self.leclaserpowerstopPushButton.setEnabled(True)

            ## finishing text for infobox
            self.infoTextBrowser.append('Connection to the waveplate is established.')
            self.connecttowaveplateButton.setEnabled(False)

        except:
            ## error message for info box
            self.infoTextBrowser.append('Could not connect to waveplate.')

    def newlaserpowersetEvent(self):
        try:
            ## inital text for infobox
            self.infoTextBrowser.append(f'Setting laser power to {float(self.newlaserpowerLineEdit.text())} %')
            #<<--function that changes the laser power
            self.laserpowerprogressBar.setValue(float(self.newlaserpowerLineEdit.text()))
        except:
            ## error message for infobox
            self.infoTextBrowser.append('Power could not be set.')

    #STAGE
    def connecttostageEvent(self):
        try:
            ## initial text for infobox
            self.infoTextBrowser.append('Trying to connect to the stage ...')
            #<<--function that is connecting to the waveplate
            self.isstageconnectedCheckBox.setChecked(True)
            #<<--function that reads current stage position & updates stage position field

            ## enable buttons that are related to changing the stage position
            self.newstagepositionsetButton.setEnabled(True)
            self.cpcstagepositionstartPushButton.setEnabled(True)
            self.cpcstagepositionstopPushButton.setEnabled(True)
            self.lecstagepositionstartPushButton.setEnabled(True)
            self.lecstagepositionstopPushButton.setEnabled(True)

            ## finishing text for infobox
            self.infoTextBrowser.append('Connection to the stage is established.')
            self.connecttostageButton.setEnabled(False)


        except:
            ## error message for info box
            self.infoTextBrowser.append('Could not connect to waveplate.')

    def newstagepositionsetEvent(self):
        try:
            ## inital text for infobox
            stvalue = float(self.newstagepositionLineEdit.text())
            self.infoTextBrowser.append(f'Setting stage position to {stvalue:.4f} mm')
            #<<--function that changes the stage position
            self.displaycurrentstagepostitionLineEdit.setText(f'{stvalue:.4f}')

        except:
            ## error message for infobox
            self.infoTextBrowser.append('Stage position could not be set.')


    #--------------------------------------------------------------------------------------#
    #--------------------------COBOLDSCANTAB FUNCTIONS-------------------------------------#
    #--------------------------------------------------------------------------------------#

    #Laser power
    def cpclaserpowerstartEvent(self):
        self.cpclaserpowerscanThread.T_cpclpfirst = int(self.cpcfirstpowerLineEdit.text())
        self.cpclaserpowerscanThread.T_cpclplast = int(self.cpclastpowerLineEdit.text())
        self.cpclaserpowerscanThread.T_cpclpsteps = int(self.cpclaserpowerstepsLineEdit.text())
        self.cpclaserpowerscanThread.T_cpclpinttime = int(self.cpclaserpowerinttimeLineEdit.text())

        self.cpclaserpowerscanThread.T_threadactive = True
        self.cpclaserpowerscanThread.start()

    def cpclaserpowerstopEvent(self):
        self.cpclaserpowerscanThread.stop()
        self.infoTextBrowser.append('The laser power scan has been aborted.')

    #Stage position
    def cpcstagepositionstartEvent(self):
        self.cpcstagepositionscanThread.T_cpcspfirst = int(self.cpcfirstpositionLineEdit.text())
        self.cpcstagepositionscanThread.T_cpcsplast = int(self.cpclastpositionLineEdit.text())
        self.cpcstagepositionscanThread.T_cpcspsteps = int(self.cpcstagepositionstepsLineEdit.text())
        self.cpcstagepositionscanThread.T_cpcspinttime = int(self.cpcstagepositioninttimeLineEdit.text())

        self.cpcstagepositionscanThread.T_threadactive = True
        self.cpcstagepositionscanThread.start()

    def cpcstagepositionstopEvent(self):
        self.cpcstagepositionscanThread.stop()
        self.infoTextBrowser.append('The stage position scan has been aborted.')

    #--------------------------------------------------------------------------------------#
    #--------------------------LECROYSCANTAB FUNCTIONS-------------------------------------#
    #--------------------------------------------------------------------------------------#

    #Laser power
    def leclaserpowerstartEvent(self):
        self.leclaserpowerscanThread.T_leclpfirst = int(self.lecfirstpowerLineEdit.text())
        self.leclaserpowerscanThread.T_leclplast = int(self.leclastpowerLineEdit.text())
        self.leclaserpowerscanThread.T_leclpsteps = int(self.leclaserpowerstepsLineEdit.text())
        self.leclaserpowerscanThread.T_leclpinttime = int(self.leclaserpowerinttimeLineEdit.text())
        self.leclaserpowerscanThread.T_oscchannel = self.oscchannelSpinBox.value()

        self.leclaserpowerscanThread.T_threadactive = True
        self.leclaserpowerscanThread.start()        

    def leclaserpowerstopEvent(self):
        self.leclaserpowerscanThread.stop()
        self.infoTextBrowser.append('The laser power scan has been aborted.')

    #Stage position
    def lecstagepositionstartEvent(self):
        self.lecstagepositionscanThread.T_lecspfirst = int(self.lecfirstpositionLineEdit.text())
        self.lecstagepositionscanThread.T_lecsplast = int(self.leclastpositionLineEdit.text())
        self.lecstagepositionscanThread.T_lecspsteps = int(self.lecstagepositionstepsLineEdit.text())
        self.lecstagepositionscanThread.T_lecspinttime = int(self.lecstagepositioninttimeLineEdit.text())
        self.lecstagepositionscanThread.T_oscchannel = self.oscchannelSpinBox.value()

        self.lecstagepositionscanThread.T_threadactive = True
        self.lecstagepositionscanThread.start()

    def lecstagepositionstopEvent(self):
        self.lecstagepositionscanThread.stop()
        self.infoTextBrowser.append('The stage position scan has been aborted.')



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LazerLabGUI = QtWidgets.QDialog()
    ui = Ui_LazerLabGUI()
    ui.setupUi(LazerLabGUI)
    LazerLabGUI.show()
    sys.exit(app.exec_())
