import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    parser.add_argument("output_file")
    args = parser.parse_args()

    try:
        with open(args.input_file, "r") as input_file:
            with open(args.output_file, "w") as output_file:
                games = {} # key: game, value: count
                for line in input_file:
                    lists = line.strip("\n").split("|")
                    game_number = int(lists[0].split(":")[0].split()[-1])
                    add_to_game_count_dictionary(game_number, games)
                    copies = games.get(game_number)
                    numbers = {}
                    for number in lists[0].split(":")[1].strip().split():
                        numbers[number] = True        
                    
                    matches = 0
                    for number in lists[1].strip().split():
                        if numbers.get(number):
                            matches += 1
                    for i in range(1, matches + 1):
                        for _ in range(copies):
                            add_to_game_count_dictionary(int(game_number) + i, games)
                total_games = 0
                for count in games.values():
                    total_games += count
                print(total_games)
                output_file.write(str(total_games))
    except FileNotFoundError:
        print("File does not exist.")
    except:
        print("Something went wrong.")

def add_to_game_count_dictionary(game_number, games):
    if count := games.get(game_number):
        games[game_number] = count + 1
    else:
        games[game_number] = 1


if __name__ == "__main__":
    main()