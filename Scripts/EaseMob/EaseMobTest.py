# -*- coding: utf-8 -*-
import datetime
import json
from time import sleep
from qiniu import Auth, put_file, etag
from EaseMobHelper import *
import re

def outputFunction(val):
    print(val)

if __name__ == '__main__':
    print ''
    interval = 1
    fnc = outputFunction
    # self.target = 1000686
    # self.idstart = 1000671
    # self.idend = 1001193
    helper = EaseMobHelper(fnc,1000686,1000671,1001193)
    baseclass = BaseClass()
    helper.mainMethod()
