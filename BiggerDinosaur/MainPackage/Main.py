#main.py
# Name: Brianna Jarrell
# email: jarrelbc@mail.uc.edu
# Assignment Number: Assignment 08
# Date: 3-28-24
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
    myCursor = myState.Connect("GroceryStoreSimulator") 
    myCursor = myStore.Connect("GroceryStoreSimulator") 
    myCursor = myStoreHistory.Connect("GroceryStoreSimulator") 
    # Submit query to SQL server and join tables 
    
    myCursor.execute("""
                        SELECT S.city, St.stateAbbreviation, S.store, SH.storeID
                        FROM dbo.tState St 
                        INNER JOIN dbo.tStore S ON St.stateAbbreviation = S.store
                        INNER JOIN dbo.tStoreHistory SH ON S.state = SH.storeID
                        WHERE St.stateAbbreviation = 'OH'
                        """)
    
    # Fetch all rows from the result
    rows = myCursor.fetchall()

    # Print only the "store" column
    for row in rows:
        print(row['store'])
        
    # Print total number of rows
    total_rows = myCursor.rowcount
    print("Total number of rows:", total_rows)