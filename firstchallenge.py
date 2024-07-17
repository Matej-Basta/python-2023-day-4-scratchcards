import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    args = parser.parse_args()

    try:
        with open(args.input_file, "r") as input_file:
            total_points = 0
            for line in input_file:
                lists = line.strip("\n").split("|")
                numbers = {}
                for number in lists[0].split(":")[1].strip().split():
                    numbers[number] = True        
                has_points = False
                points = 0
                for number in lists[1].strip().split():
                    if numbers.get(number):
                        print(number)
                        if has_points:
                            points *= 2
                        else:
                            points = 1
                            has_points = True
                print(points)    
                total_points += points
            print(total_points)

    except FileNotFoundError:
        print("File does not exist.")
    except:
        print("Something went wrong.")


if __name__ == "__main__":
    main()