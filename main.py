from models.drivers import drivers_list
from models.principals import principal_list
from models.engines import engines_list
from models.teams import add_team, teams_list, edit_team, delete_team

print("\n----F1 FANTASY 2025----")
print("Make Your Dream F1 Team!")

while True:
    print("\n1. Drivers List\n2. Team Principals List\n3. Engine Manufacturers List \n4. Add a new team\n5. Edit a team\n6. Remove a team\n7. Custom Teams List\n8. Exit")
    choice = input("Choose an option: ")
    if choice == '1':
        drivers_list()
    elif choice == '2':
        principal_list()
    elif choice == '3':
        engines_list()
    elif choice == '4':
        add_team()
    elif choice == '5':
        edit_team()
    elif choice == '6':
        delete_team()
    elif choice == '7':
        teams_list()
    elif choice == '8':
        break

    '''
    tambah fungsi delete team
    tambah fungsi edit team
    '''




