#define the menu of hotel

menu = {
    'pizza':40,
    'pasta':50,
    'burger':60,
    'salad':70,
    'coffee':80,
}

#greet
print("Welcome to Taj Hotel")
print(" Pizza: Rs40 \n Pasta: Rs50 \n Burger: Rs60 \n Salad: Rs70 \n Coffee: Rs80")


#total the menu item
order_total = 0

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not avaialable yet!")

another_order = input("Do you want to add another item? (yes/no) ")
if another_order == "yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not avaialable!")

print(f"The total amount of items to pay is {order_total}")