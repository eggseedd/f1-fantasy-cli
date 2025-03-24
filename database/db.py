import pyodbc

def get_db():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost;"
        "DATABASE=f1_fantasy;"
        "Trusted_Connection=yes;"
    )
    return conn
