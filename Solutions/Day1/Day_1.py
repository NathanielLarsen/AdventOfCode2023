import re
file = 'input.txt'
instructions = open(file, 'r').read().splitlines()
def indentify_numbers(instructions):
    tot = 0
    new_strings = []
    for instruction in instructions:
        new_strings.append((instruction
                            .replace('one', 'o1e')
                            .replace('two','t2o')
                            .replace('three','t3e')
                            .replace('four','f4r')
                            .replace('five','f5e')
                            .replace('six','s6x')
                            .replace('seven','s7n')
                            .replace('eight','e8t')
                            .replace('nine','n9e')))
    for instruction in new_strings:
        params = list(re.findall('\d', instruction))
        new_param = params[0] + params[-1]
        tot += int(new_param)
    return tot
print("Part 2 Solution:", indentify_numbers(instructions))