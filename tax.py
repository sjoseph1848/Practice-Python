import xlrd
import MySQLdb

#Open the workbook and define the worksheet
general = xlrd.open_workbook("GeneralLedger.xls")
sheet = general.sheet_by_index(0)

#Establish a MySQL connection
database = MySQLdb.connect (host="localhost",user="root",passwd="Nice4you",db = "taxAccounting")

#Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()

#Create the INSERT INTO sql query
query = """INSERT INTO table_generalLedger (AccountNumber,Description,Amount,ClientId) VALUES(%s,%s,%s,%s)"""
#Create a For Loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
for r in range(1, sheet.nrows):
        AccountNumber = sheet.cell(r,0).value
        Description   = sheet.cell(r,1).value
        Amount        = sheet.cell(r,2).value
        ClientId      = sheet.cell(r,3).value

#Assign values from each row
        values = (AccountNumber,Description,Amount,ClientId)


#Execute sql query
        cursor.execute(query,values)
#Close the cursor
cursor.close()
#Commit the transaction
database.commit()
#Close the database connection
database.close()
#Print results
print("")
print("Your General Ledger is in")
