# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'easemob_main.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(871, 635)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineTarget = QtWidgets.QLineEdit(self.tab)
        self.lineTarget.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.lineTarget.setInputMask("")
        self.lineTarget.setText("")
        self.lineTarget.setObjectName("lineTarget")
        self.horizontalLayout.addWidget(self.lineTarget)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineStart = QtWidgets.QLineEdit(self.tab)
        self.lineStart.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.lineStart.setText("")
        self.lineStart.setObjectName("lineStart")
        self.horizontalLayout.addWidget(self.lineStart)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEnd = QtWidgets.QLineEdit(self.tab)
        self.lineEnd.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.lineEnd.setObjectName("lineEnd")
        self.horizontalLayout.addWidget(self.lineEnd)
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout.addWidget(self.label_10)
        self.lineSleep = QtWidgets.QLineEdit(self.tab)
        self.lineSleep.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.lineSleep.setObjectName("lineSleep")
        self.horizontalLayout.addWidget(self.lineSleep)
        self.btnStart = QtWidgets.QPushButton(self.tab)
        self.btnStart.setObjectName("btnStart")
        self.horizontalLayout.addWidget(self.btnStart)
        self.btnPause = QtWidgets.QPushButton(self.tab)
        self.btnPause.setObjectName("btnPause")
        self.horizontalLayout.addWidget(self.btnPause)
        self.btnStop = QtWidgets.QPushButton(self.tab)
        self.btnStop.setObjectName("btnStop")
        self.horizontalLayout.addWidget(self.btnStop)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textEditLog = QtWidgets.QTextEdit(self.tab)
        self.textEditLog.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEditLog.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEditLog.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.textEditLog.setObjectName("textEditLog")
        self.verticalLayout_2.addWidget(self.textEditLog)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 100)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.line2URL = QtWidgets.QLineEdit(self.tab_2)
        self.line2URL.setInputMask("")
        self.line2URL.setText("")
        self.line2URL.setObjectName("line2URL")
        self.horizontalLayout_6.addWidget(self.line2URL)
        self.btn2Start = QtWidgets.QPushButton(self.tab_2)
        self.btn2Start.setObjectName("btn2Start")
        self.horizontalLayout_6.addWidget(self.btn2Start)
        self.btn2Pause = QtWidgets.QPushButton(self.tab_2)
        self.btn2Pause.setObjectName("btn2Pause")
        self.horizontalLayout_6.addWidget(self.btn2Pause)
        self.btn2Stop = QtWidgets.QPushButton(self.tab_2)
        self.btn2Stop.setObjectName("btn2Stop")
        self.horizontalLayout_6.addWidget(self.btn2Stop)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.text2Params = QtWidgets.QTextEdit(self.tab_2)
        self.text2Params.setFrameShadow(QtWidgets.QFrame.Plain)
        self.text2Params.setObjectName("text2Params")
        self.horizontalLayout_5.addWidget(self.text2Params)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.line2Path = QtWidgets.QLineEdit(self.tab_2)
        self.line2Path.setObjectName("line2Path")
        self.horizontalLayout_2.addWidget(self.line2Path)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.line2ThreadCount = QtWidgets.QLineEdit(self.tab_2)
        self.line2ThreadCount.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.line2ThreadCount.setInputMask("")
        self.line2ThreadCount.setObjectName("line2ThreadCount")
        self.horizontalLayout_3.addWidget(self.line2ThreadCount)
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.line2LoopCount = QtWidgets.QLineEdit(self.tab_2)
        self.line2LoopCount.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.line2LoopCount.setObjectName("line2LoopCount")
        self.horizontalLayout_3.addWidget(self.line2LoopCount)
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.line2Sleep = QtWidgets.QLineEdit(self.tab_2)
        self.line2Sleep.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.line2Sleep.setObjectName("line2Sleep")
        self.horizontalLayout_3.addWidget(self.line2Sleep)
        self.cb2IsCallAgain = QtWidgets.QCheckBox(self.tab_2)
        self.cb2IsCallAgain.setObjectName("cb2IsCallAgain")
        self.horizontalLayout_3.addWidget(self.cb2IsCallAgain)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.text2Log = QtWidgets.QTextEdit(self.tab_2)
        self.text2Log.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.text2Log.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.text2Log.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.text2Log.setObjectName("text2Log")
        self.verticalLayout_6.addWidget(self.text2Log)
        self.verticalLayout_5.addLayout(self.verticalLayout_6)
        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 1)
        self.verticalLayout_5.setStretch(2, 1)
        self.verticalLayout_5.setStretch(3, 100)
        self.verticalLayout_7.addLayout(self.verticalLayout_5)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_7.addWidget(self.label_11)
        self.line3URL = QtWidgets.QLineEdit(self.tab_3)
        self.line3URL.setObjectName("line3URL")
        self.horizontalLayout_7.addWidget(self.line3URL)
        self.btn3Start = QtWidgets.QPushButton(self.tab_3)
        self.btn3Start.setObjectName("btn3Start")
        self.horizontalLayout_7.addWidget(self.btn3Start)
        self.btn3Pause = QtWidgets.QPushButton(self.tab_3)
        self.btn3Pause.setObjectName("btn3Pause")
        self.horizontalLayout_7.addWidget(self.btn3Pause)
        self.btn3Stop = QtWidgets.QPushButton(self.tab_3)
        self.btn3Stop.setObjectName("btn3Stop")
        self.horizontalLayout_7.addWidget(self.btn3Stop)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_4.addWidget(self.label_12)
        self.text3Params = QtWidgets.QTextEdit(self.tab_3)
        self.text3Params.setObjectName("text3Params")
        self.horizontalLayout_4.addWidget(self.text3Params)
        self.verticalLayout_8.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_8.addWidget(self.label_13)
        self.line3Path = QtWidgets.QLineEdit(self.tab_3)
        self.line3Path.setObjectName("line3Path")
        self.horizontalLayout_8.addWidget(self.line3Path)
        self.label_14 = QtWidgets.QLabel(self.tab_3)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_8.addWidget(self.label_14)
        self.line3Sleep = QtWidgets.QLineEdit(self.tab_3)
        self.line3Sleep.setObjectName("line3Sleep")
        self.horizontalLayout_8.addWidget(self.line3Sleep)
        self.horizontalLayout_8.setStretch(1, 1)
        self.verticalLayout_8.addLayout(self.horizontalLayout_8)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.text3Log = QtWidgets.QTextEdit(self.tab_3)
        self.text3Log.setObjectName("text3Log")
        self.verticalLayout_10.addWidget(self.text3Log)
        self.verticalLayout_8.addLayout(self.verticalLayout_10)
        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(1, 1)
        self.verticalLayout_8.setStretch(2, 1)
        self.verticalLayout_8.setStretch(3, 100)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)

        self.btn3Start.clicked.connect(MainWindow.slot3)
        self.btn2Start.clicked.connect(MainWindow.slot2)
        self.btnStart.clicked.connect(MainWindow.slot1)

        self.btn3Pause.clicked.connect(MainWindow.slot3p)
        self.btn2Pause.clicked.connect(MainWindow.slot2p)
        self.btnPause.clicked.connect(MainWindow.slot1p)

        self.btn3Stop.clicked.connect(MainWindow.slot3s)
        self.btn2Stop.clicked.connect(MainWindow.slot2s)
        self.btnStop.clicked.connect(MainWindow.slot1s)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "欧加批量测试工具"))
        self.label.setText(_translate("MainWindow", "接收人id"))
        self.lineTarget.setPlaceholderText(_translate("MainWindow", "如1000777"))
        self.label_2.setText(_translate("MainWindow", "发送人id,从"))
        self.lineStart.setPlaceholderText(_translate("MainWindow", "如1000671"))
        self.label_3.setText(_translate("MainWindow", "至"))
        self.lineEnd.setPlaceholderText(_translate("MainWindow", "如1001200"))
        self.label_10.setText(_translate("MainWindow", "间隔时间"))
        self.lineSleep.setText(_translate("MainWindow", "1000"))
        self.lineSleep.setPlaceholderText(_translate("MainWindow", "单位毫秒"))
        self.btnStart.setText(_translate("MainWindow", "开始"))
        self.btnPause.setText(_translate("MainWindow", "暂停"))
        self.btnStop.setText(_translate("MainWindow", "停止"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "批量消息发送"))
        self.label_4.setText(_translate("MainWindow", "调用地址"))
        self.line2URL.setPlaceholderText(_translate("MainWindow", "输入接口名称,如http://ceshi.offerplus.com/offerplus/login.do"))
        self.btn2Start.setText(_translate("MainWindow", "调用"))
        self.btn2Pause.setText(_translate("MainWindow", "暂停"))
        self.btn2Stop.setText(_translate("MainWindow", "停止"))
        self.label_5.setText(_translate("MainWindow", "必传参数"))
        self.text2Params.setPlaceholderText(_translate("MainWindow", "输入必传参数,格式:参数名=参数值,一行对应一组参数,文件类型的参数用paramname(file)=xxx表示,如:offerImage(file)=/Users/liaoyilin/Desktop/timg.jpeg,/Users/liaoyilin/Desktop/timg2.jpeg\""))
        self.label_6.setText(_translate("MainWindow", "批量参数excel文件路径"))
        self.line2Path.setPlaceholderText(_translate("MainWindow", "如/Users/apple/Desktop/data.xlsx excel文件第一行放参数名,第二行开始放参数值,一个参数填一列.文件参数用paramname(file)格式,如offerImage(file)"))
        self.label_7.setText(_translate("MainWindow", "多线程重复执行配置    开启线程数"))
        self.line2ThreadCount.setText(_translate("MainWindow", "1"))
        self.line2ThreadCount.setPlaceholderText(_translate("MainWindow", "1-100"))
        self.label_8.setText(_translate("MainWindow", "单个任务执行次数"))
        self.line2LoopCount.setText(_translate("MainWindow", "1"))
        self.line2LoopCount.setPlaceholderText(_translate("MainWindow", "1-100"))
        self.label_9.setText(_translate("MainWindow", "间隔时间"))
        self.line2Sleep.setText(_translate("MainWindow", "100"))
        self.line2Sleep.setPlaceholderText(_translate("MainWindow", "单位毫秒"))
        self.cb2IsCallAgain.setText(_translate("MainWindow", "执行完成后再次重新执行"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "接口批量调用/压力测试"))
        self.label_11.setText(_translate("MainWindow", "服务器地址"))
        self.line3URL.setPlaceholderText(_translate("MainWindow", "输入服务器地址,如http://ceshi.offerplus.com/offerplus"))
        self.btn3Start.setText(_translate("MainWindow", "调用"))
        self.btn3Pause.setText(_translate("MainWindow", "暂停"))
        self.btn3Stop.setText(_translate("MainWindow", "停止"))
        self.label_12.setText(_translate("MainWindow", "必传参数"))
        self.text3Params.setPlaceholderText(_translate("MainWindow", "输入必传参数,格式:参数名=参数值,一行对应一组参数,文件类型的参数用paramname(file)=xxx表示,如:offerImage(file)=/Users/liaoyilin/Desktop/timg.jpeg,/Users/liaoyilin/Desktop/timg2.jpeg\""))
        self.label_13.setText(_translate("MainWindow", "自动化测试excel文件路径"))
        self.line3Path.setPlaceholderText(_translate("MainWindow", "如/Users/apple/Desktop/data.xlsx excel文件第一行放参数名,第二行开始放参数值,一个参数填一列.文件参数用paramname(file)格式,如offerImage(file)"))
        self.label_14.setText(_translate("MainWindow", "间隔时间"))
        self.line3Sleep.setText(_translate("MainWindow", "100"))
        self.line3Sleep.setPlaceholderText(_translate("MainWindow", "单位毫秒"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "接口自动化测试"))
