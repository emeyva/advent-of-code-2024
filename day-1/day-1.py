"""Solution to Day of Advent of Code 2024"""

FILENAME = 'input.txt'

def create_list():
    list_left = []
    list_right = []
    with open(FILENAME, 'r') as location_ids:
        for line in location_ids:
            line_array = line.replace('\n','').split('   ')
            list_left.append(int(line_array[0]))
            list_right.append(int(line_array[1]))
    print(f"list_left:{sorted(list_left)}")
    print(f"list_right:{sorted(list_right)}")
    return list_left, list_right

def sum_of_difference(list_left, list_right):
    size = len(list_left)
    difference_sum = 0

    for number in range(0, size):
        difference_sum += abs(list_left[number] - list_right[number])

    return difference_sum

def sum_of_simmilarities(list_left, list_right):
    size = len(list_left)
    simmilarities_sum = 0

    for number_left in range(0, size):
        count_same_number = 0
        for number_right in range(0, size):
            if(list_left[number_left] == list_right[number_right]):
                count_same_number += 1
        simmilarities_sum += list_left[number_left]*count_same_number

    return simmilarities_sum



def solve_part_one(list_left, list_right):
    difference_sum = sum_of_difference(sorted(list_left), sorted(list_right))
    print(f"Sum of distances: {difference_sum}")

def solve_part_two(list_left, list_right):
    simmilarites_sum = sum_of_simmilarities(sorted(list_left), sorted(list_right))
    print(f"Sum of simmilarities: {simmilarites_sum}")

def main():
    print("Day 1 - Advent of Code")
    list_left, list_right = create_list()
    
    # part 1
    solve_part_one(list_left, list_right)

    # part 2
    solve_part_two(list_left, list_right)




if(__name__=='__main__'):
    main()