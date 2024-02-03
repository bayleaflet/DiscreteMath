# BJC, Original Author 1/29/2024
# Asks the user for a number between 1 and 9, and prints out all of the
# permutations for N in lexicographical order.

def print_instructions():
    print("Welcome to the permutation generator, where you can visualize all permutations in lexigographic order for the number N.")

def consider_number(input_amount):
    # Appends Input Number into list
    list_of_N = []
    for i in range(input_amount):
        list_of_N.append(int(i))
    return list_of_N

def find_next_permutation(A):
    # Finds the rightmost element that is smaller than element to its right
    i = len(A) -2
    while i >= 0 and A[i] >= A[i+1]:
        i -= 1
    if i == -1:
        return None

    # Finds smallest element to right of A[i] that is greater than A[i]
    j = len(A) - 1
    while A[j] <= A[i]:
        j -= 1

    A[i],A[j] = A[j],A[i]

    A[i+1:] = reversed(A[i+1:])
    return A

def generate_all_permutations(A):
    permutations = [A.copy()]
    while True:
        next_perm = find_next_permutation(A)
        if next_perm is None:
            break
        permutations.append(next_perm.copy())
        A = next_perm
    return permutations



def main():
    print_instructions
    while True:
        infix = int(input("Please choose a number 1-9 to use for the permutation generator: "))
        if infix > 9 or infix <= 0:
            print("Sorry, only choose a number between 1 and 9")
        else:
            break

    perm_list = consider_number(infix)
    all_perms = generate_all_permutations(perm_list)
    for p in all_perms:
        print(p)
if __name__ == "__main__":
    main()
