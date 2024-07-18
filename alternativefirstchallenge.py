import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    args = parser.parse_args()

    try:
        with open(args.input_file, "r") as input_file:
            total = 0
            for line in input_file:
                win_numbers, actual_numbers = line.split("|")
                win_numbers = win_numbers.split(":")[1]
                intersection = set(win_numbers.split()) & set(actual_numbers.split())
                if intersection:
                    total += 2 ** (len(intersection) - 1)
            print(total)
                    
    except FileNotFoundError:
        raise Exception("The file does not exist.")
    except:
        raise Exception("Something went wrong.")

if __name__ == "__main__":
    main()