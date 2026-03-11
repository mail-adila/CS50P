# 02/28/2026

# implement a program that prompts consumers users to input a fruit (case-insensitively)
# and then outputs the number of calories in one portion of that fruit, per the FDA’s poster for fruits,
# which is also available as text. Capitalization aside, assume that users will input fruits exactly
# as written in the poster (e.g., strawberries, not strawberry). Ignore any input that isn’t a fruit.
# Fruit,Serving Size,Calories,Potassium (%DV),Fiber (%DV),Sugars,Vit C (%DV)
# Apple,1 large (242g),130,7%,20%,25g,8%
# Avocado,1/5 medium (30g),50,4%,4%,0g,4%
# Banana,1 medium (126g),110,13%,12%,19g,15%
# Cantaloupe,1/4 medium (134g),50,7%,4%,11g,80%
# Grapefruit,1/2 medium (154g),60,5%,8%,11g,100%
# Grapes,3/4 cup (126g),90,7%,4%,20g,2%
# Honeydew,1/10 medium (134g),50,6%,4%,11g,45%
# Kiwifruit,2 medium (148g),90,13%,16%,13g,240%
# Lemon,1 medium (58g),15,2%,8%,2g,40%
# Lime,1 medium (67g),20,2%,8%,0g,35%
# Nectarine,1 medium (140g),60,7%,8%,11g,15%
# Orange,1 medium (154g),80,7%,12%,14g,130%
# Peach,1 medium (147g),60,7%,8%,13g,15%
# Pear,1 medium (166g),100,5%,24%,16g,10%
# Pineapple,2 slices (112g),50,3%,4%,10g,50%
# Plums,2 medium (151g),70,7%,8%,16g,10%
# Strawberries,8 medium (147g),50,5%,8%,8g,160%
# Sweet Cherries,21 cherries (140g),100,10%,4%,16g,15%
# Tangerine,1 medium (109g),50,5%,8%,9g,45%
# Watermelon,2 cups diced (280g),80,8%,4%,20g,25%

def find_calories(fruit):
    calorie_chart = {
        "Apple"   : 130,
        "Avocado" : 50,
        "Banana"  : 110,
        "Cantaloupe" : 50,
        "Grapefruit" : 60,
        "Grapes"     : 90,
        "Honeydew"   : 50,
        "Kiwifruit"  : 90,
        "Lemon"      : 15,
        "Lime"       : 20,
        "Nectarine"  : 60,
        "Orange"     : 80,
        "Peach"      : 60,
        "Pear"       : 100,
        "Pineapple"  : 50,
        "Plums"      : 70,
        "Strawberries":50,
        "Sweet Cherries":100,
        "Tangerine"  : 50,
        "Watermelon" : 80
    }
    fruit = fruit.strip().lower().title()
    return calorie_chart.get(fruit)

def main():
    consumer_fruit = input("Enter the fruit:")
    calories = (find_calories(consumer_fruit))
    if calories is not None:
        print(f"Calories: {calories}")

if __name__ == "__main__":
    main()