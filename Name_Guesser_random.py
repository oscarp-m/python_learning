import random
import string
 
total_number_of_loops = 0
name_to_guess = str(input("Enter the name to guess: ")).lower()
loops_todo = int(input("Enter the number of loops to do: "))
guessed_name = ""
name_is_guessed = False
number_of_guesses = 0
total_number_of_guesses = 0

print(f"Loop's done: {total_number_of_loops}")
while total_number_of_loops < loops_todo:
    number_of_loops = 0
    guessed_name = ""
    name_is_guessed = False

    while name_is_guessed == False:
        for char in name_to_guess:
            char_is_correct = False
            while char_is_correct == False:
                guessed_char = random.choice(string.ascii_lowercase)
                print(f"{guessed_char}")
                number_of_guesses = number_of_guesses + 1

                if guessed_char == char:
                    guessed_name = guessed_name + guessed_char
                    print(f"{guessed_name}")
                    char_is_correct = True

            if guessed_name == name_to_guess:
                name_is_guessed = True
                
    guessed_name = ""
    total_number_of_guesses = total_number_of_guesses + number_of_guesses
    number_of_guesses = 0
    total_number_of_loops = total_number_of_loops + 1
    print(f"Loop's done: {total_number_of_loops}")
                
print(f"Number of guesses to guess the name: {total_number_of_guesses}")
print(f"the mean number of guesses to guess the name: {total_number_of_guesses / total_number_of_loops}")
  