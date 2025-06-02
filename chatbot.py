# 💬 Chat Bot - Cosmetic Store 🛍️
import datetime

# 🕒 Greeting based on the time of day
def greeting():
    hour = datetime.datetime.now().hour
    if hour < 12:
        return "🌅 Good Morning! Welcome to the Cosmetic Store Chatbot!"
    elif 12 <= hour < 18:
        return "☀️ Good Afternoon! Welcome to the Cosmetic Store Chatbot!"
    else:
        return "🌙 Good Evening! Welcome to the Cosmetic Store Chatbot!"

print(greeting())

# 📋 Menu (Product: Price in ₹)
menu = {
    "💄 Lipstick": 250.0,
    "🖤 Kajal": 120.0,
    "🧴 Foundation": 500.0,
    "🧼 Compact Powder": 300.0,
    "🌸 Blush": 280.0,
    "🧽 Makeup Remover": 200.0,
    "🎁 Combo (Lipstick + Kajal)": 350.0,
    "🎁 Combo (Foundation + Compact Powder)": 750.0
}

# 📢 Function to display the menu
def show_menu():
    print("\n--- 📦 COSMETIC MENU ---")
    for item, price in menu.items():
        print(f"{item}: ₹{price:.2f}")
    print()

# 🛍️ Function to take the order
def take_order():
    order = {}
    while True:
        item = input("🛒 Enter the name of the item you want to order (or type 'done' to finish): ").title()
        if item == "Done":
            break
        elif item in menu:
            quantity = int(input(f"🔢 How many {item}s would you like? "))
            if item in order:
                order[item] += quantity  # ➕ add to existing quantity
            else:
                order[item] = quantity   # 🆕 add new item to order
        else:
            print("❌ Sorry, that item is not on the menu. Please try again.")
    return order

# 🧾 Function to calculate the total bill
def calculate_bill(order):
    total = 0
    print("\n🧾 --- YOUR ORDER SUMMARY ---")
    for item, quantity in order.items():
        price = menu[item] * quantity
        total += price
        print(f"{item} x {quantity} = ₹{price:.2f}")

    # 🚚 Add delivery charges for bill below ₹200
    if total < 200:
        print("🚚 A delivery charge of ₹30 has been added for orders below ₹200")
        total += 30

    print(f"\n💵 Total Bill: ₹{total:.2f}")
    return total

# 🧠 Main Chatbot function
def cosmetic_chatbot():
    print("🎉 Welcome to the Cosmetic Store Chatbot!")
    show_menu()
    order = take_order()

    if order:
        total = calculate_bill(order)
        print("\n🙏 Thank you for shopping with us!")
        print("👋 We hope to see you again soon!")
    else:
        print("⚠️ You didn't order anything. Goodbye!")

# ▶️ Start the chatbot
cosmetic_chatbot()
