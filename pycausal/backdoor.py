import networkx as nx

'''
Function to find a set S that satisfies the backdoor condition for dag G
    dag - should be either adjancency list or networkx digraph
    Returns parents of X
'''
def backdoor(dag, x, y):
    # converting to networkx graph
    if not isinstance(dag, nx.classes.digraph.DiGraph):
        dag = nx.DiGraph(dag)
    # return parents of x as they will always satisfy condition
    parents = []
    for node in x:
        parents += dag.predecessors(node)
    return parents

'''
Function to check if a set S that satisfies the backdoor condition for dag G
    dag - should be either adjancency list or networkx digraph
    x,y,s - sets of nodes
    Returns parents of X
'''
def check_backdoor(dag, x, y, s):
    # converting to networkx graph
    if not isinstance(dag, nx.classes.digraph.DiGraph):
        dag = nx.DiGraph(dag)
    
    all_descendants = []
    for node in x:
        all_descendants += nx.descendants(dag, node)
    
    for node in s:
        if node in all_descendants:
            return False
        
    all_paths = nx.all_simple_paths(dag.to_undirected(), x, y)
    for path in all_paths:
        # check if some node from s is in path -> path is blocked
        # this loop might take a lot of time to execute
        value = sum([1 if set_node in path else 0 for set_node in s])
        if value < 1:
            return False
        
    return True