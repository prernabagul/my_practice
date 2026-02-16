class PasswordManager:
    def __init__(self, filename="passwords.txt"):
        self.filename = filename

    def add_password(self):
        website = input("Enter website name: ")
        username = input("Enter username: ")
        password = input("Enter password: ")

        with open(self.filename, "a") as file:
            file.write(f"{website},{username},{password}\n")

        print("Password saved successfully!")

    def view_passwords(self):
        try:
            with open(self.filename, "r") as file:
                data = file.readlines()

                if not data:
                    print("No passwords saved yet.")
                    return

                print("\nSaved Passwords:")
                for line in data:
                    website, username, password = line.strip().split(",")
                    print(f"Website: {website} | Username: {username} | Password: {password}")

        except FileNotFoundError:
            print("No passwords saved yet.")

    def search_password(self):
        website_to_search = input("Enter website to search: ")

        try:
            with open(self.filename, "r") as file:
                for line in file:
                    website, username, password = line.strip().split(",")
                    if website.lower() == website_to_search.lower():
                        print(f"Found -> Username: {username}, Password: {password}")
                        return
                print("Website not found.")
        except FileNotFoundError:
            print("No passwords saved yet.")

    def delete_password(self):
        website_to_delete = input("Enter website to delete: ")
        updated_data = []

        try:
            with open(self.filename, "r") as file:
                for line in file:
                    website, username, password = line.strip().split(",")
                    if website.lower() != website_to_delete.lower():
                        updated_data.append(line)

            with open(self.filename, "w") as file:
                file.writelines(updated_data)

            print("Password deleted (if it existed).")

        except FileNotFoundError:
            print("No passwords saved yet.")


# -------- MAIN PROGRAM --------
manager = PasswordManager()

while True:
    print("\n===== PASSWORD MANAGER =====")
    print("1. Add Password")
    print("2. View All Passwords")
    print("3. Search Password")
    print("4. Delete Password")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == "1":
        manager.add_password()
    elif choice == "2":
        manager.view_passwords()
    elif choice == "3":
        manager.search_password()
    elif choice == "4":
        manager.delete_password()
    elif choice == "5":
        print("Exiting Password Manager 🔐")
        break
    else:
        print("Invalid choice. Try again.")
