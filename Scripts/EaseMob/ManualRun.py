# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from easemob_main import *
import datetime
import time
import re
from EaseMobHelper import *
from BatchExecuteHelper import *
from MultiInterfaceSeqExecuteHelper import *

reload(sys)
sys.setdefaultencoding('utf8')


class BigWorkThread(QtCore.QThread):
    """docstring for BigWorkThread"""
    #声明一个信号，同时返回一个list，同理什么都能返回啦
    refreshSignal = QtCore.pyqtSignal(list)
    finishSignal = QtCore.pyqtSignal(list)
    #构造函数里增加形参
    def __init__(self, t,s,e,it,parent=None):
        super(BigWorkThread, self).__init__(parent)
        #储存参数
        self.t = t
        self.s = s
        self.e = e
        self.it = it
        self.hhelper = None

    def outputFunction(self, val):
        self.refreshSignal.emit([val])

    def myMethod(self,t,s,e,it):
        fun = self.outputFunction
        self.hhelper = EaseMobHelper(fun,t,s,e,it)
        self.hhelper.mainMethod()

    #重写 run() 函数，在里面干大事。
    def run(self):
        #大事
        self.myMethod(self.t,self.s,self.e,self.it)
        #大事干完了，发送一个信号告诉主线程窗口
        self.finishSignal.emit(['hello,','world','!'])


class BatchExecuteThread(QtCore.QThread):
    """docstring for BigWorkThread"""
    #声明一个信号，同时返回一个list，同理什么都能返回啦
    refreshSignal = QtCore.pyqtSignal(list)
    finishSignal = QtCore.pyqtSignal(list)
    #构造函数里增加形参
    def __init__(self, t,s,e,tn,wn,rd,it,parent=None):
        super(BatchExecuteThread, self).__init__(parent)
        #储存参数
        self.t = t
        self.s = s
        self.e = e
        self.tn = tn
        self.wn = wn
        self.rd = rd
        self.it = it
        self.hhelper=None

    def outputFunction(self, val):
        self.refreshSignal.emit([val])

    def myMethod(self,t,s,e,tn,wn,rd,it):
        fun = self.outputFunction
        self.hhelper = BatchExecuteHelper(fun,t,s,e,tn,wn,rd,it)
        #self.hhelper.mainMethod()
        self.hhelper.multiThreadMethod()

    #重写 run() 函数，在里面干大事。
    def run(self):
        #大事
        self.myMethod(self.t,self.s,self.e,self.tn,self.wn,self.rd,self.it)
        #大事干完了，发送一个信号告诉主线程窗口
        self.finishSignal.emit(['hello,','world','!'])

class MultiInterfaceSeqExecuteThread(QtCore.QThread):
    """docstring for BigWorkThread"""
    #声明一个信号，同时返回一个list，同理什么都能返回啦
    refreshSignal = QtCore.pyqtSignal(list)
    finishSignal = QtCore.pyqtSignal(list)
    #构造函数里增加形参
    def __init__(self, t,s,e,it,parent=None):
        super(MultiInterfaceSeqExecuteThread, self).__init__(parent)
        #储存参数
        self.t = t
        self.s = s
        self.e = e
        self.it = it
        self.hhelper=None

    def outputFunction(self, val):
        self.refreshSignal.emit([val])

    def myMethod(self,t,s,e,it):
        fun = self.outputFunction
        self.hhelper = MultiInterfaceSeqExecuteHelper(fun,t,s,e,it)
        #self.hhelper.mainMethod()
        self.hhelper.multiThreadMethod()

    #重写 run() 函数，在里面干大事。
    def run(self):
        #大事
        self.myMethod(self.t,self.s,self.e,self.it)
        #大事干完了，发送一个信号告诉主线程窗口
        self.finishSignal.emit(['hello,','world','!'])


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.new = Ui_MainWindow()
        self.new.setupUi(self)
        self.pause1 = 0
        self.pause2 = 0
        self.pause3 = 0
        self.stop1 = 0
        self.stop2 = 0
        self.stop3 = 0
        self.bwThread1 = None
        self.bwThread2 = None
        self.bwThread3 = None

    def slot1(self):
        self.pause1=0
        self.stop1=0
        self.new.btnPause.setText("暂停")
        self.BigWork()

    def slot1p(self):
        if self.bwThread1:
            if self.pause1 == 0:
                self.pause1=1
                self.bwThread1.hhelper.pause = 1
                self.new.btnPause.setText("继续")
            else:
                self.pause1 = 0
                self.bwThread1.hhelper.pause = 0
                self.new.btnPause.setText("暂停")

    def slot1s(self):
        if self.bwThread1:
            self.stop1 = 1
            self.new.btnPause.setText("暂停")
            self.bwThread1.hhelper.stop = 1

    def slot2(self):
        self.pause2 = 0
        self.stop2 = 0
        self.new.btn2Pause.setText("暂停")
        self.BatchWork()

    def slot2p(self):
        if self.bwThread2:
            if self.pause2 == 0:
                self.pause2 = 1
                self.bwThread2.hhelper.pause = 1
                self.new.btn2Pause.setText("继续")
            else:
                self.pause2 = 0
                self.bwThread2.hhelper.pause = 0
                self.new.btn2Pause.setText("暂停")

    def slot2s(self):
        if self.bwThread2:
            self.stop2 = 1
            self.new.btn2Pause.setText("暂停")
            self.bwThread2.hhelper.stop = 1

    def slot3(self):
        self.pause3 = 0
        self.stop3 = 0
        self.new.btn3Pause.setText("暂停")
        self.MultiInterfaceWork()

    def slot3p(self):
        if self.bwThread3:
            if self.pause3 == 0:
                self.pause3 = 1
                self.bwThread3.hhelper.pause = 1
                self.new.btn3Pause.setText("继续")
            else:
                self.pause3 = 0
                self.bwThread3.hhelper.pause = 0
                self.new.btn3Pause.setText("暂停")

    def slot3s(self):
        if self.bwThread3:
            self.stop3 = 1
            self.new.btn3Pause.setText("暂停")
            self.bwThread3.hhelper.stop = 1

    def BigWork(self):
        # 把按钮禁用掉
        self.new.btnStart.setDisabled(True)
        # 新建对象，传入参数
        s1 = str(self.new.lineTarget.text())
        s2 = str(self.new.lineStart.text())
        s3 = str(self.new.lineEnd.text())
        s4 = str(self.new.lineSleep.text())

        # 将正则表达式编译成Pattern对象
        pattern = re.compile(r'\d+')
        # 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
        match1 = not pattern.match(s1)
        match2 = not pattern.match(s2)
        match3 = not pattern.match(s3)
        match4 = not pattern.match(s4)

        if match1 or match2 or match3 or match4:
            # 使用Match获得分组信息
            self.new.textEditLog.append("%s" % ('id 需要整型,间隔时间需要整型'))
            self.new.btnStart.setDisabled(False)
        else:
            t = int(s1)
            s = int(s2)
            e = int(s3)
            it = int(s4)
            self.bwThread1 = BigWorkThread(t,s,e,it)
            # 连接子进程的信号和槽函数
            self.bwThread1.refreshSignal.connect(self.BigWorkUpdate1)
            self.bwThread1.finishSignal.connect(self.BigWorkEnd1)
            # 开始执行 run() 函数里的内容refreshSignal
            self.bwThread1.start()

    def BigWorkUpdate1(self, ls):
        val = datetime.datetime.now()
        timestr = val.strftime("%y-%m-%d %H:%M:%S")
        self.new.textEditLog.append("%s %s" % (timestr, ls[0]))

    # 增加形参准备接受返回值 ls
    def BigWorkEnd1(self, ls):
        print '\nget!'
        # 使用传回的返回值
        for word in ls:
            print word,
        # 恢复按钮
        self.new.btnStart.setDisabled(False)
        # QtWidgets.QMessageBox.information(self, "标题", "这是第一个PyQt5 GUI程序")

    def BatchWork(self):
        # 把按钮禁用掉
        self.new.btn2Start.setDisabled(True)
        # 新建对象，传入参数

        s1 = str(self.new.line2URL.text())
        s2 = str(self.new.text2Params.toPlainText())
        s3 = str(self.new.line2Path.text())
        s4 = str(self.new.line2ThreadCount.text())
        s5 = str(self.new.line2LoopCount.text())
        s6 = "0"
        if self.new.cb2IsCallAgain.isChecked():
            s6 = "1"
        else:
            s6 = "0"
        s7 = str(self.new.line2Sleep.text())

        # 将正则表达式编译成Pattern对象
        pattern1 = re.compile(r'^http[s]?://.+$')
        pattern2 = re.compile(r'\d+')
        # 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
        match1 = not pattern1.match(s1)

        match4 = not pattern2.match(s4)
        match5 = not pattern2.match(s5)
        match7 = not pattern2.match(s7)

        if match1:
            # 使用Match获得分组信息
            self.new.text2Log.append("%s" % ('url不对'))
            self.new.btn2Start.setDisabled(False)
        elif match4 or match5 or match7:
            self.new.text2Log.append("%s" % ('线程数,任务数,间隔时间,需要int'))
            self.new.btn2Start.setDisabled(False)
        else:
            if int(s4) >100 or int(s4) < 0:
                self.new.text2Log.append("%s" % ('开启线程数1-100'))
                self.new.btn2Start.setDisabled(False)
            elif int(s5) >100 or int(s5) < 0:
                self.new.text2Log.append("%s" % ('单个任务执行次数1-100'))
                self.new.btn2Start.setDisabled(False)
            else:
                self.bwThread2 = BatchExecuteThread(s1, s2, s3,int(s4),int(s5),int(s6),int(s7))
                # 连接子进程的信号和槽函数
                self.bwThread2.refreshSignal.connect(self.BigWorkUpdate2)
                self.bwThread2.finishSignal.connect(self.BigWorkEnd2)
                # 开始执行 run() 函数里的内容refreshSignal
                self.bwThread2.start()


    def BigWorkUpdate2(self, ls):
        val = datetime.datetime.now()
        timestr = val.strftime("%y-%m-%d %H:%M:%S")
        self.new.text2Log.append("%s %s" % (timestr, ls[0]))

    # 增加形参准备接受返回值 ls
    def BigWorkEnd2(self, ls):
        print '\nget!'
        # 使用传回的返回值
        for word in ls:
            print word,
        # 恢复按钮
        self.new.btn2Start.setDisabled(False)
        # QtWidgets.QMessageBox.information(self, "标题", "这是第一个PyQt5 GUI程序")


    def MultiInterfaceWork(self):
        # 把按钮禁用掉
        self.new.btn3Start.setDisabled(True)
        # 新建对象，传入参数

        s1 = str(self.new.line3URL.text())
        s2 = str(self.new.text3Params.toPlainText())
        s3 = str(self.new.line3Path.text())
        s7 = str(self.new.line3Sleep.text())

        # 将正则表达式编译成Pattern对象
        pattern1 = re.compile(r'^http[s]?://.+$')
        pattern2 = re.compile(r'\d+')
        pattern3 = re.compile(r'^[\w/\\.:]+$')
        # 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
        match1 = not pattern1.match(s1)
        match7 = not pattern2.match(s7)
        match3 = not pattern3.match(s3)

        if match1:
            # 使用Match获得分组信息
            self.new.text3Log.append("%s" % ('url不对'))
            self.new.btn3Start.setDisabled(False)
        elif match3:
            self.new.text3Log.append("%s" % ('批量参数路径不能为空'))
            self.new.btn3Start.setDisabled(False)
        elif match7:
            self.new.text3Log.append("%s" % ('间隔时间,需要int'))
            self.new.btn3Start.setDisabled(False)
        else:
            self.bwThread3 = MultiInterfaceSeqExecuteThread(s1, s2, s3,int(s7))
            # 连接子进程的信号和槽函数
            self.bwThread3.refreshSignal.connect(self.BigWorkUpdate3)
            self.bwThread3.finishSignal.connect(self.BigWorkEnd3)
            # 开始执行 run() 函数里的内容refreshSignal
            self.bwThread3.start()


    def BigWorkUpdate3(self, ls):
        val = datetime.datetime.now()
        timestr = val.strftime("%y-%m-%d %H:%M:%S")
        self.new.text3Log.append("%s %s" % (timestr, ls[0]))

    # 增加形参准备接受返回值 ls
    def BigWorkEnd3(self, ls):
        print '\nget!'
        # 使用传回的返回值
        for word in ls:
            print word,
        # 恢复按钮
        self.new.btn3Start.setDisabled(False)
        # QtWidgets.QMessageBox.information(self, "标题", "这是第一个PyQt5 GUI程序")
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())