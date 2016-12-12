# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EventQueryDialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_EventQueryDialog(object):
    def setupUi(self, EventQueryDialog):
        EventQueryDialog.setObjectName(_fromUtf8("EventQueryDialog"))
        EventQueryDialog.resize(550, 710)
        EventQueryDialog.setMinimumSize(QtCore.QSize(450, 710))
        self.verticalLayout = QtGui.QVBoxLayout(EventQueryDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.timeGroupBox = QtGui.QGroupBox(EventQueryDialog)
        self.timeGroupBox.setObjectName(_fromUtf8("timeGroupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.timeGroupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.timeBetweenRadioButton = QtGui.QRadioButton(self.timeGroupBox)
        self.timeBetweenRadioButton.setEnabled(True)
        self.timeBetweenRadioButton.setChecked(True)
        self.timeBetweenRadioButton.setObjectName(_fromUtf8("timeBetweenRadioButton"))
        self.verticalLayout_2.addWidget(self.timeBetweenRadioButton)
        self.timeWidget = QtGui.QWidget(self.timeGroupBox)
        self.timeWidget.setMinimumSize(QtCore.QSize(0, 45))
        self.timeWidget.setObjectName(_fromUtf8("timeWidget"))
        self.endtimeDateTimeEdit = QtGui.QDateTimeEdit(self.timeWidget)
        self.endtimeDateTimeEdit.setGeometry(QtCore.QRect(300, 12, 144, 24))
        self.endtimeDateTimeEdit.setCalendarPopup(True)
        self.endtimeDateTimeEdit.setTimeSpec(QtCore.Qt.UTC)
        self.endtimeDateTimeEdit.setObjectName(_fromUtf8("endtimeDateTimeEdit"))
        self.starttimeDateTimeEdit = QtGui.QDateTimeEdit(self.timeWidget)
        self.starttimeDateTimeEdit.setGeometry(QtCore.QRect(70, 12, 160, 24))
        self.starttimeDateTimeEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.starttimeDateTimeEdit.setCalendarPopup(True)
        self.starttimeDateTimeEdit.setTimeSpec(QtCore.Qt.UTC)
        self.starttimeDateTimeEdit.setObjectName(_fromUtf8("starttimeDateTimeEdit"))
        self.starttimeLabel = QtGui.QLabel(self.timeWidget)
        self.starttimeLabel.setGeometry(QtCore.QRect(25, 12, 40, 16))
        self.starttimeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.starttimeLabel.setObjectName(_fromUtf8("starttimeLabel"))
        self.endtimeLabele = QtGui.QLabel(self.timeWidget)
        self.endtimeLabele.setGeometry(QtCore.QRect(255, 12, 40, 16))
        self.endtimeLabele.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.endtimeLabele.setObjectName(_fromUtf8("endtimeLabele"))
        self.verticalLayout_2.addWidget(self.timeWidget)
        self.timeDuringStationsRadioButton = QtGui.QRadioButton(self.timeGroupBox)
        self.timeDuringStationsRadioButton.setObjectName(_fromUtf8("timeDuringStationsRadioButton"))
        self.verticalLayout_2.addWidget(self.timeDuringStationsRadioButton)
        self.verticalLayout.addWidget(self.timeGroupBox)
        self.magnitudeGroupBox = QtGui.QGroupBox(EventQueryDialog)
        self.magnitudeGroupBox.setMinimumSize(QtCore.QSize(0, 45))
        self.magnitudeGroupBox.setObjectName(_fromUtf8("magnitudeGroupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.magnitudeGroupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.magnitudeWidget = QtGui.QWidget(self.magnitudeGroupBox)
        self.magnitudeWidget.setObjectName(_fromUtf8("magnitudeWidget"))
        self.minmagLineEdit = QtGui.QLineEdit(self.magnitudeWidget)
        self.minmagLineEdit.setGeometry(QtCore.QRect(20, 12, 60, 21))
        self.minmagLineEdit.setObjectName(_fromUtf8("minmagLineEdit"))
        self.maxmagLineEdit = QtGui.QLineEdit(self.magnitudeWidget)
        self.maxmagLineEdit.setGeometry(QtCore.QRect(100, 12, 60, 21))
        self.maxmagLineEdit.setObjectName(_fromUtf8("maxmagLineEdit"))
        self.magtypeComboBox = QtGui.QComboBox(self.magnitudeWidget)
        self.magtypeComboBox.setEnabled(True)
        self.magtypeComboBox.setGeometry(QtCore.QRect(250, 10, 190, 26))
        self.magtypeComboBox.setObjectName(_fromUtf8("magtypeComboBox"))
        self.magtypeComboBox.addItem(_fromUtf8(""))
        self.magtypeComboBox.addItem(_fromUtf8(""))
        self.magtypeComboBox.addItem(_fromUtf8(""))
        self.magtypeComboBox.addItem(_fromUtf8(""))
        self.magtypeComboBox.addItem(_fromUtf8(""))
        self.label = QtGui.QLabel(self.magnitudeWidget)
        self.label.setGeometry(QtCore.QRect(85, 12, 10, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_3.addWidget(self.magnitudeWidget)
        self.verticalLayout.addWidget(self.magnitudeGroupBox)
        self.depthGroupBox = QtGui.QGroupBox(EventQueryDialog)
        self.depthGroupBox.setObjectName(_fromUtf8("depthGroupBox"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.depthGroupBox)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.depthWidget = QtGui.QWidget(self.depthGroupBox)
        self.depthWidget.setMinimumSize(QtCore.QSize(0, 45))
        self.depthWidget.setObjectName(_fromUtf8("depthWidget"))
        self.mindepthLineEdit = QtGui.QLineEdit(self.depthWidget)
        self.mindepthLineEdit.setGeometry(QtCore.QRect(20, 12, 60, 21))
        self.mindepthLineEdit.setObjectName(_fromUtf8("mindepthLineEdit"))
        self.maxdepthLineEdit = QtGui.QLineEdit(self.depthWidget)
        self.maxdepthLineEdit.setGeometry(QtCore.QRect(100, 12, 60, 21))
        self.maxdepthLineEdit.setObjectName(_fromUtf8("maxdepthLineEdit"))
        self.label_2 = QtGui.QLabel(self.depthWidget)
        self.label_2.setGeometry(QtCore.QRect(85, 12, 10, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_5.addWidget(self.depthWidget)
        self.verticalLayout.addWidget(self.depthGroupBox)
        self.locationGroupBox = QtGui.QGroupBox(EventQueryDialog)
        self.locationGroupBox.setMinimumSize(QtCore.QSize(0, 375))
        self.locationGroupBox.setObjectName(_fromUtf8("locationGroupBox"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.locationGroupBox)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.locationRangeRadioButton = QtGui.QRadioButton(self.locationGroupBox)
        self.locationRangeRadioButton.setChecked(True)
        self.locationRangeRadioButton.setObjectName(_fromUtf8("locationRangeRadioButton"))
        self.verticalLayout_4.addWidget(self.locationRangeRadioButton)
        self.locationRangeWidget = QtGui.QWidget(self.locationGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.locationRangeWidget.sizePolicy().hasHeightForWidth())
        self.locationRangeWidget.setSizePolicy(sizePolicy)
        self.locationRangeWidget.setMinimumSize(QtCore.QSize(0, 120))
        self.locationRangeWidget.setObjectName(_fromUtf8("locationRangeWidget"))
        self.locationRangeEastLineEdit = QtGui.QLineEdit(self.locationRangeWidget)
        self.locationRangeEastLineEdit.setGeometry(QtCore.QRect(90, 40, 60, 21))
        self.locationRangeEastLineEdit.setObjectName(_fromUtf8("locationRangeEastLineEdit"))
        self.locationRangeWestLineEdit = QtGui.QLineEdit(self.locationRangeWidget)
        self.locationRangeWestLineEdit.setGeometry(QtCore.QRect(20, 40, 60, 21))
        self.locationRangeWestLineEdit.setObjectName(_fromUtf8("locationRangeWestLineEdit"))
        self.locationRangeNorthLineEdit = QtGui.QLineEdit(self.locationRangeWidget)
        self.locationRangeNorthLineEdit.setGeometry(QtCore.QRect(60, 12, 60, 21))
        self.locationRangeNorthLineEdit.setObjectName(_fromUtf8("locationRangeNorthLineEdit"))
        self.locationRangeSouthLineEdit = QtGui.QLineEdit(self.locationRangeWidget)
        self.locationRangeSouthLineEdit.setGeometry(QtCore.QRect(60, 70, 60, 21))
        self.locationRangeSouthLineEdit.setObjectName(_fromUtf8("locationRangeSouthLineEdit"))
        self.verticalLayout_4.addWidget(self.locationRangeWidget)
        self.locationDistanceFromPointRadioButton = QtGui.QRadioButton(self.locationGroupBox)
        self.locationDistanceFromPointRadioButton.setEnabled(True)
        self.locationDistanceFromPointRadioButton.setObjectName(_fromUtf8("locationDistanceFromPointRadioButton"))
        self.verticalLayout_4.addWidget(self.locationDistanceFromPointRadioButton)
        self.distanceFromPointWidget = QtGui.QWidget(self.locationGroupBox)
        self.distanceFromPointWidget.setMinimumSize(QtCore.QSize(0, 80))
        self.distanceFromPointWidget.setObjectName(_fromUtf8("distanceFromPointWidget"))
        self.distanceFromPointEastLineEdit = QtGui.QLineEdit(self.distanceFromPointWidget)
        self.distanceFromPointEastLineEdit.setEnabled(True)
        self.distanceFromPointEastLineEdit.setGeometry(QtCore.QRect(70, 40, 60, 21))
        self.distanceFromPointEastLineEdit.setObjectName(_fromUtf8("distanceFromPointEastLineEdit"))
        self.label_8 = QtGui.QLabel(self.distanceFromPointWidget)
        self.label_8.setEnabled(True)
        self.label_8.setGeometry(QtCore.QRect(135, 40, 10, 16))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.distanceFromPointWidget)
        self.label_9.setEnabled(True)
        self.label_9.setGeometry(QtCore.QRect(225, 40, 10, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.distanceFromPointMinRadiusLineEdit = QtGui.QLineEdit(self.distanceFromPointWidget)
        self.distanceFromPointMinRadiusLineEdit.setEnabled(True)
        self.distanceFromPointMinRadiusLineEdit.setGeometry(QtCore.QRect(20, 10, 60, 21))
        self.distanceFromPointMinRadiusLineEdit.setObjectName(_fromUtf8("distanceFromPointMinRadiusLineEdit"))
        self.label_10 = QtGui.QLabel(self.distanceFromPointWidget)
        self.label_10.setEnabled(True)
        self.label_10.setGeometry(QtCore.QRect(85, 10, 10, 16))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.distanceFromPointMaxRadiusLineEdit = QtGui.QLineEdit(self.distanceFromPointWidget)
        self.distanceFromPointMaxRadiusLineEdit.setEnabled(True)
        self.distanceFromPointMaxRadiusLineEdit.setGeometry(QtCore.QRect(100, 10, 60, 21))
        self.distanceFromPointMaxRadiusLineEdit.setObjectName(_fromUtf8("distanceFromPointMaxRadiusLineEdit"))
        self.distanceFromPointNorthLineEdit = QtGui.QLineEdit(self.distanceFromPointWidget)
        self.distanceFromPointNorthLineEdit.setEnabled(True)
        self.distanceFromPointNorthLineEdit.setGeometry(QtCore.QRect(160, 40, 60, 21))
        self.distanceFromPointNorthLineEdit.setObjectName(_fromUtf8("distanceFromPointNorthLineEdit"))
        self.label_11 = QtGui.QLabel(self.distanceFromPointWidget)
        self.label_11.setEnabled(True)
        self.label_11.setGeometry(QtCore.QRect(165, 10, 60, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_6 = QtGui.QLabel(self.distanceFromPointWidget)
        self.label_6.setEnabled(True)
        self.label_6.setGeometry(QtCore.QRect(20, 40, 40, 13))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_10.raise_()
        self.distanceFromPointMaxRadiusLineEdit.raise_()
        self.distanceFromPointMinRadiusLineEdit.raise_()
        self.label_11.raise_()
        self.distanceFromPointEastLineEdit.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.distanceFromPointNorthLineEdit.raise_()
        self.label_6.raise_()
        self.verticalLayout_4.addWidget(self.distanceFromPointWidget)
        self.locationDistanceFromStationsRadioButton = QtGui.QRadioButton(self.locationGroupBox)
        self.locationDistanceFromStationsRadioButton.setEnabled(False)
        self.locationDistanceFromStationsRadioButton.setObjectName(_fromUtf8("locationDistanceFromStationsRadioButton"))
        self.verticalLayout_4.addWidget(self.locationDistanceFromStationsRadioButton)
        self.distanceFromStationsWidget = QtGui.QWidget(self.locationGroupBox)
        self.distanceFromStationsWidget.setMinimumSize(QtCore.QSize(0, 45))
        self.distanceFromStationsWidget.setObjectName(_fromUtf8("distanceFromStationsWidget"))
        self.distanceFromStationsMinradiusLineEdit = QtGui.QLineEdit(self.distanceFromStationsWidget)
        self.distanceFromStationsMinradiusLineEdit.setEnabled(False)
        self.distanceFromStationsMinradiusLineEdit.setGeometry(QtCore.QRect(20, 12, 60, 21))
        self.distanceFromStationsMinradiusLineEdit.setObjectName(_fromUtf8("distanceFromStationsMinradiusLineEdit"))
        self.label_3 = QtGui.QLabel(self.distanceFromStationsWidget)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(85, 12, 10, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.distanceFromStationsMaxradiusLineEdit = QtGui.QLineEdit(self.distanceFromStationsWidget)
        self.distanceFromStationsMaxradiusLineEdit.setEnabled(False)
        self.distanceFromStationsMaxradiusLineEdit.setGeometry(QtCore.QRect(100, 12, 60, 21))
        self.distanceFromStationsMaxradiusLineEdit.setObjectName(_fromUtf8("distanceFromStationsMaxradiusLineEdit"))
        self.label_5 = QtGui.QLabel(self.distanceFromStationsWidget)
        self.label_5.setEnabled(True)
        self.label_5.setGeometry(QtCore.QRect(165, 12, 60, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_4.addWidget(self.distanceFromStationsWidget)
        self.verticalLayout.addWidget(self.locationGroupBox)

        self.retranslateUi(EventQueryDialog)
        QtCore.QMetaObject.connectSlotsByName(EventQueryDialog)

    def retranslateUi(self, EventQueryDialog):
        EventQueryDialog.setWindowTitle(_translate("EventQueryDialog", "Dialog", None))
        self.timeGroupBox.setTitle(_translate("EventQueryDialog", "Time", None))
        self.timeBetweenRadioButton.setText(_translate("EventQueryDialog", "Between start and end times", None))
        self.endtimeDateTimeEdit.setDisplayFormat(_translate("EventQueryDialog", "yyyy-MM-dd hh:mm:ss", None))
        self.starttimeDateTimeEdit.setDisplayFormat(_translate("EventQueryDialog", "yyyy-MM-dd hh:mm:ss", None))
        self.starttimeLabel.setText(_translate("EventQueryDialog", "start", None))
        self.endtimeLabele.setText(_translate("EventQueryDialog", "end", None))
        self.timeDuringStationsRadioButton.setText(_translate("EventQueryDialog", "During operation of selected stations", None))
        self.magnitudeGroupBox.setTitle(_translate("EventQueryDialog", "Magnitude", None))
        self.minmagLineEdit.setText(_translate("EventQueryDialog", "0", None))
        self.maxmagLineEdit.setText(_translate("EventQueryDialog", "10", None))
        self.magtypeComboBox.setItemText(0, _translate("EventQueryDialog", "All Types", None))
        self.magtypeComboBox.setItemText(1, _translate("EventQueryDialog", "TB", None))
        self.magtypeComboBox.setItemText(2, _translate("EventQueryDialog", "ML", None))
        self.magtypeComboBox.setItemText(3, _translate("EventQueryDialog", "MS", None))
        self.magtypeComboBox.setItemText(4, _translate("EventQueryDialog", "MW", None))
        self.label.setText(_translate("EventQueryDialog", "-", None))
        self.depthGroupBox.setTitle(_translate("EventQueryDialog", "Depth", None))
        self.mindepthLineEdit.setText(_translate("EventQueryDialog", "0", None))
        self.maxdepthLineEdit.setText(_translate("EventQueryDialog", "6000", None))
        self.label_2.setText(_translate("EventQueryDialog", "-", None))
        self.locationGroupBox.setTitle(_translate("EventQueryDialog", "Location", None))
        self.locationRangeRadioButton.setText(_translate("EventQueryDialog", "Within lat/lon box", None))
        self.locationDistanceFromPointRadioButton.setText(_translate("EventQueryDialog", "Distance from point", None))
        self.label_8.setText(_translate("EventQueryDialog", "E", None))
        self.label_9.setText(_translate("EventQueryDialog", "N", None))
        self.label_10.setText(_translate("EventQueryDialog", "-", None))
        self.label_11.setText(_translate("EventQueryDialog", "degrees", None))
        self.label_6.setText(_translate("EventQueryDialog", "from", None))
        self.locationDistanceFromStationsRadioButton.setText(_translate("EventQueryDialog", "Distance from selected stations", None))
        self.label_3.setText(_translate("EventQueryDialog", "-", None))
        self.label_5.setText(_translate("EventQueryDialog", "degrees", None))

