# BJC, Original Author, 2/2024
# Program that considers chances for a holiday gift exchange of a user getting
# themself. Uses a permutation generator to do so.

from permutation_gen import *

def how_likely_to_get_self(infix):
    wins = 0
    losses = 0
    perm_list = consider_number(infix)
    all_perms = generate_all_permutations(perm_list)
    # Could return a list as [3 (wins), 6 (tries)]
    for permutation in all_perms:
        # Enumerate puts the index number and value into a tuple like [(0,2)] if my list was [2].
        # Next, it creates boolean values where each value is true if the current index is not in orignal position, and false otherwise.
        # The all() function checks if all the boolean values are true.
        if all(index != p for index, p in enumerate(permutation)):
            # If all elements are not in their original position, considered a True, and is thus a win.
            wins += 1
        losses += 1

    return [wins, losses]

def main():

    # Gets input from user
    while True:
        amt_of_students = int(input("Please pick a number from 2 to 10: "))
        if amt_of_students > 10 or amt_of_students < 2:
            print("Sorry, only choose a number between 2 and 10")
        else:
            break

    odds = how_likely_to_get_self(amt_of_students)
    wins = odds[0]
    tries = odds[1] # Count of Total Permutations

    print(f"{wins} of {tries} wins. Probability of a person getting themself is", wins / tries)

if __name__ == '__main__':
    main()
