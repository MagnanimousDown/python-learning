# This code is to check the ODBC driver version on the system
# import pyodbc

# print(pyodbc.drivers())

# Creating first connection:

# import pyodbc

# conn = pyodbc.connect(
#     "DRIVER={ODBC Driver 17 for SQL Server};"
#     "SERVER=OMKAR\\SQLEXPRESS;"
#     "DATABASE=master;"
#     "Trusted_Connection=yes;"
# )

# print("Connected successfully!")

# cursor = conn.cursor()

# cursor.execute("SELECT 1")

# row = cursor.fetchall()

# print(row)

# conn.close()