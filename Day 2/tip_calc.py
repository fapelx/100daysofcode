user_money_prompt = float(input("Hello how large was a bill?\n"))
user_how_many_people = int(input("How many people want to split a bill?\n"))
user_how_much_tip = float(input("How big tip in % you wish to give?\n"))
total_with_tip = user_money_prompt * (1+user_how_much_tip/100)
total_per_person = total_with_tip/user_how_many_people

print(f"You each need to pay {round(total_per_person,2)} $")