shopping_list = []

def add_item():
    item = input("Enter the item to add: ").strip()
    shopping_list.append(item)
    print(f"{item} has been added  to your shopping list.")

def remove_item():
    item = input("Enter the item to remove: ").strip
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been revomed from you shopping list")
    else:
        print(f"{item} not found on your cart")

def view_list():
    if not shopping_list:
        print("Your shoping lists is empty")
    else:
        print("\nYour shopping list: ")
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")

def display_menu():
    print("Shopping list manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    while True:
        display_menu()
        choice = input("Choose an option 1-4: ").strip()

        if choice == "1":
            add_item()
        elif choice == "2":
            remove_item()
        elif choice == "3":
            view_list()
        elif choice == "4":
            print("Exiting shopping list.")
            break
        else:
            print("Invalid choices")



if __name__ == "__main__":
    main()