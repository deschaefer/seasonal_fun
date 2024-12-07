


# Function to retrieve a square subset of a specified size from the 2D array
def get_subset(row, col, size, data):
    # adjust
    top_left_row = row - 3
    top_left_col = col - 3

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



def main():

    tests_names = ['4_ne.txt', '4_n.txt', '4_s.txt', '4_w.txt', '4_ne.txt', '4_nw.txt', '4_se.txt', '4_sw.txt', '4_e.txt']

    test_data = []
    for test_name in tests_names:
        input_data = read_array('data/'+test_name)
        test_data.append(input_data)

    for test_set in test_data:
        for row in test_set:
            print(row)
        print('-------------------')

    # Define the filename
    filename = 'input_4_a.txt'

    input_data = read_array(filename)

    # Example: Get a 7x7 subset starting from (1, 1)
    top_left_row = 3  # 2nd row (0-based index)
    top_left_col = 3  # 2nd column (0-based index)
    subset_size = 7   # Size of the subset

    subset = get_subset(top_left_row, top_left_col, subset_size, input_data)

    # Display the subset
    print(f"{subset_size}x{subset_size} Subset:")
    for row in subset:
        print(row)

    for test_set in test_data:
        match = True
        for i in range(len(test_set)):      # Iterate over rows
            for j in range(len(test_set[i])):  # Iterate over columns
                test_value = test_set[i][j]        # Access the value at position (i, j)
                if test_value is not ".":
                    input_value = subset[i][j]
                    if test_value != input_value:
                        match = False
        if match:
            print('Match found')


def read_array(filename):
    # Open the file and read its contents
    rval = []
    with open(filename, 'r') as file:
        for line in file:
            # Strip leading/trailing whitespace and convert the line to a list of characters
            row = list(line.strip())  # Convert the line to a list of characters
            rval.append(row)

    return rval


if __name__ == '__main__':
    main()
