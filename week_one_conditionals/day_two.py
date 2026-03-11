# 02/25/2026 - Wednesday

# Convert typed smileys to actual smileys
def convert(user_input):
    # Making Faces
    if ":)" in user_input:
        user_input = user_input.replace(":)", "🙂")
    if ":(" in user_input:
        user_input = user_input.replace(":(", "🙁")
    return user_input

# Input mass in kg and outputs the equivalent number of Joules.
def convert_kg_joules(user_input):
    kilograms = int(user_input)
    # e=mc^2, c=300000000
    return kilograms * pow(300000000, 2)

# Tip calculator
def calculate_tip(meal_amount, tip_percentage):
    return meal_amount * tip_percentage / 100


def main():
    # meal_amount = float(input("How much was the meal:"))
    # tip_percentage = float(input("What percentage would you like to tip:"))
    # tip = calculate_tip(meal_amount, tip_percentage)
    # print(f"Tip amounts to ${tip:.2f}")
    # print(f"The total bill now is ${meal_amount + tip:.2f}")
    a = int(input("Enter the first number:"))
    b = int(input("Enter the second number:"))
    sum = a + b
    difference = a - b
    product = a * b
    division = float(a / b)
    print(f"Sum : {sum}")
    print(f"Difference : {difference}")
    print(f"Product : {product}")
    print(f"Division : {division:.2f}")


main()