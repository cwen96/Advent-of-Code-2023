import re


def q1():
    with open("input.txt", mode="r") as f:
        input = f.readlines()
        max_red = 12
        max_green = 13
        max_blue = 14
        sum_valid_ids = 0

    # Sum game ID if the game is valid for all colours
    for i in range(len(input)):
        if isValidGame(r"\br\w+", input, i, max_red) and isValidGame(r"\bg\w+", input, i, max_green) and isValidGame(r"\bb\w+", input, i, max_blue):
            sum_valid_ids += i + 1

    return sum_valid_ids


def isValidGame(regex, input, i, max_num_colour):
    # Regex to find the position of each colour
    position = re.finditer(regex, input[i])

    # Iterate over each position to get the amount of regex colour
    for iter in position:
        regex_index = iter.span()[0]
        # Construct two digit integer
        tens = "0"
        ones = input[i][regex_index - 2]
        # If the number has 2 digits, update the tens digit
        if input[i][regex_index - 3].isdigit():
            tens = input[i][regex_index - 3]
        # If the value exceeds the maximum amount possible
        if int(tens + ones) > max_num_colour:
            return False
    return True


def main():
    print(f"Q1 ans: {q1()}\n")


if __name__ == "__main__":
    main()
