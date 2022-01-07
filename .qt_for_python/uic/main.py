# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 860)
        MainWindow.setMinimumSize(QSize(940, 560))
        MainWindow.setBaseSize(QSize(0, 0))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.verticalLayout_19 = QVBoxLayout(self.styleSheet)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setStyleSheet(u"background-image: url(:/images/images/images/logo_gaitubao_40x40.png);")
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_init = QPushButton(self.topMenu)
        self.btn_init.setObjectName(u"btn_init")
        sizePolicy.setHeightForWidth(self.btn_init.sizePolicy().hasHeightForWidth())
        self.btn_init.setSizePolicy(sizePolicy)
        self.btn_init.setMinimumSize(QSize(0, 45))
        self.btn_init.setFont(font)
        self.btn_init.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_init.setLayoutDirection(Qt.LeftToRight)
        self.btn_init.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-library.png);")

        self.verticalLayout_8.addWidget(self.btn_init)

        self.btn_product = QPushButton(self.topMenu)
        self.btn_product.setObjectName(u"btn_product")
        sizePolicy.setHeightForWidth(self.btn_product.sizePolicy().hasHeightForWidth())
        self.btn_product.setSizePolicy(sizePolicy)
        self.btn_product.setMinimumSize(QSize(0, 45))
        self.btn_product.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_product.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-devices.png);")

        self.verticalLayout_8.addWidget(self.btn_product)

        self.btn_biddingflow = QPushButton(self.topMenu)
        self.btn_biddingflow.setObjectName(u"btn_biddingflow")
        sizePolicy.setHeightForWidth(self.btn_biddingflow.sizePolicy().hasHeightForWidth())
        self.btn_biddingflow.setSizePolicy(sizePolicy)
        self.btn_biddingflow.setMinimumSize(QSize(0, 45))
        self.btn_biddingflow.setFont(font)
        self.btn_biddingflow.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_biddingflow.setLayoutDirection(Qt.LeftToRight)
        self.btn_biddingflow.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-library-add.png);")

        self.verticalLayout_8.addWidget(self.btn_biddingflow)

        self.btn_record = QPushButton(self.topMenu)
        self.btn_record.setObjectName(u"btn_record")
        sizePolicy.setHeightForWidth(self.btn_record.sizePolicy().hasHeightForWidth())
        self.btn_record.setSizePolicy(sizePolicy)
        self.btn_record.setMinimumSize(QSize(0, 45))
        self.btn_record.setFont(font)
        self.btn_record.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_record.setLayoutDirection(Qt.LeftToRight)
        self.btn_record.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-save.png);")

        self.verticalLayout_8.addWidget(self.btn_record)

        self.btn_tools = QPushButton(self.topMenu)
        self.btn_tools.setObjectName(u"btn_tools")
        self.btn_tools.setMinimumSize(QSize(0, 45))
        self.btn_tools.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_tools.setStyleSheet(u"background-image: url(:/icons/images/icons/Tools.png);")

        self.verticalLayout_8.addWidget(self.btn_tools)

        self.btn_law = QPushButton(self.topMenu)
        self.btn_law.setObjectName(u"btn_law")
        sizePolicy.setHeightForWidth(self.btn_law.sizePolicy().hasHeightForWidth())
        self.btn_law.setSizePolicy(sizePolicy)
        self.btn_law.setMinimumSize(QSize(0, 45))
        self.btn_law.setFont(font)
        self.btn_law.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_law.setLayoutDirection(Qt.LeftToRight)
        self.btn_law.setStyleSheet(u"background-image: url(:/icons/images/icons/law.png);")

        self.verticalLayout_8.addWidget(self.btn_law)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(222, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setBaseSize(QSize(0, 0))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QStackedWidget(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setMinimumSize(QSize(0, 0))
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.extraProduct = QWidget()
        self.extraProduct.setObjectName(u"extraProduct")
        self.verticalLayout_12 = QVBoxLayout(self.extraProduct)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraProduct)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_basic = QPushButton(self.extraTopMenu)
        self.btn_basic.setObjectName(u"btn_basic")
        sizePolicy.setHeightForWidth(self.btn_basic.sizePolicy().hasHeightForWidth())
        self.btn_basic.setSizePolicy(sizePolicy)
        self.btn_basic.setMinimumSize(QSize(0, 45))
        self.btn_basic.setFont(font)
        self.btn_basic.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_basic.setLayoutDirection(Qt.LeftToRight)
        self.btn_basic.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-plus.png);")

        self.verticalLayout_11.addWidget(self.btn_basic)

        self.btn_agreement = QPushButton(self.extraTopMenu)
        self.btn_agreement.setObjectName(u"btn_agreement")
        sizePolicy.setHeightForWidth(self.btn_agreement.sizePolicy().hasHeightForWidth())
        self.btn_agreement.setSizePolicy(sizePolicy)
        self.btn_agreement.setMinimumSize(QSize(0, 45))
        self.btn_agreement.setFont(font)
        self.btn_agreement.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_agreement.setLayoutDirection(Qt.LeftToRight)
        self.btn_agreement.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_agreement)

        self.btn_demand = QPushButton(self.extraTopMenu)
        self.btn_demand.setObjectName(u"btn_demand")
        sizePolicy.setHeightForWidth(self.btn_demand.sizePolicy().hasHeightForWidth())
        self.btn_demand.setSizePolicy(sizePolicy)
        self.btn_demand.setMinimumSize(QSize(0, 45))
        self.btn_demand.setFont(font)
        self.btn_demand.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_demand.setLayoutDirection(Qt.LeftToRight)
        self.btn_demand.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-zoom-in.png);")

        self.verticalLayout_11.addWidget(self.btn_demand)

        self.btn_file = QPushButton(self.extraTopMenu)
        self.btn_file.setObjectName(u"btn_file")
        sizePolicy.setHeightForWidth(self.btn_file.sizePolicy().hasHeightForWidth())
        self.btn_file.setSizePolicy(sizePolicy)
        self.btn_file.setMinimumSize(QSize(0, 45))

        self.verticalLayout_11.addWidget(self.btn_file)

        self.btn_buyNotice = QPushButton(self.extraTopMenu)
        self.btn_buyNotice.setObjectName(u"btn_buyNotice")
        sizePolicy.setHeightForWidth(self.btn_buyNotice.sizePolicy().hasHeightForWidth())
        self.btn_buyNotice.setSizePolicy(sizePolicy)
        self.btn_buyNotice.setMinimumSize(QSize(0, 45))
        self.btn_buyNotice.setBaseSize(QSize(0, 45))

        self.verticalLayout_11.addWidget(self.btn_buyNotice)

        self.btn_enroll = QPushButton(self.extraTopMenu)
        self.btn_enroll.setObjectName(u"btn_enroll")
        sizePolicy.setHeightForWidth(self.btn_enroll.sizePolicy().hasHeightForWidth())
        self.btn_enroll.setSizePolicy(sizePolicy)
        self.btn_enroll.setMinimumSize(QSize(0, 45))

        self.verticalLayout_11.addWidget(self.btn_enroll)

        self.btn_ready = QPushButton(self.extraTopMenu)
        self.btn_ready.setObjectName(u"btn_ready")
        sizePolicy.setHeightForWidth(self.btn_ready.sizePolicy().hasHeightForWidth())
        self.btn_ready.setSizePolicy(sizePolicy)
        self.btn_ready.setMinimumSize(QSize(0, 45))

        self.verticalLayout_11.addWidget(self.btn_ready)

        self.btn_bidOpen = QPushButton(self.extraTopMenu)
        self.btn_bidOpen.setObjectName(u"btn_bidOpen")
        sizePolicy.setHeightForWidth(self.btn_bidOpen.sizePolicy().hasHeightForWidth())
        self.btn_bidOpen.setSizePolicy(sizePolicy)
        self.btn_bidOpen.setMinimumSize(QSize(0, 45))
        self.btn_bidOpen.setSizeIncrement(QSize(0, 0))
        self.btn_bidOpen.setBaseSize(QSize(0, 0))

        self.verticalLayout_11.addWidget(self.btn_bidOpen)

        self.btn_productResult = QPushButton(self.extraTopMenu)
        self.btn_productResult.setObjectName(u"btn_productResult")
        sizePolicy.setHeightForWidth(self.btn_productResult.sizePolicy().hasHeightForWidth())
        self.btn_productResult.setSizePolicy(sizePolicy)
        self.btn_productResult.setMinimumSize(QSize(0, 45))

        self.verticalLayout_11.addWidget(self.btn_productResult)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraProduct)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")

        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraProduct)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)

        self.extraContent.addWidget(self.extraProduct)
        self.extraOpen = QWidget()
        self.extraOpen.setObjectName(u"extraOpen")
        self.extraTopMenu_2 = QFrame(self.extraOpen)
        self.extraTopMenu_2.setObjectName(u"extraTopMenu_2")
        self.extraTopMenu_2.setGeometry(QRect(0, 0, 221, 281))
        self.extraTopMenu_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.extraTopMenu_2.setMouseTracking(True)
        self.extraTopMenu_2.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.extraTopMenu_2)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.btn_openbasic = QPushButton(self.extraTopMenu_2)
        self.btn_openbasic.setObjectName(u"btn_openbasic")
        sizePolicy.setHeightForWidth(self.btn_openbasic.sizePolicy().hasHeightForWidth())
        self.btn_openbasic.setSizePolicy(sizePolicy)
        self.btn_openbasic.setMinimumSize(QSize(0, 45))
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.btn_openbasic.setPalette(palette)
        self.btn_openbasic.setFont(font)
        self.btn_openbasic.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_openbasic.setLayoutDirection(Qt.LeftToRight)
        self.btn_openbasic.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-plus.png);")

        self.verticalLayout_16.addWidget(self.btn_openbasic)

        self.btn_openLocal = QPushButton(self.extraTopMenu_2)
        self.btn_openLocal.setObjectName(u"btn_openLocal")
        sizePolicy.setHeightForWidth(self.btn_openLocal.sizePolicy().hasHeightForWidth())
        self.btn_openLocal.setSizePolicy(sizePolicy)
        self.btn_openLocal.setMinimumSize(QSize(0, 45))
        self.btn_openLocal.setFont(font)
        self.btn_openLocal.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_openLocal.setMouseTracking(True)
        self.btn_openLocal.setLayoutDirection(Qt.LeftToRight)
        self.btn_openLocal.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_16.addWidget(self.btn_openLocal)

        self.btn_openCheck = QPushButton(self.extraTopMenu_2)
        self.btn_openCheck.setObjectName(u"btn_openCheck")
        sizePolicy.setHeightForWidth(self.btn_openCheck.sizePolicy().hasHeightForWidth())
        self.btn_openCheck.setSizePolicy(sizePolicy)
        self.btn_openCheck.setMinimumSize(QSize(0, 45))
        self.btn_openCheck.setFont(font)
        self.btn_openCheck.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_openCheck.setLayoutDirection(Qt.LeftToRight)
        self.btn_openCheck.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-zoom-in.png);")

        self.verticalLayout_16.addWidget(self.btn_openCheck)

        self.btn_openfit = QPushButton(self.extraTopMenu_2)
        self.btn_openfit.setObjectName(u"btn_openfit")
        sizePolicy.setHeightForWidth(self.btn_openfit.sizePolicy().hasHeightForWidth())
        self.btn_openfit.setSizePolicy(sizePolicy)
        self.btn_openfit.setMinimumSize(QSize(0, 45))

        self.verticalLayout_16.addWidget(self.btn_openfit)

        self.btn_openScore = QPushButton(self.extraTopMenu_2)
        self.btn_openScore.setObjectName(u"btn_openScore")
        sizePolicy.setHeightForWidth(self.btn_openScore.sizePolicy().hasHeightForWidth())
        self.btn_openScore.setSizePolicy(sizePolicy)
        self.btn_openScore.setMinimumSize(QSize(0, 45))
        self.btn_openScore.setBaseSize(QSize(0, 45))

        self.verticalLayout_16.addWidget(self.btn_openScore)

        self.btn_openResult = QPushButton(self.extraTopMenu_2)
        self.btn_openResult.setObjectName(u"btn_openResult")
        sizePolicy.setHeightForWidth(self.btn_openResult.sizePolicy().hasHeightForWidth())
        self.btn_openResult.setSizePolicy(sizePolicy)
        self.btn_openResult.setMinimumSize(QSize(0, 45))

        self.verticalLayout_16.addWidget(self.btn_openResult)

        self.extraContent.addWidget(self.extraOpen)
        self.extraRecord = QWidget()
        self.extraRecord.setObjectName(u"extraRecord")
        self.extraTopMenu_3 = QFrame(self.extraRecord)
        self.extraTopMenu_3.setObjectName(u"extraTopMenu_3")
        self.extraTopMenu_3.setGeometry(QRect(0, 0, 221, 101))
        self.extraTopMenu_3.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.extraTopMenu_3)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.btn_recordBasic = QPushButton(self.extraTopMenu_3)
        self.btn_recordBasic.setObjectName(u"btn_recordBasic")
        sizePolicy.setHeightForWidth(self.btn_recordBasic.sizePolicy().hasHeightForWidth())
        self.btn_recordBasic.setSizePolicy(sizePolicy)
        self.btn_recordBasic.setMinimumSize(QSize(0, 45))
        self.btn_recordBasic.setFont(font)
        self.btn_recordBasic.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_recordBasic.setLayoutDirection(Qt.LeftToRight)
        self.btn_recordBasic.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-plus.png);")

        self.verticalLayout_22.addWidget(self.btn_recordBasic)

        self.btn_recordSituation = QPushButton(self.extraTopMenu_3)
        self.btn_recordSituation.setObjectName(u"btn_recordSituation")
        sizePolicy.setHeightForWidth(self.btn_recordSituation.sizePolicy().hasHeightForWidth())
        self.btn_recordSituation.setSizePolicy(sizePolicy)
        self.btn_recordSituation.setMinimumSize(QSize(0, 45))
        self.btn_recordSituation.setFont(font)
        self.btn_recordSituation.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_recordSituation.setLayoutDirection(Qt.LeftToRight)
        self.btn_recordSituation.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_22.addWidget(self.btn_recordSituation)

        self.extraContent.addWidget(self.extraRecord)

        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"background-image: url(:/images/images/images/logoBig.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.stackedWidget.addWidget(self.home)
        self.init = QWidget()
        self.init.setObjectName(u"init")
        self.verticalLayout = QVBoxLayout(self.init)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 0)
        self.label_17 = QLabel(self.init)
        self.label_17.setObjectName(u"label_17")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.label_17)

        self.frame = QFrame(self.init)
        self.frame.setObjectName(u"frame")
        sizePolicy3.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy3)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout.setContentsMargins(-1, -1, -1, 0)
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_7)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_8)

        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_9)

        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_3)

        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_11)

        self.lineEdit_8 = QLineEdit(self.frame)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit_8)

        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_10)

        self.lineEdit_4 = QLineEdit(self.frame)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEdit_4)

        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_12)

        self.lineEdit_7 = QLineEdit(self.frame)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lineEdit_7)

        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_13)

        self.lineEdit_5 = QLineEdit(self.frame)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.lineEdit_5)

        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_14)

        self.lineEdit_6 = QLineEdit(self.frame)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.lineEdit_6)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.init)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy3.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy3)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(9, 0, -1, -1)
        self.groupBox = QGroupBox(self.frame_2)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.radioButton_5 = QRadioButton(self.groupBox)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.horizontalLayout_6.addWidget(self.radioButton_5)

        self.radioButton_4 = QRadioButton(self.groupBox)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.horizontalLayout_6.addWidget(self.radioButton_4)


        self.gridLayout.addWidget(self.groupBox, 6, 0, 1, 2)

        self.radioButton_3 = QRadioButton(self.frame_2)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.gridLayout.addWidget(self.radioButton_3, 1, 3, 1, 1)

        self.comboBox_2 = QComboBox(self.frame_2)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout.addWidget(self.comboBox_2, 8, 1, 1, 1)

        self.label_15 = QLabel(self.frame_2)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 5, 0, 1, 1)

        self.label_20 = QLabel(self.frame_2)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout.addWidget(self.label_20, 8, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.frame_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.radioButton_6 = QRadioButton(self.groupBox_2)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.horizontalLayout_7.addWidget(self.radioButton_6)

        self.radioButton_7 = QRadioButton(self.groupBox_2)
        self.radioButton_7.setObjectName(u"radioButton_7")

        self.horizontalLayout_7.addWidget(self.radioButton_7)


        self.gridLayout.addWidget(self.groupBox_2, 6, 2, 1, 2)

        self.label_16 = QLabel(self.frame_2)
        self.label_16.setObjectName(u"label_16")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.label_16, 1, 0, 1, 1)

        self.radioButton = QRadioButton(self.frame_2)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout.addWidget(self.radioButton, 1, 1, 1, 1)

        self.radioButton_2 = QRadioButton(self.frame_2)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout.addWidget(self.radioButton_2, 1, 2, 1, 1)

        self.comboBox = QComboBox(self.frame_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEditable(False)

        self.gridLayout.addWidget(self.comboBox, 5, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.pushButton = QPushButton(self.init)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 45))
        self.pushButton.setStyleSheet(u"background-color: rgb(181, 152, 255);")

        self.verticalLayout.addWidget(self.pushButton)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 4)
        self.verticalLayout.setStretch(2, 1)
        self.stackedWidget.addWidget(self.init)
        self.biddingflow = QWidget()
        self.biddingflow.setObjectName(u"biddingflow")
        self.verticalLayout_20 = QVBoxLayout(self.biddingflow)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label = QLabel(self.biddingflow)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label)

        self.stackedWidget.addWidget(self.biddingflow)
        self.record = QWidget()
        self.record.setObjectName(u"record")
        self.label_2 = QLabel(self.record)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(290, 80, 53, 16))
        self.stackedWidget.addWidget(self.record)
        self.tools = QWidget()
        self.tools.setObjectName(u"tools")
        self.label_3 = QLabel(self.tools)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(330, 160, 53, 16))
        self.stackedWidget.addWidget(self.tools)
        self.money = QWidget()
        self.money.setObjectName(u"money")
        self.label_4 = QLabel(self.money)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(250, 120, 53, 16))
        self.stackedWidget.addWidget(self.money)
        self.law = QWidget()
        self.law.setObjectName(u"law")
        self.verticalLayout_21 = QVBoxLayout(self.law)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.tableWidget = QTableWidget(self.law)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_21.addWidget(self.tableWidget)

        self.label_5 = QLabel(self.law)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_21.addWidget(self.label_5)

        self.stackedWidget.addWidget(self.law)
        self.editProduct = QWidget()
        self.editProduct.setObjectName(u"editProduct")
        self.frame_3 = QFrame(self.editProduct)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(29, 90, 601, 141))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_4 = QFrame(self.editProduct)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(270, 320, 120, 80))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.editProduct)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(200, 40, 53, 16))
        self.stackedWidget.addWidget(self.editProduct)
        self.basicsearch = QWidget()
        self.basicsearch.setObjectName(u"basicsearch")
        self.searchFrame = QFrame(self.basicsearch)
        self.searchFrame.setObjectName(u"searchFrame")
        self.searchFrame.setGeometry(QRect(-1, 100, 661, 211))
        self.searchFrame.setFrameShape(QFrame.StyledPanel)
        self.searchFrame.setFrameShadow(QFrame.Raised)
        self.productList = QFrame(self.basicsearch)
        self.productList.setObjectName(u"productList")
        self.productList.setGeometry(QRect(9, 319, 631, 431))
        self.productList.setFrameShape(QFrame.StyledPanel)
        self.productList.setFrameShadow(QFrame.Raised)
        self.label_18 = QLabel(self.basicsearch)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(20, 30, 91, 16))
        self.stackedWidget.addWidget(self.basicsearch)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(222, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setStyleSheet(u"")
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QStackedWidget(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setStyleSheet(u"")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.contentSettingsPage1 = QWidget()
        self.contentSettingsPage1.setObjectName(u"contentSettingsPage1")
        self.verticalLayout_13 = QVBoxLayout(self.contentSettingsPage1)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettingsPage1)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_13.addWidget(self.topMenus)

        self.contentSettings.addWidget(self.contentSettingsPage1)
        self.contentSettingsPage2 = QWidget()
        self.contentSettingsPage2.setObjectName(u"contentSettingsPage2")
        self.contentSettings.addWidget(self.contentSettingsPage2)

        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font4 = QFont()
        font4.setBold(False)
        font4.setItalic(False)
        self.creditsLabel.setFont(font4)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.verticalLayout_19.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.extraContent.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(8)
        self.comboBox.setCurrentIndex(0)
        self.contentSettings.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"\u6d69\u884c\u62db\u6807", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"\u5168\u6d41\u7a0b\u62db\u6807\u7ba1\u7406\u7cfb\u7edf", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u9875", None))
        self.btn_init.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210\u9879\u76ee", None))
        self.btn_product.setText(QCoreApplication.translate("MainWindow", u"\u9879\u76ee\u7ba1\u7406", None))
        self.btn_biddingflow.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u6807\u6d41\u7a0b", None))
        self.btn_record.setText(QCoreApplication.translate("MainWindow", u"\u5907\u6848\u6d41\u7a0b", None))
        self.btn_tools.setText(QCoreApplication.translate("MainWindow", u"\u5de5\u5177\u5408\u96c6", None))
        self.btn_law.setText(QCoreApplication.translate("MainWindow", u"\u6cd5\u5f8b\u6cd5\u89c4", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"\u529f\u80fd", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_basic.setText(QCoreApplication.translate("MainWindow", u"\u57fa\u672c\u4fe1\u606f", None))
        self.btn_agreement.setText(QCoreApplication.translate("MainWindow", u"\u4ee3\u7406\u534f\u8bae", None))
        self.btn_demand.setText(QCoreApplication.translate("MainWindow", u"\u9700\u6c42\u8bba\u8bc1", None))
        self.btn_file.setText(QCoreApplication.translate("MainWindow", u"\u91c7\u8d2d\u6587\u4ef6", None))
        self.btn_buyNotice.setText(QCoreApplication.translate("MainWindow", u"\u91c7\u8d2d\u76f8\u5173\u516c\u544a", None))
        self.btn_enroll.setText(QCoreApplication.translate("MainWindow", u"\u62a5\u540d\u60c5\u51b5", None))
        self.btn_ready.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u6807\u524d\u51c6\u5907", None))
        self.btn_bidOpen.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u6807\u60c5\u51b5", None))
        self.btn_productResult.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u6807\u7ed3\u679c", None))
        self.btn_openbasic.setText(QCoreApplication.translate("MainWindow", u"\u57fa\u672c\u4fe1\u606f", None))
        self.btn_openLocal.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u6807\u73b0\u573a", None))
        self.btn_openCheck.setText(QCoreApplication.translate("MainWindow", u"\u8d44\u683c\u5ba1\u67e5", None))
        self.btn_openfit.setText(QCoreApplication.translate("MainWindow", u"\u7b26\u5408\u6027\u5ba1\u67e5", None))
        self.btn_openScore.setText(QCoreApplication.translate("MainWindow", u"\u8bc4\u5206", None))
        self.btn_openResult.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u679c", None))
        self.btn_recordBasic.setText(QCoreApplication.translate("MainWindow", u"\u57fa\u672c\u4fe1\u606f", None))
        self.btn_recordSituation.setText(QCoreApplication.translate("MainWindow", u"\u79fb\u4ea4\u60c5\u51b5", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"\u6d69\u884c\u62db\u6807--\u6d4b\u8bd5\u9636\u6bb5", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210\u9879\u76ee", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u9879\u76ee\u8d1f\u8d23\u4eba\uff1a", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5982\u6302\u9760\uff0c\u9879\u76ee\u8d1f\u8d23\u4eba\u4e3a\u5b9e\u9645\u8d1f\u8d23\u4eba", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u9879\u76ee\u7ecf\u7406\uff1a", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u91c7\u8d2d\u5355\u4f4d\u540d\u79f0\uff1a", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u91c7\u8d2d\u4eba\u5730\u5740\uff1a", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u91c7\u8d2d\u4eba\u8054\u7cfb\u4eba\uff1a", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u91c7\u8d2d\u4eba\u8054\u7cfb\u65b9\u5f0f\uff1a", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u9879\u76ee\u540d\u79f0\uff1a", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u9884\u7b97\u91d1\u989d\uff08\u4e07\u5143\uff09\uff1a", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u9762\u5411\u4e2d\u5c0f\u4f01\u4e1a\uff1a", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"\u662f", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"\u5426", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"\u5de5\u7a0b", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"\u56db\u5ddd\u653f\u5e9c\u91c7\u8d2d\u7f51", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u4e2d\u56fd\u653f\u5e9c\u91c7\u8d2d\u7f51", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"\u4e2d\u56fd\u62db\u6807\u6295\u6807\u516c\u5171\u670d\u52a1\u5e73\u53f0", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"\u91c7\u8d2d\u4e0e\u62db\u6807\u7f51", None))

        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u9879\u76ee\u91c7\u8d2d\u65b9\u5f0f\uff1a", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u6302\u7f51\u7f51\u5740\uff1a", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u9700\u8981\u9700\u6c42\u8bba\u8bc1\uff1a", None))
        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"\u662f", None))
        self.radioButton_7.setText(QCoreApplication.translate("MainWindow", u"\u5426", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u9879\u76ee\u7c7b\u578b\uff1a", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u670d\u52a1", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u8d27\u7269", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u7ade\u4e89\u6027\u78cb\u5546", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u516c\u5f00\u62db\u6807", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u7ade\u4e89\u6027\u8c08\u5224", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u8be2\u4ef7", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"\u6bd4\u9009", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"\u5355\u4e00\u6765\u6e90", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"\u5c65\u7ea6\u9a8c\u6536", None))

        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210\u9879\u76ee", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u6807\u6d41\u7a0b", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5907\u6848\u6d41\u7a0b", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5de5\u5177\u9875", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u8d22\u52a1", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u6cd5\u89c4", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u9009\u62e9\u9879\u76ee", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: figro ZP", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"V0.0.2", None))
    # retranslateUi

