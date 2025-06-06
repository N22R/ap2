from collections import defaultdict, deque


def read_input(file_name):
    dependencies = defaultdict(list)
    in_degree = defaultdict(int)

    with open(file_name, 'r') as f:
        for line in f:
            doc, required_doc = line.strip().split()
            dependencies[required_doc].append(doc)
            in_degree[doc] += 1
            if required_doc not in in_degree:
                in_degree[required_doc] = 0

    return dependencies, in_degree


def sort(dependencies, in_degree):
    queue = deque()
    result = []

    for doc in in_degree:
        if in_degree[doc] == 0:
            queue.append(doc)

    while queue:
        doc = queue.popleft()
        result.append(doc)

        for dependent_doc in dependencies[doc]:
            in_degree[dependent_doc] -= 1
            if in_degree[dependent_doc] == 0:
                queue.append(dependent_doc)

    return result


def main():
    input_file = 'govern.in'
    output_file = 'govern.out'

    dependencies, in_degree = read_input(input_file)
    sorted_docs = sort(dependencies, in_degree)

    with open(output_file, 'w') as f:
        for doc in sorted_docs:
            f.write(doc + '\n')


if __name__ == "__main__":
    main()