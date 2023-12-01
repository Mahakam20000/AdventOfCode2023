""" --- Part Two ---
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values? """

def calculate_sum(input):
    """
        input: a string \n divided

        output: a number representing the sum of the numbers thus calculated:
                for every line in the input file, join the first and the last 
                digit
    """
    sum = 0
    for line in input.splitlines():
        number = ""
        for char in line:
            if char.isdigit():
                    number += char
                    break
        for char in line[::-1]:
            if char.isdigit():
                    number += char
                    break
        sum += int(number)
    return sum


def substitute_words_with_numbers(lines):
    """
        input: a list of strings

        output: a list of strings where each string from input is edited 
                sustituting the words rappresenting numbers with the numbers
                itselfs

        Using a dictionary to fast substitute the words with the replace 
        function. Due the need of don't brake concatenated strings 
        (i.e.: eightwo, where the "t" is shared between the words "eight" and
        "two") I substitute words using the form <word><number><word>.
        Words in line are checked against this dictionary using the dict's 
        order, so the first check is for "zero", the second for "one" and so on.
        Due this behaviour there is no risk that a digit is duplicated.
    """
    dict = {
        'zero': 'zero0zero',
        'one': 'one1one',
        'two': 'two2two',
        'three': 'three3three',
        'four': 'four4four',
        'five': 'five5five',
        'six': 'six6six',
        'seven': 'seven7seven',
        'eight': 'eight8eight',
        'nine': 'nine9nine'
    }
    out = ""
    for line in lines:
        for key, value in dict.items():
            line = line.replace(key, value)
        out += line
    return out

with open('day_01/input', 'r') as input:
    lines = input.readlines()

new_input = substitute_words_with_numbers(lines)
print(calculate_sum(new_input))