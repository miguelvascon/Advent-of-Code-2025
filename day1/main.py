import sys

def calculate_passthroughs(direction, clicks, index):
    count = clicks // 100
    remainder = clicks % 100
    if direction == "R":
        if index + remainder >= 100:
            count += 1
    else:
        if index > 0 and remainder >= index:
            count += 1
    return count

def rotate_dial(file_path):
    try:
        with open(file_path) as input:
            result = 0
            index = 50

            for line in input:
                direction = line[0]
                clicks = int(line[1:])
                result += calculate_passthroughs(direction, clicks, index)
                index = (index + clicks) % 100 if direction == "R" else (index - clicks + 100) % 100

            return result

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

    answer = rotate_dial(sys.argv[1])
    print(f"The dial pointed at zero {answer} times.")

if __name__=="__main__":
    main()