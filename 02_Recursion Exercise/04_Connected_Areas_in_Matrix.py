class Area:
    def __init__(self, r, c, s):
        self.row = r
        self.col = c
        self.size = s


rows, cols = int(input()), int(input())
matrix = []

for _ in range(rows):
    matrix.append(list(input()))


def explore_area(r, c, m):
    if r < 0 or c < 0 or r >= len(matrix) or c >= len(matrix[0]):
        return 0
    if m[r][c] != "-":
        return 0

    m[r][c] = "v"

    result = 1

    result += explore_area(r - 1, c, m)
    result += explore_area(r + 1, c, m)
    result += explore_area(r, c - 1, m)
    result += explore_area(r, c + 1, m)

    return result


areas = []

for row in range(rows):
    for col in range(cols):
        size = explore_area(row, col, matrix)
        if size == 0:
            continue
        areas.append(Area(row, col, size))

print(f"Total areas found: {len(areas)}")
for idx, area in enumerate(sorted(areas, key=lambda a: a.size, reverse=True)):
    print(f"Area #{idx + 1} at ({area.row}, {area.col}), size: {area.size}")
