"""Solution to Day 4 of Advent of Code 2024"""

FILENAME = "input.txt"
TARGET_WORD = "XMAS"
TARGET_WORD_2 = "X-MAS"
DIRECTIONS = [
    (0, 1),  # Horizontal right
    (0, -1),  # Horizontal left
    (1, 0),  # Vertical down
    (-1, 0),  # Vertical up
    (1, 1),  # Diagonal down-right
    (-1, -1),  # Diagonal up-left
    (1, -1),  # Diagonal down-left
    (-1, 1),  # Diagonal up-right
]


def _get_grid_list():
    grid_list = []
    with open(FILENAME, "r") as filename:
        grid_list = [list(line.strip()) for line in filename.readlines()]

    return grid_list


def _find_xmas_word(grid_list):
    rows, cols = len(grid_list), len(grid_list[0])
    word_len = len(TARGET_WORD)
    count = 0

    def _check_direction(r, c, row_step, col_step):
        for i in range(word_len):
            nr, nc = r + i * row_step, c + i * col_step
            if (
                not (0 <= nr < rows and 0 <= nc < cols)  # boundaries
                or grid_list[nr][nc] != TARGET_WORD[i]  # correct letter
            ):
                return False
        return True

    for r in range(rows):
        for c in range(cols):
            for row_step, col_step in DIRECTIONS:
                if _check_direction(r, c, row_step, col_step):
                    count += 1

    return count


def _find_x_mas_word(grid_list):
    rows, cols = len(grid_list), len(grid_list[0])
    count = 0

    def _is_x_mas(r, c):
        if r + 2 >= rows or c + 2 >= cols:  # out of bound
            return False

        return (
            (
                grid_list[r][c] == "M"
                and grid_list[r][c + 2] == "S"
                and grid_list[r + 1][c + 1] == "A"
                and grid_list[r + 2][c] == "M"
                and grid_list[r + 2][c + 2] == "S"
            )
            or (
                grid_list[r][c] == "S"
                and grid_list[r][c + 2] == "M"
                and grid_list[r + 1][c + 1] == "A"
                and grid_list[r + 2][c] == "S"
                and grid_list[r + 2][c + 2] == "M"
            )
            or (
                grid_list[r][c] == "M"
                and grid_list[r][c + 2] == "M"
                and grid_list[r + 1][c + 1] == "A"
                and grid_list[r + 2][c] == "S"
                and grid_list[r + 2][c + 2] == "S"
            )
            or (
                grid_list[r][c] == "S"
                and grid_list[r][c + 2] == "S"
                and grid_list[r + 1][c + 1] == "A"
                and grid_list[r + 2][c] == "M"
                and grid_list[r + 2][c + 2] == "M"
            )
        )

    for r in range(rows):
        for c in range(cols):
            if _is_x_mas(r, c):
                count += 1

    return count


def main():
    print("Day 4 - Advent of Code")

    # part 1
    grid_list = _get_grid_list()
    num_occurences = _find_xmas_word(grid_list)
    print(f"part1\n{TARGET_WORD} ocurences:\n{num_occurences}")

    # part 2
    x_mas_occurences = _find_x_mas_word(grid_list)
    print(f"\npart2\n{TARGET_WORD} X ocurences:\n{x_mas_occurences}")


if __name__ == "__main__":
    main()
