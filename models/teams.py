from database.db import get_db

def add_team():
    try:
        team_name = input("Enter your team name: ")
        team_principal = input("Choose your team principal: ")
        team_engine = input("Choose your engine manufacturer: ")
        driver_names = input("Choose your drivers (comma-seperated): ").split(',')

        conn = get_db()
        with conn:
            with conn.cursor() as cursor:

                cursor.execute("SELECT id FROM team_principals WHERE name = ?", team_principal)
                p_check = cursor.fetchone()
                if p_check == None:
                    print("Error: Team principal not found.")
                    return
                principal_id = p_check[0]
                
                cursor.execute("SELECT id FROM engines WHERE manufacturer = ?", team_engine)
                e_check = cursor.fetchone()
                if e_check == None:
                    print("Error: Engine not found.")
                    return
                engine_id = e_check[0]
                
                drivers_id = []
                for driver in driver_names:
                    cursor.execute("SELECT id FROM drivers WHERE name = ?", driver)
                    d_check = cursor.fetchone()
                    if d_check == None:
                        print(f"Error: Driver not found.")
                        return
                    drivers_id.append(d_check[0])
                    
                cursor.execute("INSERT INTO teams (name) OUTPUT INSERTED.id VALUES (?)", team_name)
                team_id = cursor.fetchone()[0]

                cursor.execute("INSERT INTO team_principals_teams (team_principals_id, teams_id) VALUES (?, ?)", (principal_id, team_id))
                cursor.execute("INSERT INTO engines_teams (engines_id, teams_id) VALUES (?, ?)", (engine_id, team_id))
                for driver in drivers_id:
                    cursor.execute("INSERT INTO teams_drivers (teams_id, drivers_id) VALUES (?, ?)", (team_id, driver))

            conn.commit()
            print(f"Team '{team_name}' added successfully!")

    except Exception as e:
        conn.rollback()
        print(f"Error adding team: {e}")

def delete_team():
    try:
        team_name = input("Select the team you want to remove: ")

        conn = get_db()
        with conn:
            with conn.cursor() as cursor:

                cursor.execute("SELECT id FROM teams WHERE name = ?", team_name)
                team_id = cursor.fetchone()
                if team_id is None:
                    print("Error: Team not found.")
                    return
                team_id = team_id[0]

                cursor.execute("DELETE FROM teams WHERE id = ?", team_id)

            conn.commit()
            print(f"Team '{team_name}' deleted successfully!")

    except Exception as e:
        conn.rollback()
        print(f"Error deleting team: {e}")


def edit_team():
    try:
        team_name = input("Select the team you want to edit: ")
        print("**If you don't want to change, re-enter the old value**")
        new_team_name = input("Enter the new team name: ")
        new_principal = input("Enter the new team principal: ")
        new_drivers = input("Enter the new drivers (comma-seperated): ").split(',')
        new_engine = input("Enter the new engine: ")

        conn = get_db()
        with conn:
            with conn.cursor() as cursor:

                cursor.execute("SELECT id FROM teams WHERE name = ?", team_name)
                team_id = cursor.fetchone()
                if team_id is None:
                    print("Error: Team not found.")
                    return
                team_id = team_id[0]

                cursor.execute("SELECT id FROM team_principals WHERE name = ?", new_principal)
                p_check = cursor.fetchone()
                if p_check == None:
                    print("Error: Team principal not found.")
                    return
                principal_id = p_check[0]
                
                cursor.execute("SELECT id FROM engines WHERE manufacturer = ?", new_engine)
                e_check = cursor.fetchone()
                if e_check == None:
                    print("Error: Engine not found.")
                    return
                engine_id = e_check[0]
                
                drivers_id = []
                for driver in new_drivers:
                    cursor.execute("SELECT id FROM drivers WHERE name = ?", driver)
                    d_check = cursor.fetchone()
                    if d_check == None:
                        print(f"Error: Driver not found.")
                        return
                    drivers_id.append(d_check[0])
                
                cursor.execute("UPDATE teams SET name = ? WHERE id = ?", (new_team_name, team_id))

                cursor.execute("UPDATE team_principals_teams SET team_principals_id = ? WHERE teams_id = ?", (principal_id, team_id))
                cursor.execute("UPDATE engines_teams SET engines_id = ? WHERE teams_id = ?", (engine_id, team_id))
                cursor.execute("DELETE FROM teams_drivers WHERE teams_id = ?", team_id)
                for driver in drivers_id:
                    cursor.execute("INSERT INTO teams_drivers (teams_id, drivers_id) VALUES (?, ?)", (team_id, driver))

            
            conn.commit()
            print(f"Team '{new_team_name}' updated successfully!")            

    except Exception as e:
        conn.rollback()
        print(f"Error updating team: {e}")


def teams_list():
    with get_db() as conn:
        with conn.cursor() as cursor:

            cursor.execute("SELECT * FROM teams")
            print("\nTeams List:")
            for row in cursor.fetchall():
                team_id = row[0]
                print(f"\n{row.name}")
                cursor.execute("SELECT name from team_principals JOIN team_principals_teams ON id=team_principals_id WHERE teams_id = ?", team_id)
                temp = cursor.fetchone()
                print(f"{temp.name} (Team Principal)")

                cursor.execute("SELECT name from drivers JOIN teams_drivers ON id=drivers_id WHERE teams_id = ?", team_id)
                for index, driver in enumerate(cursor.fetchall()):
                    print(f"{driver.name} (Driver {index + 1})")

                cursor.execute("SELECT manufacturer from engines JOIN engines_teams ON id=engines_id WHERE teams_id = ?", team_id)
                temp = cursor.fetchone()
                print(f"{temp.manufacturer} (Engine Manufacturer)")