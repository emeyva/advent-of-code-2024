import regex as re

"""Solution to Day 3 of Advent of Code 2024"""

FILENAME = 'input.txt'

def get_file_content():
    file_text = ''
    with open(FILENAME, 'r') as filename:
        file_text = filename.read()
    
    return file_text

def apply_regex(text):
    regex = r'mul\([0-9]{1,3}\,[0-9]{1,3}\)'
    matches = re.findall(regex, text)

    return matches

def calculate_sum(matches):
    sum = 0
    for match in matches:
        first_value, second_value = match.replace('mul(','').replace(')','').split(',')
        sum += int(first_value) * int(second_value)

    return sum

def validate_text(text):
    sum_two = 0
    matches = text.split("don't()")
    valid_matches = []
    valid_matches.append(matches[0])

    for match in matches[1:]:
        new_match = match.split("do()")
        if(len(new_match) > 1):
            valid_matches.append(new_match[1:])

    for valid_text in valid_matches:
        regex_parts = apply_regex(str(valid_text))
        sum_mul = calculate_sum(regex_parts)
        sum_two += sum_mul

    return sum_two

def main():
    print("Day 3 - Advent of Code")
    
    # part 1
    text = get_file_content()
    matches = apply_regex(text)
    sum_mul = calculate_sum(matches)

    print(f"part-one sum: {sum_mul}")

    # part 2
    second_sum = validate_text(text)
    print(f"part-two sum: {second_sum}")


if(__name__=='__main__'):
    main()