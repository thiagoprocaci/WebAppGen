# -*- coding: utf-8 -*-
from IOhandler import *
import os

class Structure:
    project = None
    generationFolderDest = None
    rootFolder = None
    srcFolder = None
    mainFolder = None
    mainJavaFolder = None
    mainConfigFolder = None
    mainWebInfFolder = None
    mainWebappFolder = None
    mainResourceFolder = None
    mainMetaInfFolder = None
    testFolder = None
    testJavaFolder = None
    testResourceFolder = None
    mainResourceMetaInfFolder = None
    mainResourceSpringFolder = None
    serviceMainFolder = None
    serviceTestFolder = None
    presentationMainFolder = None
    presentationTestFolder = None
    modelMainFolder = None
    modelTestFolder = None
    persistenceMainFolder = None
    persistenceTestFolder = None
    viewsFolder = None
    customerFolder = None

    def __init__(self, project, generationFolderDest):
        self.project = project
        self.generationFolderDest = generationFolderDest
        self.rootFolder = None
        self.srcFolder = None
        self.mainFolder = None
        self.mainJavaFolder = None
        self.mainConfigFolder = None
        self.mainWebInfFolder = None
        self.mainWebappFolder = None
        self.mainResourceFolder = None
        self.mainMetaInfFolder = None
        self.testFolder = None
        self.testJavaFolder = None
        self.testResourceFolder = None
        self.mainResourceMetaInfFolder = None
        self.mainResourceSpringFolder = None
        self.serviceMainFolder = None
        self.serviceTestFolder = None
        self.presentationMainFolder = None
        self.presentationTestFolder = None
        self.modelMainFolder = None
        self.modelTestFolder = None
        self.persistenceMainFolder = None
        self.persistenceTestFolder = None
        self.viewsFolder = None
        self.customerFolder = None


    def generate(self):
        self.generateStructure()
        self.generatePom()  
        self.generateWebXml()   
        self.generateIndex()
        self.generateConfig()
        self.generateLogback()
        self.generateSpring()
        self.generateTomcatContext()
        self.generateJavaExample()


    def genenateFile(self, templateFileName, fileName, destFolder):
        fileTemplatePath = '../' + os.sep + 'resources' + os.sep + templateFileName        
        fileTemplate = FileHandler.readFile(fileTemplatePath)
        fileApp = fileTemplate.replace('#PROJECT_NAME#', self.project.name)
        fileApp = fileApp.replace('#GROUP_NAME#', self.project.group)

        filePath = destFolder + os.sep + fileName         
        FileHandler.writeContent(fileApp, filePath)

    def generateJavaExample(self):
        self.genenateFile('CustomerTemplate.java', 'Customer.java', self.modelMainFolder) 
        self.genenateFile('CustomerControllerTemplate.java', 'CustomerController.java', self.presentationMainFolder) 
        self.genenateFile('CustomerRepositoryTemplate.java', 'CustomerRepository.java', self.persistenceMainFolder) 
        self.genenateFile('customerListTemplate.jsp', 'customerList.jsp', self.customerFolder) 


    def generateTomcatContext(self):
        self.genenateFile('contextTemplate.xml', 'context.xml', self.mainMetaInfFolder)       

    def generateSpring(self):
        self.genenateFile('applicationTemplate.xml', 'application.xml', self.mainResourceSpringFolder)       
        self.genenateFile('presentationTemplate.xml', 'presentation.xml', self.mainResourceSpringFolder)       

    def generateLogback(self):
        self.genenateFile('logbackTemplate.xml', 'logback.xml', self.mainResourceFolder)       


    def generateConfig(self):
        self.genenateFile('configTemplate.properties', 'config.properties', self.mainConfigFolder)       
        self.genenateFile('logTemplate.properties', 'log.properties', self.mainConfigFolder)

    def generateIndex(self):
        self.genenateFile('indexTemplate.jsp', 'index.jsp', self.mainWebappFolder)
    
    def generateWebXml(self):
        self.genenateFile('webTemplate.xml', 'web.xml', self.mainWebInfFolder)

    def generatePom(self):
        self.genenateFile('pomTemplate.xml', 'pom.xml', self.rootFolder)       


    def generateStructure(self):

        FileHandler.deleteFolder(self.generationFolderDest)        
        self.rootFolder = FileHandler.createFolder(self.generationFolderDest, self.project.name)
        
        self.srcFolder = FileHandler.createFolder(self.rootFolder, 'src')        
        self.mainFolder = FileHandler.createFolder(self.srcFolder, 'main')
        self.mainConfigFolder = FileHandler.createFolder(self.mainFolder, 'config')
        self.mainJavaFolder = FileHandler.createFolder(self.mainFolder, 'java')
        self.mainResourceFolder = FileHandler.createFolder(self.mainFolder, 'resources')
        self.mainResourceMetaInfFolder = FileHandler.createFolder(self.mainResourceFolder, 'META-INF')
        self.mainResourceSpringFolder = FileHandler.createFolder(self.mainResourceMetaInfFolder, 'spring')
        self.mainWebappFolder = FileHandler.createFolder(self.mainFolder, 'webapp')
        self.mainMetaInfFolder = FileHandler.createFolder(self.mainWebappFolder, 'META-INF')
        self.mainWebInfFolder = FileHandler.createFolder(self.mainWebappFolder, 'WEB-INF')
        self.viewsFolder = FileHandler.createFolder(self.mainWebInfFolder, 'views')
        self.customerFolder = FileHandler.createFolder(self.viewsFolder, 'customer')

        self.testFolder = FileHandler.createFolder(self.srcFolder, 'test')        
        self.testJavaFolder = FileHandler.createFolder(self.testFolder, 'java')
        self.testResourceFolder = FileHandler.createFolder(self.testFolder, 'resources')

        currentMainPackage = self.mainJavaFolder
        currentTestPackage = self.testJavaFolder
        for packageName in self.project.group.split('.'):
            currentMainPackage = FileHandler.createFolder(currentMainPackage, packageName)        
            currentTestPackage = FileHandler.createFolder(currentTestPackage, packageName)   

        self.serviceMainFolder = FileHandler.createFolder(currentMainPackage, 'service')
        self.serviceTestFolder = FileHandler.createFolder(currentTestPackage, 'service')
        self.presentationMainFolder = FileHandler.createFolder(currentMainPackage, 'presentation')
        self.presentationTestFolder = FileHandler.createFolder(currentTestPackage, 'presentation')
        self.modelMainFolder = FileHandler.createFolder(currentMainPackage, 'model')
        self.modelTestFolder = FileHandler.createFolder(currentTestPackage, 'model')
        self.persistenceMainFolder = FileHandler.createFolder(currentMainPackage, 'persistence')
        self.persistenceTestFolder = FileHandler.createFolder(currentTestPackage, 'persistence')


        







        



