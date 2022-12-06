import pyodbc

connect_db = pyodbc.connect(driver='{SQL Server}', 
                      host='LAPTOP-A2R2157O', database='HTTM',
                      user='sa', password='1408')