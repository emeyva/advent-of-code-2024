"""Solution to Day 2 of Advent of Code 2024"""

FILENAME = 'input.txt'

def create_multi_array():
    multi_array = []
    with open(FILENAME, 'r') as location_ids:
        for line in location_ids:
            line_array = line.replace('\n','').split(' ')
            multi_array.append(line_array)

    print(f"number of arrays:{len(multi_array)}")
    return multi_array

def validate_arrays_part_one(multi_array):
    safe_reports = 0
    for array in multi_array:
        safe = 1
        if(int(array[0]) > int(array[1])):
            for index in range(0, len(array)-1):
                diff_levels = abs(int(array[index])-int(array[index+1]))
                if not (diff_levels > 0 and diff_levels < 4 and (int(array[index])>int(array[index+1]))):
                    safe = 0
        elif(int(array[0]) < int(array[1])):
            for index in range(0, len(array)-1):
                
                diff_levels = abs(int(array[index])-int(array[index+1]))
                if not (diff_levels > 0 and diff_levels < 4 and (int(array[index]) < int(array[index+1]))):
                    safe = 0
        else: 
            safe = 0
        safe_reports += safe

    return safe_reports


def validate_arrays_part_two(multi_array):
    safe_reports = 0
    for array in multi_array:
        safe = 1
        for pos in range(0, len(array)):
            short_array = array[:pos] + array[pos+1:]
            safe = 1
            for index in range(0, len(short_array)-1):
                if(int(short_array[0]) > int(short_array[1])):
                    for index in range(0, len(short_array)-1):
                        diff_levels = abs(int(short_array[index])-int(short_array[index+1]))
                        if not (diff_levels > 0 and diff_levels < 4 and (int(short_array[index])>int(short_array[index+1]))):
                            safe = 0
                elif(int(short_array[0]) < int(short_array[1])):
                    for index in range(0, len(short_array)-1):
                        
                        diff_levels = abs(int(short_array[index])-int(short_array[index+1]))
                        if not (diff_levels > 0 and diff_levels < 4 and (int(short_array[index]) < int(short_array[index+1]))):
                            safe = 0
                else: 
                    safe = 0
            if safe == 1:
                safe_reports += safe
                break
    return safe_reports

def main():
    print("Day 2 - Advent of Code")
    
    # part 1
    multi_array = create_multi_array()
    safe_reports_part_one = validate_arrays_part_one(multi_array)
    print(f"safe reports - part 1: {safe_reports_part_one}")
    # part 2
    safe_reports_part_two = validate_arrays_part_two(multi_array)
    print(f"safe reports - part 2: {safe_reports_part_two}")

if(__name__=='__main__'):
    main()