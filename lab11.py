class TreeNode:
    def __init__(self, name):
        self.name = name
        self.parent = None


def find_lca(node1, node2):
    visited = set()
    # Поднимаемся от node1 к корню и записываем все пройденные узлы
    while node1 is not None:
        visited.add(node1)
        node1 = node1.parent
    # Поднимаемся от node2 к корню и ищем первый общий узел с node1
    while node2 not in visited:
        node2 = node2.parent

    return node2.name


if __name__ == "__main__":
    n = int(input())-1 #Подсчёт с нуля
    people = {}
    for _ in range(n):
        line = input().split()
        child_name = line[0]
        parent_name = line[1] if len(line) > 1 else None

        if child_name not in people:
            people[child_name] = TreeNode(child_name)
        if parent_name and parent_name not in people:
            people[parent_name] = TreeNode(parent_name)
        if parent_name:
            people[child_name].parent = people[parent_name]

    q = int(input())
    queries = []
    for _ in range(q):
        query = input().split()
        queries.append(query)

    for query in queries:
        person1_name, person2_name = query
        person1 = people[person1_name]
        person2 = people[person2_name]
        lca = find_lca(person1, person2)
        print(lca)
