# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectMode.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(588, 751)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(588, 747))
        Dialog.setMaximumSize(QtCore.QSize(588, 16777215))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 1, 0, 1, 1)
        self.verticalFrame = QtWidgets.QFrame(Dialog)
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.timeFrame = QtWidgets.QFrame(self.verticalFrame)
        self.timeFrame.setObjectName("timeFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.timeFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox = QtWidgets.QCheckBox(self.timeFrame)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.spinBox = QtWidgets.QSpinBox(self.timeFrame)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.verticalLayout.addWidget(self.timeFrame)
        self.verticalFrame_2 = QtWidgets.QFrame(self.verticalFrame)
        self.verticalFrame_2.setObjectName("verticalFrame_2")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.checkBox_2 = QtWidgets.QCheckBox(self.verticalFrame_2)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_22.addWidget(self.checkBox_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem1)
        self.pushButton_13 = QtWidgets.QPushButton(self.verticalFrame_2)
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_22.addWidget(self.pushButton_13)
        self.verticalLayout_13.addLayout(self.horizontalLayout_22)
        self.verticalFrame_21 = QtWidgets.QFrame(self.verticalFrame_2)
        self.verticalFrame_21.setObjectName("verticalFrame_21")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalFrame_21)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.label_12 = QtWidgets.QLabel(self.verticalFrame_21)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_25.addWidget(self.label_12)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem2)
        self.spinBox_11 = QtWidgets.QSpinBox(self.verticalFrame_21)
        self.spinBox_11.setObjectName("spinBox_11")
        self.horizontalLayout_25.addWidget(self.spinBox_11)
        self.pushButton_15 = QtWidgets.QPushButton(self.verticalFrame_21)
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout_25.addWidget(self.pushButton_15)
        self.verticalLayout_9.addLayout(self.horizontalLayout_25)
        self.verticalLayout_13.addWidget(self.verticalFrame_21)
        self.verticalLayout.addWidget(self.verticalFrame_2)
        self.verticalFrame_22 = QtWidgets.QFrame(self.verticalFrame)
        self.verticalFrame_22.setObjectName("verticalFrame_22")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalFrame_22)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.checkBox_3 = QtWidgets.QCheckBox(self.verticalFrame_22)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout_10.addWidget(self.checkBox_3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem3)
        self.pushButton_7 = QtWidgets.QPushButton(self.verticalFrame_22)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_10.addWidget(self.pushButton_7)
        self.verticalLayout_6.addLayout(self.horizontalLayout_10)
        self.verticalFrame_4 = QtWidgets.QFrame(self.verticalFrame_22)
        self.verticalFrame_4.setObjectName("verticalFrame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalFrame_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_7 = QtWidgets.QLabel(self.verticalFrame_4)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_14.addWidget(self.label_7)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem4)
        self.spinBox_6 = QtWidgets.QSpinBox(self.verticalFrame_4)
        self.spinBox_6.setObjectName("spinBox_6")
        self.horizontalLayout_14.addWidget(self.spinBox_6)
        self.pushButton_8 = QtWidgets.QPushButton(self.verticalFrame_4)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_14.addWidget(self.pushButton_8)
        self.verticalLayout_4.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_8 = QtWidgets.QLabel(self.verticalFrame_4)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_15.addWidget(self.label_8)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem5)
        self.spinBox_7 = QtWidgets.QSpinBox(self.verticalFrame_4)
        self.spinBox_7.setObjectName("spinBox_7")
        self.horizontalLayout_15.addWidget(self.spinBox_7)
        self.pushButton_9 = QtWidgets.QPushButton(self.verticalFrame_4)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_15.addWidget(self.pushButton_9)
        self.verticalLayout_4.addLayout(self.horizontalLayout_15)
        self.verticalLayout_6.addWidget(self.verticalFrame_4)
        self.verticalLayout.addWidget(self.verticalFrame_22)
        self.fileFrame = QtWidgets.QFrame(self.verticalFrame)
        self.fileFrame.setObjectName("fileFrame")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.fileFrame)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox_4 = QtWidgets.QCheckBox(self.fileFrame)
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalLayout_2.addWidget(self.checkBox_4)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.pushButton = QtWidgets.QPushButton(self.fileFrame)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout_18.addLayout(self.horizontalLayout_2)
        self.frame = QtWidgets.QFrame(self.fileFrame)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_6.addWidget(self.pushButton_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem8)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_8.addWidget(self.pushButton_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.verticalLayout_18.addWidget(self.frame)
        self.verticalLayout.addWidget(self.fileFrame)
        self.fileIntervalFrame = QtWidgets.QFrame(self.verticalFrame)
        self.fileIntervalFrame.setObjectName("fileIntervalFrame")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.fileIntervalFrame)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkBox_5 = QtWidgets.QCheckBox(self.fileIntervalFrame)
        self.checkBox_5.setObjectName("checkBox_5")
        self.horizontalLayout_3.addWidget(self.checkBox_5)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.pushButton_2 = QtWidgets.QPushButton(self.fileIntervalFrame)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.verticalLayout_10.addLayout(self.horizontalLayout_3)
        self.frame1 = QtWidgets.QFrame(self.fileIntervalFrame)
        self.frame1.setObjectName("frame1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_2 = QtWidgets.QLabel(self.frame1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_11.addWidget(self.label_2)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem10)
        self.spinBox_4 = QtWidgets.QSpinBox(self.frame1)
        self.spinBox_4.setObjectName("spinBox_4")
        self.horizontalLayout_11.addWidget(self.spinBox_4)
        self.label = QtWidgets.QLabel(self.frame1)
        self.label.setObjectName("label")
        self.horizontalLayout_11.addWidget(self.label)
        self.spinBox_2 = QtWidgets.QSpinBox(self.frame1)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_11.addWidget(self.spinBox_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_11.addWidget(self.pushButton_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_3 = QtWidgets.QLabel(self.frame1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_12.addWidget(self.label_3)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem11)
        self.spinBox_5 = QtWidgets.QSpinBox(self.frame1)
        self.spinBox_5.setObjectName("spinBox_5")
        self.horizontalLayout_12.addWidget(self.spinBox_5)
        self.label_6 = QtWidgets.QLabel(self.frame1)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_12.addWidget(self.label_6)
        self.spinBox_3 = QtWidgets.QSpinBox(self.frame1)
        self.spinBox_3.setObjectName("spinBox_3")
        self.horizontalLayout_12.addWidget(self.spinBox_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame1)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_12.addWidget(self.pushButton_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_12)
        self.verticalLayout_10.addWidget(self.frame1)
        self.verticalLayout.addWidget(self.fileIntervalFrame)
        self.errorFrame = QtWidgets.QFrame(self.verticalFrame)
        self.errorFrame.setObjectName("errorFrame")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.errorFrame)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.checkBox_6 = QtWidgets.QCheckBox(self.errorFrame)
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout_11.addWidget(self.checkBox_6)
        self.verticalLayout.addWidget(self.errorFrame)
        self.interruptFrame = QtWidgets.QFrame(self.verticalFrame)
        self.interruptFrame.setObjectName("interruptFrame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.interruptFrame)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.checkBox_9 = QtWidgets.QCheckBox(self.interruptFrame)
        self.checkBox_9.setObjectName("checkBox_9")
        self.horizontalLayout_7.addWidget(self.checkBox_9)
        self.verticalLayout.addWidget(self.interruptFrame)
        self.gridLayout.addWidget(self.verticalFrame, 4, 0, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Select Git-Auto-Commit Modes"))
        self.radioButton_2.setText(_translate("Dialog", "Commit on conditions"))
        self.checkBox.setText(_translate("Dialog", "Commit to a certain time interval (minutes)"))
        self.checkBox_2.setText(_translate("Dialog", "Commit to a certain time interval based on the creation time of a file"))
        self.pushButton_13.setText(_translate("Dialog", "Add files"))
        self.label_12.setText(_translate("Dialog", "file name"))
        self.pushButton_15.setText(_translate("Dialog", "Delete"))
        self.checkBox_3.setText(_translate("Dialog", "Commit when changes occur to a file of more than a certain percentage"))
        self.pushButton_7.setText(_translate("Dialog", "Add files"))
        self.label_7.setText(_translate("Dialog", "file name"))
        self.pushButton_8.setText(_translate("Dialog", "Delete"))
        self.label_8.setText(_translate("Dialog", "file name"))
        self.pushButton_9.setText(_translate("Dialog", "Delete"))
        self.checkBox_4.setText(_translate("Dialog", "Commit when particular files changes"))
        self.pushButton.setText(_translate("Dialog", "Add files"))
        self.label_4.setText(_translate("Dialog", "file name"))
        self.pushButton_5.setText(_translate("Dialog", "Delete"))
        self.label_5.setText(_translate("Dialog", "file name"))
        self.pushButton_6.setText(_translate("Dialog", "Delete"))
        self.checkBox_5.setText(_translate("Dialog", "Commit when a specific intervals of particular files changes"))
        self.pushButton_2.setText(_translate("Dialog", "PushButton"))
        self.label_2.setText(_translate("Dialog", "file name"))
        self.label.setText(_translate("Dialog", "~"))
        self.pushButton_3.setText(_translate("Dialog", "Delete"))
        self.label_3.setText(_translate("Dialog", "file name"))
        self.label_6.setText(_translate("Dialog", "~"))
        self.pushButton_4.setText(_translate("Dialog", "Delete"))
        self.checkBox_6.setText(_translate("Dialog", "Commit in the event of an error"))
        self.checkBox_9.setText(_translate("Dialog", "Commit in the event of interrupt execution"))
        self.radioButton.setText(_translate("Dialog", "Commit whenever changes occur"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())