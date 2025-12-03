import sys

def find_max_voltage(bank: str) -> int:
    index = 0
    digits_needed = 12
    size = len(bank)
    max_joltage = ""

    for i in range(digits_needed):
        remaining = digits_needed - 1 - i
        max_index = size - remaining
        window = bank[index:max_index]
        best = max(window)
        max_joltage += best
        relative = window.index(best)
        index += relative + 1

    return int(max_joltage)


def get_banks(file_path: str) -> list[str]:
    try:
        banks = []
        with open(file_path) as input:
            for line in input:
                banks.append(line.strip())
        return banks

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

    banks = get_banks(sys.argv[1])

    answer = 0
    for bank in banks:
        jolatage = find_max_voltage(bank)
        answer += jolatage
    print(f"The total output joltage is {answer}")

if __name__=="__main__":
    main()