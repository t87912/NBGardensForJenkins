# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 11:11:07 2016

@author: Administrator
"""

# Import modules:
import sys
import logging

# Import other python class files:
from Login import Login
from MySQLDatabase import MySQLDatabase
from MongoDatabase import MongoDatabase

class MainLogic(object):
    """ MainLogic: Holds the logic for running the program in the prompt.  """
    def __init__(self):
        self.menuLines = ["\nPlease select an option: ",
                         "1. Query MySQL Database.",
                         "2. Query MongoDB Database.",
                         "9. Quit."]
        self.runProgram()
    
    """
    def startLogging(self):
        self.logger = logging.getLogger('ASAS Log')
        self.logger.setLevel(logging.DEBUG)
        logging.basicConfig(filename = "Logs\\ASAS-Log.log", filemode="a", level = logging.DEBUG, format='%(asctime)s %(message)s')
        self.logger.info('ASAS Program Opened - Logging Started')
    """

    def runProgram(self):  
        """ runProgram: Holds logic for the menu choices. """
        valid = False
        while (not valid):
            print ("Welcome to the NB Gardens Databse Query System!")
            self.printGnome()
            self.printMenu()
            valid = self.getMenuInput()
            if (valid):
                if (self.menuOption == 1):
                    validLogin = False
                    while (not validLogin):
                        userLogin = Login()
                        userLoginDetails = userLogin.getLoginDetails()
                        db = MySQLDatabase(userLoginDetails)
                        validLogin = db.login()
                    db.mainLogic()
                    valid = False
                elif (self.menuOption == 2):
                    mongoDB = MongoDatabase()
                    mongoDB.run()
                    valid = False
                elif (self.menuOption == 9):
                    print ("Exiting the program...")
                    sys.exit(0)
        
    def printMenu(self):
        """ printMenu: Prints the main menu. """
        for x in range(0, len(self.menuLines)):
            print (self.menuLines[x])
            
    def printGnome(self):
        """ printGnome: Reads text file containing gnome in ASCII text and
            prints it out, stripping out newline characters. """
        with open('gnome.txt') as f:            
            for line in f: 
                line = line.rstrip('\n')
                print (line)
    
    def getMenuInput(self):
        """ getMenuInput: Gets user input for the menu, returns True/False. """
        userChoice = input("Input option number: ")
        try:
            userChoice = int(userChoice)
        except:
            print ("Error. Please enter a valid number.")
            return False
        if (int(userChoice) not in [1,2,9]):
            print ("Error. Please enter a valid number.")
            return False
        else:
            self.menuOption = userChoice
            return True
        
if __name__ == "__main__":
    app = MainLogic()