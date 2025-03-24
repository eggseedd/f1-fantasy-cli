from database.db import get_db

def engines_list():
    with get_db() as conn:
        with conn.cursor() as cursor:

            cursor.execute("SELECT manufacturer FROM engines")
            print("\nEngine Manufacturers List:")
            for row in cursor.fetchall():
                print(row.manufacturer)
