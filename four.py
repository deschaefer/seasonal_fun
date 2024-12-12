
def read_array(filename):

    rval = []
    with open(filename, 'r') as file:
        for line in file:
            row = list(line.strip())
            rval.append(row)

    return rval


def get_subset(row, col, size, data):
    # adjust
    top_left_row = row - 1
    top_left_col = col - 1

    subset = []
    for i in range(size):
        # Check for index bounds
        if top_left_row + i < len(data):
            row = []
            for j in range(size):
                if (top_left_row+i) < 0 or (top_left_col+j) < 0:
                    row.append('+')
                elif top_left_col + j < len(data[top_left_row + i]):
                    row.append(data[top_left_row + i][top_left_col + j])
                else:
                    row.append(None)  # Fill with None if out of bounds
            subset.append(row)
        else:
            subset.append([None] * size)  # Fill with None if out of bounds
    return subset


def read_test_data():

    # tests_names = ['4_ne.txt', 
    #                '4_n.txt', 
    #                '4_s.txt', 
    #                '4_w.txt', 
    #                '4_nw.txt', 
    #                '4_se.txt', 
    #                '4_sw.txt', 
    #                '4_e.txt']

    tests_names = ['xmas_1.txt', 'xmas_2.txt', 'xmas_3.txt', 'xmas_4.txt']

    # read in the test data sets
    test_data = []
    for test_name in tests_names:
        input_data = read_array('data/'+test_name)
        test_data.append(input_data)

    for test_set in test_data:
        for row in test_set:
            print(row)
        print('-------------------')    

    return test_data


def main():

    match_count = 0

    test_data = read_test_data()

    subset_size = 3

    filename = 'data/input_4.txt'
    input_data = read_array(filename)

    for x in range(len(input_data)):
        for y in range(len(input_data[x])):

            subset = get_subset(x, y, subset_size, input_data)

            print(f"{x} x {y} Subset:")
            for row in subset:
                print(row)

            for test_set in test_data:
                match = True
                for i in range(len(test_set)):
                    for j in range(len(test_set[i])):
                        test_value = test_set[i][j]
                        if test_value != ".":
                            input_value = subset[i][j]
                            if test_value != input_value:
                                match = False
                if match:
                    print('matching test set')
                    for row in test_set:
                        print(row)
                    match_count += 1
                    print(f'Match found {match_count}')

    print(f"Match count: {match_count}")


if __name__ == '__main__':
    main()
