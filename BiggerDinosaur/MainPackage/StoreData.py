#storeData.py
# Name: Bigger Dinosaur Brianna Jarrell, Maddie, Akash 
# email: jarrelbc@mail.uc.edu
# Assignment Number: Assignment 08
# Date: 3-28-24
# Course/Section:IS 4010-002
# Semester/Year: Spring 2024
# Brief Description of the assignment:
# Citations:
# Anything else that's relevant:We are pulling code from the SQL file and getting data it
  

import pyodbc

class state:
    def Connect(self,myDatabase = "GroceryStoreSimulator"):  
        '''
        Connect to the database and create a cursor
        @return: The cursor object
        '''
        conn = pyodbc.connect('Driver={SQL Server};'
            'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
            'Database=' + myDatabase+ ';'
            'uid=IS4010Login;'
            'pwd=P@ssword2;')
        
        cursor = conn.cursor()
        return cursor
    
class store:
    def Connect(self,myDatabase = "GroceryStoreSimulator"):  
        '''
        Connect to the database and create a cursor
        @return: The cursor object
        '''
        conn = pyodbc.connect('Driver={SQL Server};'
            'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
            'Database=' + myDatabase+ ';'
            'uid=IS4010Login;'
            'pwd=P@ssword2;')
        
        cursor = conn.cursor()
        return cursor
    
class storeHistory:
    def Connect(self,myDatabase = "GroceryStoreSimulator"):  
        '''
        Connect to the database and create a cursor
        @return: The cursor object
        '''
        conn = pyodbc.connect('Driver={SQL Server};'
            'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
            'Database=' + myDatabase+ ';'
            'uid=IS4010Login;'
            'pwd=P@ssword2;')
        
        cursor = conn.cursor()
        return cursor
