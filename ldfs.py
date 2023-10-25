from queue import LifoQueue
from puzzle import Puzzle

def limited_deep_first_search(initial_state, max_depth):
    start_node = Puzzle(initial_state, None, None, 0)
    stack = LifoQueue()
    stack.put((start_node, 0))  # Починаємо з кореневого вузла і глибини 0
    while not stack.empty():
        node, depth = stack.get()
        if depth > max_depth:
            continue  # Пропускаємо вузли глибше за max_depth
        if node.goal_test():
            return node.find_solution()
        if depth < max_depth:
            children = node.generate_child()
            for child in children:
                stack.put((child, depth + 1))
    return None  # Розв'язок не знайдено