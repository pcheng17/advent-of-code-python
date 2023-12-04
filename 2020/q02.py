from aocd import get_data


def get_input():
    return get_data(day=2, year=2020)

def parse(input):
    data_list = input.splitlines()
    data = [] 
    for row in data_list:
        x, y, z = row.split()
        a, b = map(int, x.split('-'))
        letter = y[:-1]
        data.append((a, b, letter, z))
    return data

def part_a(input):
    data = parse(input)
    valid = 0
    for a, b, letter, password in input:
        count = password.count(letter)
        if a <= count and count <= b:
            valid += 1
    return valid

def part_b(input):
    data = parse(input)
    valid = 0
    for a, b, letter, password in input:
        if password[a-1] == letter and password[b-1] != letter:
            valid += 1
        elif password[a-1] != letter and password[b-1] == letter:
            valid += 1
    return valid
