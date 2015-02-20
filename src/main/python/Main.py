# -*- coding: utf-8 -*-

from Model import *
from Structure import *
import os


def main():
    projectName = sys.argv[1]
    projectGroup = sys.argv[2]    
    generationFolderDest = '..'+ os.sep + '..' + os.sep + '..' + os.sep + 'generated-app'    

    project = Project(projectName, projectGroup)
    

    structure = Structure(project, generationFolderDest)    
    structure.generate()


if __name__ == '__main__':
    main()