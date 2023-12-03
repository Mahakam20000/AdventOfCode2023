"""--- Day 3: Gear Ratios ---
You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

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
In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?"""


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



def complete_number(r: int, c: int) -> int:
    """
        Given the coordinates of a digit in the matrix, returns all the horizontally continuous 
        digits.
        Substitute the returned digits with "." to avoid taking the same digit more than once.
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
        matrix_scheme[r][i] = "."
    return int(number)



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
        if c > 0:
            e = matrix_scheme[r+1][c-1]
            if e.isdigit():
                ret.append(complete_number(r+1, c-1))
        if c < r_len-1:
            e = matrix_scheme[r+1][c+1]
            if e.isdigit():
                ret.append(complete_number(r+1, c+1))
    return ret


def find_symbols(matrix_scheme: list[list[str]]) -> list[int]:
    """
        Input: the matrix representing the input

        Output: the list of the numbers near the symbols
    """
    numbers = []
    for r, row in enumerate(matrix_scheme):
        for c, e in enumerate(row):
            if not e.isdigit() and e != ".":
                numbers += search_near_digits(r, c)
    return numbers



with open('day_03/input', 'r') as input:
    l = input.readlines()

matrix_scheme = build_matrix(l)
r_len = len(matrix_scheme[0])
c_len = len(matrix_scheme)

numbers = find_symbols(matrix_scheme)
res = sum(numbers)
print(res)
