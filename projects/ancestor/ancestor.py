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
        
        # if we haven't visited the current node, add it to the set
        if v not in visited:
            visited.add(v)

            # if node has a parent:
            if has_parents(ancestors, v):
                # clear the recent list
                most_recent.clear()
                
                # enqueue the current node's parent and add it to the most recent list
                for parent, child in ancestors:
                    if child == v:
                        q.enqueue(parent)
                        print(f"queue {parent} as the parent of {v}")
                        most_recent.append(parent)
                print()
            else:
                print(f"{v} has no parents\n")
    return min(most_recent)