import csv
import pandas as pd
import numpy as np
import os
""" 
*    Two major classes are needed
*    1. for reading in mass
*    2. for writing in mass
*    3. for reading specific line
*    4. writing to the specific line
"""
"""
Global declarations for handling the filepaths
and do edit path variables if and when needed for changes

**************************
* incase if you are getting path not found variables please change the paths in read file functions *
* this is the only place where things could go wrong as there is a high chance of path mismatches as we hardcoded the paths *
* in next version this will be corrected
"""


class readFile:
    """
    The planned functions are:
    # 1. readFile(): just to read the content and store it into a data variable only meant for cases where we don't need returning output
    # 2. printPath(): this is a debug function to deal with fileNotFound exceptions incase they occur
    # 3. printFileContent(): prints all the content of the read csvFile
    # 4. returnFirstLine(): returns the first line of the csv
    # 5. returnLastLint(): returns the last line of the csv
    """
    """
    
    # class level scope declerations are:
    # 1. path
    # 2. data
    # 3. fileName

    """
    path = " "
    data = " "
    fileName = " "
    
    def __init__(self,filename):
        self.fileName = filename
        cwd = os.getcwd()
        cwd = cwd+f"\handling_csv\\"+filename
        self.path = cwd
    
    def readFile(self):
        df = pd.read_csv(self.path)
        self.data = df

    def returnPath(self):
        print(self.path)

    def returnFileName(self):
        print(self.fileName)
    
    def returnFileContent(self):
        df = pd.read_csv(self.path)
        self.data = df.values.tolist()
        print(self.data)

    def returnFirstLine(self):
        df = pd.read_csv(self.path)
        self.data = df.values.tolist()
        print(self.data[0])
    
    def returnLastLine(self):
        df = pd.read_csv(self.path)
        self.data = df.values.tolist()
        print(self.data[len(self.data)-1])
        
    

class writeFiles:
    path = " "
    data = " "
    
    def __init__(self,filePath):
        self.path = filePath
    
class readLine:
    path = " "

    def __init__(self,filePath):
        self.path = filePath

