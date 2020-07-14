from util import Stack, Queue

def has_parents(ancestors, node):
    children = set()
    for parent, child in ancestors:
        children.add(child)
    if node in children:
        return True 
    return False

def earliest_ancestor(ancestors, starting_node):
    q = Queue()
    visited = set()
    most_recent = []
    
    # makes sure that node has ancestors
    # if no parents return -1 per instructions
    if has_parents(ancestors, starting_node) is False:
        return -1
    
    # enqueue the starting node
    q.enqueue(starting_node)
    
    while q.size() > 0:
        v = q.dequeue()
        print(f"Current node {v}")