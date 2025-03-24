from database.db import get_db

def drivers_list():
    with get_db() as conn:
        with conn.cursor() as cursor:

            cursor.execute("SELECT name, nationality FROM drivers")
            print("\nDrivers List:")
            print("Name || Nationality")
            for row in cursor.fetchall():
                print(f"{row.name} || {row.nationality}")
