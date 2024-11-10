import csv
import random


def load_countries(filename):
    """Reads a CSV file and returns a list of country names."""
    countries = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            countries.append(row[0])  # Assuming each row has one country name
    return countries


def pick_random_country(countries):
    """Randomly selects a country from the list."""
    return random.choice(countries).upper()


def display_current_state(country, guessed_letters):
    """Displays the current state of the country name with guessed letters and dashes."""
    display = ''.join([letter if letter in guessed_letters else '-' for letter in country])
    return display


def play_game(country):
    """Main game loop."""
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 5

    print("Welcome to the Country Guessing Game!")
    print("Try to guess the country name. You have 5 chances to guess wrong.")

    while incorrect_guesses < max_incorrect_guesses:
        # Display current state
        current_state = display_current_state(country, guessed_letters)
        print("Country:", current_state)

        # Check if player has won
        if '-' not in current_state:
            print("Congratulations! You guessed the country:", country)
            break

        # Get player's guess
        guess = input("Guess a letter: ").upper()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
            continue

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        # Add the guess to the set of guessed letters
        guessed_letters.add(guess)

        # Check if the guess is in the country name
        if guess in country:
            print(f"Good guess! '{guess}' is in the country name.")
        else:
            incorrect_guesses += 1
            print(f"Wrong guess! You have {max_incorrect_guesses - incorrect_guesses} chances left.")

        # If reached maximum incorrect guesses
        if incorrect_guesses == max_incorrect_guesses:
            print("Sorry, you've run out of guesses. The country was:", country)


# Load the country list and start the game
filename = 'countries.csv'  # Replace with the path to your CSV file
countries = load_countries(filename)
selected_country = pick_random_country(countries)
play_game(selected_country)
