#main.py
# Name: Brianna Jarrell
# email: jarrelbc@mail.uc.edu
# Assignment Number: Assignment 08
# Date: 3-21-24
# Course/Section:IS 4010-002
# Semester/Year: Spring 2024
# Brief Description of the assignment:
  
from MainPackage.StoreData import * 

if __name__ == "__main__":
    # Instantiate an object of type Data
    myData = Data
    # Invoke the Connect method and store what it returns in another variable 
    myCursor = myData.Connect("GroceryStoreSimulator") #database 
    
    # my work to join tables 
    myCursor.executecursor.execute("""
                                    SELECT S.city, St.stateAbbreviation, S.store, SH.storeID
                                    FROM dbo.tState St 
                                    INNER JOIN dbo.tStore S ON St.stateAbbreviation = S.store
                                    INNER JOIN dbo.tStoreHistory SH ON S.state = SH.storeID
                                    WHERE St.stateAbbreviation = 'OH'
                                """)
    
    
    
            
    
        