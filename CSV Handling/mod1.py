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
    path = " "
    data = " "
    fileName = ""
    def __init__(self,filename):
        self.fileName = filename
        cwd = os.getcwd()
        cwd = cwd+f"\pythaan\handling_csv\\"+filename
        self.path = cwd
    
    def readFile(self):
      df = pd.read_csv(self.path)
      self.data = df

    def printPath(self):
        print(self.path)
        print(self.fileName)
    
    def printFileContent(self):
        df = pd.read_csv(self.path)
        self.data = df
        print(self.data)
    

class writeFiles:
    path = " "
    data = " "
    
    def __init__(self,filePath):
        self.path = filePath
    
class readLine:
    path = " "

    def __init__(self,filePath):
        self.path = filePath

