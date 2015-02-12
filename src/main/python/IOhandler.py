# -*- coding: utf-8 -*-
import sys
import codecs
import os

class FileHandler:

    @staticmethod
    def createFolder(folder):
        if not os.path.exists(folder):
            os.makedirs(folder)        
        return os.path.exists(folder)


    @staticmethod
    def createFolder(folderParent, folder):
        if not os.path.exists(folderParent):
            os.makedirs(folderParent)
        path = os.path.join(folderParent,folder)
        if not os.path.exists(path):
            os.makedirs(path)
        return path

    @staticmethod
    def deleteFolder(folder):
        for root, dirs, files in os.walk(folder, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        if os.path.exists(folder):
            os.rmdir(folder)

    @staticmethod
    def readFile(filePath):        
        f = codecs.open(filePath, 'r', encoding='utf-8')
        content = f.read()
        return content

    @staticmethod
    def writeContent(content, filePath):
        with codecs.open(filePath, 'w', encoding='utf-8') as f:
            f.write(content)



