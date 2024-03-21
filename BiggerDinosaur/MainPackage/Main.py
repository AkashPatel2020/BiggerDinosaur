#main.py
SELECT S.city, St.stateAbbreviation, S.store,  SH.storeID
FROM dbo.tState St, dbo.tStore S, dbo.tStoreHistory SH
WHERE St.stateAbbreviation = 'OH'
  