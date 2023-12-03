"""--- Part Two ---
The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.

Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?"""



def build_matrix(lines: list[str]) -> list[list[str]]:
    """
        Build a matrix from the input
    """
    matrix_scheme = []
    for row in lines:
        tmp = []
        for e in row.strip():
            tmp.append(e)
        matrix_scheme.append(tmp)
    return matrix_scheme



def find_symbols(matrix_scheme: list[list[str]]) -> list[int]:
    """
        Input: the matrix representing the input

        Output: the list of the numbers near the symbols '*'
    """
    numbers = []
    for r, row in enumerate(matrix_scheme):
        for c, e in enumerate(row):
            if e == '*':
                numbers.append(search_near_digits(r, c))
    return numbers



def search_near_digits(r: int, c: int) -> list[int]:
    """
        Input:
            r: row's number where the symbol is found
            c: column's number where the symbol is found
        
        Output: list of the numbers near the symbol
    """
    ret = []
    if c > 0:
        e = matrix_scheme[r][c-1]
        if e.isdigit():
            ret.append(complete_number(r, c-1))
    if c < r_len-1:
        e = matrix_scheme[r][c+1]
        if e.isdigit():
            ret.append(complete_number(r, c+1))
    if r > 0: # if exists a row on the top of the current
        e = matrix_scheme[r-1][c]
        if e.isdigit():
            ret.append(complete_number(r-1, c))
        else:
            if c > 0:
                e = matrix_scheme[r-1][c-1]
                if e.isdigit():
                    ret.append(complete_number(r-1, c-1))
            if c < r_len-1:
                e = matrix_scheme[r-1][c+1]
                if e.isdigit():
                    ret.append(complete_number(r-1, c+1))
    if r < c_len: # if exists a row on the bottom of the current
        e = matrix_scheme[r+1][c]
        if e.isdigit():
            ret.append(complete_number(r+1, c))
        else:
            if c > 0:
                e = matrix_scheme[r+1][c-1]
                if e.isdigit():
                    ret.append(complete_number(r+1, c-1))
            if c < r_len-1:
                e = matrix_scheme[r+1][c+1]
                if e.isdigit():
                    ret.append(complete_number(r+1, c+1))
    return ret



def complete_number(r: int, c: int) -> int:
    """
        Given the coordinates of a digit in the matrix, returns all the horizontally continuous 
        digits.
    """
    # search for the first digit of the number
    start = c
    while start > 0:
        if matrix_scheme[r][start-1].isdigit():
            start -= 1
        else:
            break
    # search for the last digit of the number
    end = c
    while end < r_len-1:
        if matrix_scheme[r][end+1].isdigit():
            end += 1
        else:
            break
    number = ""
    for i in range(start, end+1):
        number += matrix_scheme[r][i]
    return int(number)



def calculate_gear_ratio(couples: list[list[int]]) -> int:
    couples = [ x for x in numbers if len(x) == 2 ]
    res = 0
    for couple in couples:
        res += couple[0] * couple[1]
    return(res)


with open('day_03/input', 'r') as input:
    l = input.readlines()

matrix_scheme = build_matrix(l)
r_len = len(matrix_scheme[0])
c_len = len(matrix_scheme)

numbers = find_symbols(matrix_scheme)
res = calculate_gear_ratio(numbers)
print(res)
