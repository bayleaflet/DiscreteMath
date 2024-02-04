#BJC, Original Author, 2/2024
# Program that considers chances for a holiday gift exchange of a user getting
# themself. Uses a permutation generator to do so.

from permutation_gen import *

def do_calculation(infix):
    wins = 0
    losses = 0
    perm_list = consider_number(infix)
    all_perms = generate_all_permutations(perm_list)
    # Could return a list as [3 (wins), 6 (tries)]
    for index, permutation in enumerate(all_perms):
        if index == permutation[index]:
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

    odds = do_calculation(amt_of_students)
    wins = odds[0]
    tries = odds[1] # Count of Total Permutations

    print(f"{wins} of {tries} wins. Probability of a person getting themself is", wins / tries)

if __name__ == '__main__':
    main()
