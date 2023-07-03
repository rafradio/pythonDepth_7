import os
from pathlib import Path
import shutil


class DirsAndFiles:
    def __init__(self, ext):
        self.fileExt = '.' + str(ext)
        self.MAINDIR = os.getcwd()
        self.DIRNAME = 'seconddir'
        self.dirLib = [(dir_path, dir_name) for dir_path, dir_name, _ in os.walk(os.getcwd())]

    def createSecondDir(self):
        checkSecondDir = list(filter(lambda x: x[0] == self.MAINDIR and self.DIRNAME in x[1], self.dirLib))
        if len(checkSecondDir) == 0: 
            os.mkdir(self.DIRNAME)
        else:
            shutil.rmtree(self.DIRNAME)
            os.mkdir(self.DIRNAME)


    def copyDirs(self, dirName):
        dirName = os.path.join(os.getcwd(), dirName)
        print(dirName)
        dir_tupple = list(os.walk(dirName))[0]
        if len(dir_tupple[1]) > 0:
            for d in dir_tupple[1]:
                dirName = dir_tupple[0] + '\\' + d
                xx = dirName.replace("firstdir", self.DIRNAME)
                os.mkdir(xx)
                self.copyDirs(dirName)

        if len(dir_tupple[2]) > 0:
            for f in dir_tupple[2]:
                if os.path.splitext(f)[1] == self.fileExt:
                    oldFile = os.path.join(dir_tupple[0], f)
                    newDir = os.path.join(dir_tupple[0].replace("firstdir", self.DIRNAME), f)
                    shutil.copy(oldFile, newDir)



        return
