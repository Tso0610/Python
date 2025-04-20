from random import randint
from gamedata import data

game_over = False
score = 0
while not game_over:
    index_a = randint(0, len(data) - 1)
    index_b = randint(0, len(data) - 1)
    while index_b == index_a:
        index_b = randint(0, len(data) - 1)

    follower_a = data[index_a]['follower_count']
    follower_b = data[index_b]['follower_count']
    print(
        f"Compare A: {data[index_a]['name']}, {data[index_a]['description']}, {data[index_a]['country']}")
    print("VS")
    print(
        f"Compare B: {data[index_b]['name']}, {data[index_b]['description']}, {data[index_b]['country']}")
    guess = input("Who has more follower? Type 'A' or 'B': ").upper()

    if guess == 'A':
        if follower_a > follower_b:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True
    elif guess == 'B':
        if follower_b > follower_a:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True
    else:
        print("Invalid input. Please type 'A' or 'B'.")

print("Thanks for playing!")
