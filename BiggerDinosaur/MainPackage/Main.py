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
    # Instantiate the object types 
    myState = state
    myStore = store
    myStoreHistory = storeHistory
    # Invoke the Connect method and store what it returns in another variable 
    myCursor = myState.Connect("GroceryStoreSimulator") #database 
    myCursor = myStore.Connect("GroceryStoreSimulator") #database 
    myCursor = myStoreHistory.Connect("GroceryStoreSimulator") 
    # Submit query to SQL server and join tables 
    myCursor.execute("""
                                    SELECT S.city, St.stateAbbreviation, S.store, SH.storeID
                                    FROM dbo.tState St 
                                    INNER JOIN dbo.tStore S ON St.stateAbbreviation = S.store
                                    INNER JOIN dbo.tStoreHistory SH ON S.state = SH.storeID
                                    WHERE St.stateAbbreviation = 'OH'
                                """)
    print("All Grocery Stores in Ohio: " + str())
    
    
    
            
    
        