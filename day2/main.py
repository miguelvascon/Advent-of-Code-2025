import sys

def is_invalid_id(id: str) -> bool:
    size = len(id)
    for i in range(1, (size // 2) + 1):
        if size % i != 0:
            continue
        seq = id[:i]
        invalid = True
        for j in range(i, size, len(seq)):
            if seq != id[j:j + len(seq)]:
                invalid = False
        if invalid:
            return True
    return False


def sum_ids(start: int, end: int) -> int:
    total = 0
    for id in range(start, end):
        if is_invalid_id(str(id)):
            total += id
    return total

def get_ranges(file_path: str) -> list[str]:
    try:
        with open(file_path) as input:
            line = input.readline()
            return line.split(',')

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
    
    ranges = get_ranges(sys.argv[1])

    answer = 0
    for seq in ranges:
        start, end = seq.split('-')
        answer += sum_ids(int(start), int(end) + 1)
    print(f"Number of invalid IDs: {answer}")

if __name__=="__main__":
    main()