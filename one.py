


def main():
    list1 = []
    list2 = []

    with open('data/input.txt', 'r') as file:
        for line in file:
            val1, val2 = line.split()
            list1.append(int(val1))
            list2.append(int(val2))

    total = 0

    for i in range(len(list1)):
        appearances = list2.count(list1[i])
        value = appearances * list1[i]
        total += value

    print(total)


if __name__ == '__main__':
    main()
