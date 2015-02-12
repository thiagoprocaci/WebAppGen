# -*- coding: utf-8 -*-
from IOhandler import *
import os

class Structure:
    project = None
    generationFolderDest = None
    rootFolder = None
    mainWebInfFolder = None
    mainWebappFolder = None

    def __init__(self, project, generationFolderDest):
        self.project = project
        self.generationFolderDest = generationFolderDest
        self.rootFolder = None
        self.mainWebInfFolder = None
        self.mainWebappFolder = None


    def generate(self):
        self.generateStructure()
        self.generatePom()  
        self.generateWebXml()   
        self.generateIndex()

    def generateIndex(self):
        indexTemplatePath = '../' + os.sep + 'resources' + os.sep + 'indexTemplate.jsp'        
        indexTemplate = FileHandler.readFile(indexTemplatePath)      

        indexPath = self.mainWebappFolder + os.sep + 'index.jsp'         
        FileHandler.writeContent(indexTemplate, indexPath)
    
    def generateWebXml(self):
        webXmlTemplatePath = '../' + os.sep + 'resources' + os.sep + 'webTemplate.xml'        
        webTemplate = FileHandler.readFile(webXmlTemplatePath)
        web = webTemplate.replace('#PROJECT_NAME#', self.project.name)

        webPath = self.mainWebInfFolder + os.sep + 'web.xml'         
        FileHandler.writeContent(web, webPath)


    def generatePom(self):
        pomTemplatePath = '../' + os.sep + 'resources' + os.sep + 'pomTemplate.xml'        
        pomTemplate = FileHandler.readFile(pomTemplatePath)
        pom = pomTemplate.replace('#GROUP_NAME#', self.project.group)
        pom = pom.replace('#PROJECT_NAME#', self.project.name)

        pomPath = self.rootFolder + os.sep + 'pom.xml'         
        FileHandler.writeContent(pom, pomPath)
        


    def generateStructure(self):

        FileHandler.deleteFolder(self.generationFolderDest)        
        self.rootFolder = FileHandler.createFolder(self.generationFolderDest, self.project.name)
        
        srcFolder = FileHandler.createFolder(self.rootFolder, 'src')        
        mainFolder = FileHandler.createFolder(srcFolder, 'main')
        mainConfigFolder = FileHandler.createFolder(mainFolder, 'config')
        mainJavaFolder = FileHandler.createFolder(mainFolder, 'java')
        mainResourceFolder = FileHandler.createFolder(mainFolder, 'resources')
        self.mainWebappFolder = FileHandler.createFolder(mainFolder, 'webapp')
        mainMetaInfFolder = FileHandler.createFolder(self.mainWebappFolder, 'META-INF')
        self.mainWebInfFolder = FileHandler.createFolder(self.mainWebappFolder, 'WEB-INF')

        testFolder = FileHandler.createFolder(srcFolder, 'test')        
        testJavaFolder = FileHandler.createFolder(testFolder, 'java')
        testResourceFolder = FileHandler.createFolder(testFolder, 'resources')

        currentMainPackage = mainJavaFolder
        currentTestPackage = testJavaFolder
        for packageName in self.project.group.split('.'):
            currentMainPackage = FileHandler.createFolder(currentMainPackage, packageName)        
            currentTestPackage = FileHandler.createFolder(currentTestPackage, packageName)   

        







        



