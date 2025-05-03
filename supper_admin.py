from os import lseek

from file_manager import write, read


def show_all_admins():
    users = read('users.csv')
    print("\nList of admins:")
    for user in users:
        if user[3] == "admin":
            print(f"{user[1]}")
    print()


def create_admin():
    users = read("users.csv")
    user_id = str(int(users[-1][0] + 1 if users else 1))
    phone = input("Enter new admins phone number: ")
    password = input("Enter password: ")
    for user in users:
        if user[1] == phone:
            print("This number already exists: ")
            return

    new_user = [user_id, phone,password, "admin", '0' ]
    users.append(new_user)
    write('users.csv', users)
    print("Admin successfully created!")

def delete_admin():
    users = read("users.csv")
    phone = input("Enter admins phone number: ")
    new_users = [u for u in users if not (u[1] == phone and u[3] == 'admin')]

    if len(new_users) == len(users):
        print("Admin not found")
    else:
        write("users.csv", new_users)
        print("Admin deleted")
