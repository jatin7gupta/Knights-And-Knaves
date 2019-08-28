# Randomly generates a grid with 0s and 1s, whose dimension is controlled by user input,
# as well as the density of 1s in the grid, and determines the size of the largest
# isosceles triangle, consisting of nothing but 1s and whose base can be either
# vertical or horizontal, pointing either left or right or up or down.
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randint
import sys


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(len(grid))))


def size_of_largest_isosceles_triangle():
    result_size = 0
    size = 0
    # top down
    for m in range(10):
        for n in range(10):
            size = 0
            if grid[m][n] > 0:
                size += 1
                if m + 1 < 10:
                    for i in range(m+1, 10):
                        if grid[i][n] > 0:
                            if 0 <= n - size < 10 and 0 <= n + size < 10:
                                c = 0
                                for j in range(n-size, n + size + 1):
                                    if grid[i][j] > 0:
                                        c += 1
                                    else:
                                        break
                                if c == (2*size)+1:
                                    size += 1
                                else:
                                    break
                            else:
                                break
                        else:
                            break
            if size > result_size:
                result_size = size
    # bottom up
    for m in range(9, -1, -1):
        for n in range(9, -1, -1):
            size = 0
            if grid[m][n] > 0:
                size += 1
                if m - 1 >= 0:
                    for i in range(m-1, -1, -1):
                        if grid[i][n] > 0:
                            if 0 <= n - size < 10 and 0 <= n + size < 10:
                                c = 0
                                for j in range(n-size, n+size+1):
                                    if grid[i][j] > 0:
                                        c += 1
                                    else:
                                        break
                                if c == (2*size)+1:
                                    # print('m,n in size',m,n,size+1)
                                    size += 1
                                else:
                                    break
                            else:
                                break
                        else:
                            break
            if size > result_size:
                result_size = size
    for m in range(10):
        for n in range(10):
            size = 0
            if grid[m][n] > 0:
                size += 1
                if n + 1 < 10:
                    for j in range(n+1, 10):
                        if grid[m][j] > 0:
                            if 0 <= m - size < 10 and 0 <= m + size < 10:
                                c = 0
                                for i in range(m-size, m+size+1):
                                    if grid[i][j] > 0:
                                        c += 1
                                    else:
                                        break
                                if c == (2*size)+1:
                                    size += 1
                                else:
                                    break
                            else:
                                break
                        else:
                            break
            if size > result_size:
                result_size = size
    for m in range(10):
        for n in range(9, -1, -1):
            size = 0
            if grid[m][n] > 0:
                size += 1
                if n-1 >= 0:
                    for j in range(n-1, -1, -1):
                        if grid[m][j] > 0:
                            if 0 <= m-size < 10 and 0 <= m+size < 10:
                                c = 0
                                for i in range(m-size, m+size+1):
                                    if grid[i][j] > 0:
                                        c += 1
                                    else:
                                        break
                                if c == (2*size)+1:
                                    size += 1
                                else:
                                    break
                            else:
                                break
                        else:
                            break
            if size > result_size:
                result_size = size

    return result_size
    # REPLACE pass WITH YOUR CODE

# POSSIBLY DEFINE OTHER FUNCTIONS


try:
    arg_for_seed, density = (abs(int(x)) for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
grid = [[randint(0, density) for _ in range(10)] for _ in range(10)]
print('Here is the grid that has been generated:')
display_grid()
print('The largest isosceles triangle has a size of',
      size_of_largest_isosceles_triangle())
