
def _check_direction_tiny(check_me, direction):

    for i in range(len(check_me) - 1):
        if check_me[i] < check_me[i + 1] and direction == 1:
            continue
        elif check_me[i] > check_me[i + 1] and direction == -1:
            continue

        return i

    return -1


def _check_direction(check_me):

    valid = []

    directions = [1, -1]
    for direction in directions:
        res = _check_direction_tiny(check_me, direction)
        if res == -1:
            print(f"direction worked - {check_me}")
            valid.append(check_me)
        else:
            print(f"direction failed - {check_me}")

        for i in range(len(check_me)):
            check_popped = check_me.copy()
            x = check_popped.pop(i)
            if _check_direction_tiny(check_popped, direction) == -1:
                print(f"direction worked - popped: {x} - {check_popped}")
                valid.append(check_popped)
            else:
                print(f"direction failed - popped: {x} - {check_popped}")

    return valid

def _check_delta_tiny(check_me):
    for i in range(len(check_me) - 1):
        delta = abs(check_me[i] - check_me[i + 1])
        if delta < 4 and delta > 0:
            continue
        return i
    return -1


def _check_delta(valid):
    safe = []
    for check_me in valid:
        res = _check_delta_tiny(check_me)
        if res == -1:
            print(f"delta worked - {check_me}")
            safe.append(check_me)
        else:
            print(f"delta failed - {check_me}")

    for check_me in valid:
        for i in range(len(check_me)):
            check_popped = check_me.copy()
            x = check_popped.pop(i)
            if _check_delta_tiny(check_popped) == -1:
                print(f"delta worked - popped: {x} - {check_popped}")
                safe.append(check_popped)
            else:
                print(f"delta failed - popped: {x} - {check_popped}")

    return safe

def main():

    entire_list = []
    with open('data/input_two.txt', 'r') as file:
        for line in file:
            values = line.split()
            values = [int(x) for x in values]
            entire_list.append(values)

    total = 0

    for i in range(len(entire_list)):
        print(f"************************************************* checking: {i}")
        check = entire_list[i]
        original = check.copy()

        valid = _check_direction(check)

        safe = _check_delta(valid)

        check_len = len(check)
        good = False
        for candidate in safe:
            candidate_len = len(candidate)
            if candidate_len >= check_len-1:
                print(f"good: {i} - {original} - {candidate}")
                good = True

        if good:
            total = total + 1

        if not good:
            print(f"bad: {i} - {original}")
            continue

    print(total)


if __name__ == '__main__':
    main()
