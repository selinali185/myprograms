# database practice 
import sqlite3

#connection allows us to connect 
# python to a SQL database
connection = sqlite3.connect("./database.db")
#curso allows us to interact with sql db 
cursor = connection.cursor()

query = """
SELECT product_name, price FROM Products;
"""

result = cursor.execute(query).fetchall()
print(f"OUR SQL RESULT: {result}")


#BOTTOM/END OF OUR CODE
connection.commit() #this commits our changes 
connection.close() #this disconnects our connection 