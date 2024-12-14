def read_rules():

    filename = "data/input_5_rules.txt"
    rules_map = {}

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            left, right = list(line.split("|"))
            if left in rules_map:
                rules_map[left].append(right)
            else:
                rules_map[left] = [right]

    return rules_map


def read_pages():

    filename = "data/input_5_pages.txt"

    pages = []

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            new_pages = list(line.split(","))
            pages.append(new_pages)

    return pages


def validate_page(rules_map, page):
    for index, chapter in enumerate(page):
        if rules_map.get(chapter) is None:
            continue
        rules = rules_map[chapter]
        for rule in rules:
            try:
                pos = page.index(rule)
                if pos < index:
                    return False, 0
            except ValueError:
                pass
    print(f"pass {page}")
    return True, page[len(page) // 2]


def fix_page(rules_map, page):
    for index, chapter in enumerate(page):
        if rules_map.get(chapter) is None:
            continue
        rules = rules_map[chapter]
        for rule in rules:
            try:
                pos = page.index(rule)
                if pos < index:
                    page[index], page[pos] = page[pos], page[index]
                    return False, 0, page
            except ValueError:
                pass
    print(f"pass {page}")
    return True, page[len(page) // 2], page


def validate(rules_map, pages):
    sum = 0
    for page in pages:
        valid, middle_item = validate_page(rules_map, page)
        if not valid:
            while not valid:
                valid, middle_item, page = fix_page(rules_map, page)
                valid, middle_item = valid, middle_item = validate_page(rules_map, page)
            sum += int(middle_item)
    return sum


def main():
    rules_map = read_rules()
    print(rules_map)
    pages = read_pages()
    print(pages)

    validated = validate(rules_map, pages)
    print(validated)


if __name__ == "__main__":
    main()
