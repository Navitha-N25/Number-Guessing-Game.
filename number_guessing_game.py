import random
import time

def play_game(high_scores):
    print("\nWelcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Choose the difficulty level:")

    difficulties = {
        "1": ("Easy", 10),
        "2": ("Medium", 5),
        "3": ("Hard", 3)
    }

    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")

    choice = input("Enter your choice (1/2/3): ").strip()

    while choice not in difficulties:
        choice = input("Please enter 1, 2, or 3: ").strip()

    level, chances = difficulties[choice]
    number = random.randint(1, 100)
    attempts = 0

    print(f"\nGreat! You selected {level} difficulty.")
    print("Let's start the game!")
    start_time = time.time()

    while attempts < chances:
        try:
            guess = int(input(f"\nEnter your guess (1-100). Chances left: {chances - attempts}: "))
        except ValueError:
            print("Please enter a valid whole number.")
            continue

        if not 1 <= guess <= 100:
            print("Your guess must be between 1 and 100.")
            continue

        attempts += 1

        if guess == number:
            elapsed = time.time() - start_time
            print(f"\nCongratulations! You guessed the correct number in {attempts} attempts.")
            print(f"Time taken: {elapsed:.1f} seconds.")

            previous_best = high_scores.get(level)
            if previous_best is None or attempts < previous_best:
                high_scores[level] = attempts
                print(f"New {level} high score: {attempts} attempts!")
            else:
                print(f"{level} high score: {previous_best} attempts.")
            return

        if guess < number:
            print(f"Incorrect! The number is greater than {guess}.")
        else:
            print(f"Incorrect! The number is less than {guess}.")

        if attempts < chances:
            if number % 2 == 0:
                parity = "even"
            else:
                parity = "odd"
            print(f"Hint: The number is {parity}.")
            print(f"Hint: The number is in the {'lower' if number <= 50 else 'upper'} half (1-50 or 51-100).")

    print(f"\nGame over! You ran out of chances. The number was {number}.")


def main():
    high_scores = {}
    print("=" * 40)
    print("Welcome to the Number Guessing Game!")
    print("Rules: Guess the secret number from 1 to 100.")
    print("I'll tell you if your guess is too high or too low.")
    print("=" * 40)

    while True:
        play_game(high_scores)

        print("\nHigh scores this session:")
        if high_scores:
            for level, score in high_scores.items():
                print(f"- {level}: {score} attempts")
        else:
            print("No winning scores yet.")

        again = input("\nWould you like to play again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Thanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    main()
