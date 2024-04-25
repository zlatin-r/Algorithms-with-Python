rows, cols = int(input()), int(input())


def find_all_paths(row, col):
    if row > rows - 1 or col > cols - 1:
        return 0

    if row == rows - 1 and col == cols - 1:
        return 1

    result = 0

    result += find_all_paths(row, col + 1)
    result += find_all_paths(row + 1, col)

    return result


print(find_all_paths(0, 0))
