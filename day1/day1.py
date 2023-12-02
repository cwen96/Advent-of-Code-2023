def q1():
    nums = []

    with open("input.txt", mode="r") as f:
        input = f.readlines()

    for string in input:
        digit = ""
        i = 0
        while i < len(string) and len(digit) == 0:
            if string[i].isdigit():
                digit += string[i]
            i += 1

        i = len(string) - 1
        while i >= 0 and len(digit) == 1:
            if string[i].isdigit():
                digit += string[i]
            i -= 1

        if len(digit) > 0:
            nums.append(int(digit))

    return sum(nums)

def q2():
    word_to_num = {
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9
    }

    word_to_num_bw = {
        "eno" : 1,
        "owt" : 2,
        "eerht" : 3,
        "ruof" : 4,
        "evif" : 5,
        "xis" : 6,
        "neves" : 7,
        "thgie" : 8,
        "enin" : 9
    }

    nums = []

    with open("input.txt", mode="r") as f:
        input = f.readlines()

    for string in input:
        digit = ""
        
        word = ""
        i = 0
        while i < len(string) and len(digit) == 0:
            if string[i].isalpha():
                matched = 0
                word += string[i]
                for key_word in word_to_num.keys():
                    if key_word.find(word) != -1:
                        matched = 1
                        if len(digit) == 0 and word in word_to_num.keys():
                            digit += str(word_to_num[key_word])
                            break
                if matched == 0:
                    word = word[1:]
            elif string[i].isdigit():
                digit += string[i]
            i += 1

        word = ""
        i = len(string) - 1
        while (i >= 0 and len(digit) == 1):
            if string[i].isalpha():
                matched = 0
                word += string[i]
                for key_word in word_to_num_bw.keys():
                    if key_word.find(word) != -1:
                        matched = 1
                        if len(digit) == 1 and word in word_to_num_bw.keys():
                            digit += str(word_to_num_bw[key_word])
                            break
                if matched == 0:
                    word = word[1:]
            elif string[i].isdigit():
                digit += string[i]
            i -= 1

        if len(digit) > 0:
            nums.append(int(digit))
    print(nums[839])
    return sum(nums)



def main():
    print(f"Q1 ans: {q1()}")
    print(f"Q2 ans: {q2()}")



if __name__ == "__main__":
    main()
