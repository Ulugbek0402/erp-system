from file_manager import write, read

super_admin_login = "superadmin"
super_admin_password = "superadmin"


def login():
    user_login = input("Enter your phone number: ")
    password = input("Enter your password: ")

    if user_login == super_admin_login and password == super_admin_password:
        print("Welcome boss !")
        return "super_admin"

    users = read(filename="users.csv")
    for index, user in enumerate(users):

        if user[1] == user_login and user[2] == password:
            if user[3] == "admin":
                users[index][-1] = 1
                write(filename="users.csv", data=users)
                print(f"Welcome, {user[1]}")
                return "admin"
            elif user[3] == "teacher":
                users[index][-1] = 1
                write(filename="users.csv", data=users)
                print(f"Welcome, {user[1]}")
                return "teacher"
            elif user[3] == "student":
                users[index][-1] = 1
                write(filename="users.csv", data=users)
                print(f"Welcome, {user[1]}")
                return "student"
    print("Wrong phone number or password")
    return False


def logout():
    data = read(filename="users.csv")
    for index in range(len(data)):
        data[index][-1] = 0
        write(filename="users.csv", data=data)


def get_active_user():
    users = read(filename="users.csv")
    for user in users:
        if user[-1] == "1":
            return user