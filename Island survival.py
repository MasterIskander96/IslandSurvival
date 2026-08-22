import random
import time

days = 99
health = 100
food = 50
water = 50
wood = 0
stone = 0
metal = 0

print("Welcome to the game 'Island Survival'!")
time.sleep(2)
print(f"You have been stranded on a deserted island and must survive for {days} days using your skills and resources.")

for day in range(1, days + 1):
    time.sleep(2)
    print("\nYour current stats:")
    time.sleep(1)
    print(f"======== Day: {day} ========")
    time.sleep(1)
    print(f"❤️  Health: {health}")
    print(f"🍖  Food: {food}")
    print(f"💧  Water: {water}")
    print(f"🪵  Wood: {wood}")
    print(f"🪨  Stone: {stone}")
    print(f"⛏️  Metal: {metal}")
    time.sleep(4)

    print("\n1. Find food")
    print("2. Find water")
    print("3. Rest")
    print("4. Gather wood")
    print("5. Gather stone")
    print("6. Gather metal")
    print("7. Quit game")
    choice = input("\nChoose an action: ")
    
    if choice == "1":
        found_food = random.randint(0, 30)
        food += found_food
        print(f"You found {found_food} units of food.")
    elif choice == "2":
        found_water = random.randint(0, 30)
        water += found_water
        print(f"You found {found_water} units of water.")
    elif choice == "3":
        health += random.randint(0, 5)
        print("You rested and recovered health.")
    elif choice == "4":
        gathered = random.randint(5, 20)
        wood += gathered
        print(f"You gathered {gathered} units of wood.")
        health_loss = random.randint(1, 3)
        health -= health_loss
        print(f"You lost {health_loss} health while working.")
    elif choice == "5":
        gathered = random.randint(3, 15)
        stone += gathered
        print(f"You gathered {gathered} units of stone.")
        health_loss = random.randint(1, 4)
        health -= health_loss
        print(f"You lost {health_loss} health while working.")
    elif choice == "6":
        gathered = random.randint(1, 10)
        metal += gathered
        print(f"You gathered {gathered} units of metal.")
        health_loss = random.randint(2, 5)
        health -= health_loss
        print(f"You lost {health_loss} health while working.")
    elif choice == "7":
        print("You decided to quit the game. Goodbye!")
        break
    else:
        print("Invalid choice! Please select 1-7.")
        continue

    # Daily resource consumption
    food -= random.randint(3, 10)
    water -= random.randint(3, 10)
    health -= random.randint(0, 2)

    # Check for negative resources
    if food < 0:
        food = 0
        health -= random.randint(5, 10)
        print("You're starving! Health decreased.")
    if water < 0:
        water = 0
        health -= random.randint(5, 10)
        print("You're dehydrated! Health decreased.")

    # Random events
    event = random.randint(1, 100)
    
    if event <= 10:
        print("You found an abandoned camp with food and water!")
        food += random.randint(10, 20)
        water += random.randint(10, 20)
    elif event <= 20:
        print("You encountered a wild animal and got injured!")
        health -= random.randint(5, 15)
    elif event <= 30:
        print("You found bandages and treated your wound, recovering health.")
        health += random.randint(5, 15)
    elif event <= 40:
        print("You found a source of fresh water!")
        water += random.randint(10, 20)
    elif event <= 50:
        print("You found a fruit tree and gathered some food.")
        food += random.randint(10, 20)
    elif event <= 60:
        print("You found an old chest with supplies!")
        food += random.randint(5, 15)
        water += random.randint(5, 15)
    elif event <= 70:
        print("You found medicinal herbs and recovered health.")
        health += random.randint(5, 15)
    elif event <= 80:
        print("You found a campfire and warmed up, recovering health.")
        health += random.randint(5, 15)
    elif event <= 85:
        print("You found a pile of wood!")
        wood_gained = random.randint(10, 20)
        wood += wood_gained
        print(f"Added {wood_gained} wood.")
    elif event <= 90:
        print("You found a stone deposit!")
        stone_gained = random.randint(10, 20)
        stone += stone_gained
        print(f"Added {stone_gained} stone.")
    elif event <= 95:
        print("You found scrap metal!")
        metal_gained = random.randint(5, 15)
        metal += metal_gained
        print(f"Added {metal_gained} metal.")
    elif event == 100:
        print("You found an old boat and managed to sail away from the island!")
        print("Congratulations! You survived!")
        break
    
    # Cap resources at 100
    if food > 100:
        food = 100
    if water > 100:
        water = 100
    if health > 100:
        health = 100
    if wood > 100:
        wood = 100
    if stone > 100:
        stone = 100
    if metal > 100:
        metal = 100
    
    if health <= 0:
        print("\nYou died. Game over!")
        break

    input("\nPress Enter to continue...")
