from database.db import get_db

def principal_list():
    with get_db() as conn:
        with conn.cursor() as cursor:

            cursor.execute("SELECT name, experience FROM team_principals ORDER BY experience DESC")
            print("\nTeam Principals List:")
            print("Name || Experience")
            for row in cursor.fetchall():
                print(f"{row.name} || {row.experience} year(s)")
