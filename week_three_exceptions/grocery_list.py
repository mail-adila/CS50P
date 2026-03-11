# 03/03/2026 - Tuesday

# In a file called grocery.py, implement a program that prompts the user for items, one per line,
# until the user inputs control-d (which is a common way of ending one’s input to a program).
# Then output the user’s grocery list in all uppercase, sorted alphabetically by item,
# prefixing each line with the number of times the user inputted that item. No need to pluralize
# the items. Treat the user’s input case-insensitively.

def get_items():
    items = []
    while True:
        try:
            item = input("Enter the item: ").strip().lower()
        except EOFError:
            get_cost(items)
            break
        else:
            items.append(item)

def get_cost(list_of_items):
    grocery_list = {}
    for item in list_of_items:
        grocery_list[item] = grocery_list.get(item, 0) + 1

    for key in sorted(grocery_list):
        print(f"{grocery_list[key]}  {key.upper()}")


def main():
    get_items()

if __name__ == "__main__":
    main()

