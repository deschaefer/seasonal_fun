import re


def main():

    pattern = r"mul\((-?\d+),(-?\d+)\)"

    total = 0
    big_line = ""
    with open('data/input_3.txt', 'r') as file:
        for line in file:
            big_line = big_line + line

    dont_list = big_line.split("don't()")

    # the first don't is actually a do
    matches = re.findall(pattern, dont_list[0])
    for match in matches:
        val = int(match[0]) * int(match[1])
        print(f"{val}")
        total += val

    dont_list.pop(0)

    for dont in dont_list:
        print(f"Dont: {dont}")
        do_list = dont.split("do()")
        # the first is a dont
        do_list.pop(0)
        for do in do_list:
            matches = re.findall(pattern, do)
            for match in matches:
                val = int(match[0]) * int(match[1])
                print(f"{val}")
                total += val

    print(f"Total: {total}")
if __name__ == '__main__':
    main()
