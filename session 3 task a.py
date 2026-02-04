# Task A


contacts = {}


contacts["Ahmad"] = "123-456-7890"
contacts["Mina"] = "098-765-4321"
contacts["Sarah"] = "555-123-4567"


print("All contacts:")
for name, phone in contacts.items():
    print(f"{name}: {phone}")


search_name = input("Enter a name to search (or 'quit' to exit): ")
while search_name.lower() != 'quit':
    if search_name in contacts:
        print(f"{search_name}: {contacts[search_name]}")
    else:
        print(f"{search_name} not found.")
    search_name = input("Enter a name to search (or 'quit' to exit): ")

