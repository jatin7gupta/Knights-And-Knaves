# Prompts the user for a positive integer that codes a set S as follows:
# - Bit 0 codes 0
# - Bit 1 codes -1
# - Bit 2 codes 1
# - Bit 3 codes -2
# - Bit 4 codes 2
# - Bit 5 codes -3
# - Bit 6 codes 3
# ...
# Computes a derived positive integer that codes the set of running sums
# ot the members of S when those are listed in increasing order.
#
# Written by *** and Eric Martin for COMP9021


from itertools import accumulate
import sys

try:
    encoded_set = int(input('Input a positive integer: '))
    if encoded_set < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()


def logic_function(num):
    # num = encoded_set
    bin_num = bin(num)[2:]
    rev_num = bin_num[::-1]
    x = 1
    list_of_ints = [0]
    for _ in range(len(bin_num) // 2 + 1):
        list_of_ints.append(-x)
        list_of_ints.append(x)
        x += 1
    result_set = set()
    for i in range(len(rev_num)):
        if rev_num[i] == '1':
            result_set.add(list_of_ints[i])
    return result_set


def print_sorted_set(s):
    list_of_set = list(sorted(s))
    print('{', end='')
    for l in range(len(list_of_set)):
        if l == len(list_of_set) - 1:
            print(list_of_set[l], end='')
            print('}')
        else:
            print(list_of_set[l], end='')
            print(',', end=' ')


# POSSIBLY DEFINE OTHER FUNCTIONS
def display_encoded_set(encoded_set):
    result_set = logic_function(encoded_set)
    print_sorted_set(result_set)
    # REPLACE pass ABOVE WITH CODE TO PRINT OUT ENCODED SET (WITH print() STATEMENTS)


def code_derived_set(encoded_set):
    encoded_running_sum = 0
    sum_set = set()
    # REPLACE THIS COMMENT WITH YOUR CODE
    result_set = logic_function(encoded_set)
    result_list = list(sorted(result_set))
    for i in range(len(result_list)+1):
        s = 0
        if i == 0:
            s = result_list[i]
        for j in range(i):
            s = s + result_list[j]
        sum_set.add(s)
    sum_list = list(sorted(sum_set))
    for e in sum_list:
        if e >= 0:
            encoded_running_sum += 2**(2*e)
        elif e < 0:
            encoded_running_sum += 2**((-2*e)-1)
    return encoded_running_sum


print('The encoded set is: ', end='')
display_encoded_set(encoded_set)
encoded_running_sum = code_derived_set(encoded_set)
print('The derived encoded set is: ', end='')
display_encoded_set(encoded_running_sum)
print('  It is encoded by:', encoded_running_sum)
