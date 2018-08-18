# -*- coding: utf-8 -*-

import sys
import os


def getFileName(filePath):
    filename = ""
    dirname = ""
    if os.path.exists(filePath):
        filename = os.path.basename(filePath)
        dirname = os.path.dirname(filePath)
    return filename, dirname

if __name__ == "__main__":
    rootdir = '/Users/liaoyilin/Desktop/tmp/png'
    list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    index=0
    for i in range(0, len(list)):
        path = os.path.join(rootdir, list[i])
        if os.path.isfile(path):
            filename,dirname = getFileName(path)
            if len(filename) > 0:
                #print filename,dirname
                index+=1
                newname = '%s/%s.png' % (dirname,str(index))
                print path,newname
                os.rename(path,newname)


