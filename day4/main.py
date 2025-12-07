import numpy as np
import sys

def check_adjacent(row: int, col: int, rows: int, cols: int) -> bool:
    if row == 0 and col == 0:
        return True
    elif row == 0 and col == cols - 1:
        return True
    elif row == rows - 1 and col == 0:
        return True
    elif row == rows - 1 and col == cols - 1:
        return True

    return False

def count_accessable_rolls(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    result = 0

    for row in range(rows):
        for col in range(cols):
            fewer_than_four = check_adjacent(row, col, rows, cols)
            if fewer_than_four:
                result += 1

    return result

def create_matrix(file_path: str) -> np.ndarray:
    try:
        lines = []
        with open(file_path) as input:
            for line in input:
                lines.append(list(line.strip()))
        return np.array(lines)

    except FileNotFoundError:
        print("ERROR: Unable to open file.")
        exit(2)
    except ValueError:
        print("Error: File contains invalid data format")
        exit(2)

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py [path-to-file]")
        exit(1)

    matrix = create_matrix(sys.argv[1])
    answer = count_accessable_rolls(matrix)
    print(f"{answer} rolls are accessable by the forklift")

if __name__ == "__main__":
    main()
