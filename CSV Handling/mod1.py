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
    # 2. returnPath(): this is a debug function to deal with fileNotFound exceptions incase they occur
    # 3. returnFileName(): returns file name useful while debugging
    # 4. returnFileContent(): prints all the content of the read csvFile
    # 5. returnColumns(): returns a list of columns in csv
    # 6. returnFirstLine(): returns the first line of the csv
    # 7. returnLastLine(): returns the last line of the csv 
    """
    """
    
    # class level scope declerations are:
    # 1. path
    # 2. data
    # 3. fileName
    # 4. Columns in CSV

    """
    path = " "
    data = []
    fileName = " "
    columns = []
    def __init__(self,filename):
        self.fileName = filename
        cwd = os.getcwd()
        cwd = cwd+f"\handling_csv\\"+filename
        self.path = cwd
    
    def readFile(self):
        df = pd.read_csv(self.path)
        self.data = df.values.tolist()

    def returnPath(self):
        print(self.path)

    def returnFileName(self):
        print(self.fileName)
    
    def returnFileContent(self):
        self.readFile()
        print(self.data)

    def returnColumns(self):
        df = pd.read_csv(self.path)
        self.columns = df.columns.tolist()
        

    def returnFirstLine(self):
        self.readFile()
        print(self.data[0])
    
    def returnLastLine(self):
        self.readFile()
        print(self.data[len(self.data)-1])
        
        
    

class writeToFile:
     """
    The planned functions are:
    # 1. readFile(): just to read the content and store it into a data variable only meant for cases where we don't need returning output
    # 2. returnPath(): this is a debug function to deal with fileNotFound exceptions incase they occur
    # 3. returnFileName(): returns file name useful while debugging
    # 5. returnColumns(): returns a list of columns in csv
    # 6. buildNewLineDict(): for building new line dictionary with the passed values to update the csv
    # 7. writeLine(): for adding new line into the csv
    """
    """
    # class level scope declerations are:
    # 1. path
    # 2. data
    # 3. fileName
    # 4. Columns in CSV
    # 5. dictionary for new line entry
    # 6. new line for first reading line from user
            
    """

    fileName = " "
    path = " "
    data = " "
    newLine = " "
    newlineDict = {}
    col = [] #for columns list
    
    def __init__(self,filename):
        self.fileName = filename
        cwd = os.getcwd()
        cwd = cwd+f"\handling_csv\\"+filename
        self.path = cwd
    
    def readFile(self):
        df = pd.read_csv(self.path)
        self.data = df.values.tolist()

    def returnPath(self):
        print(self.path)

    def returnFileName(self):
        print(self.fileName)

    def returnColumns(self):
        df = pd.read_csv(self.path)
        self.col = df.columns.tolist()
    
    def buildNewLineDict(self):
        for individual_column,individual_value in zip(self.col,self.newLine):
            self.newlineDict[individual_column] = individual_value
    
    def writeLine(self,line):
        self.newLine = line
        self.readFile()
        self.returnColumns()
        self.buildNewLineDict()
        df1 = pd.read_csv(self.path)
        df1.loc[len(df1)] = self.newlineDict
        df1.to_csv(self.path,index = False)


