import networkx as nx

'''
Converts input datastructure to Network X Graph
'''
def getNXgraph(dag):
    if not isinstance(dag, nx.classes.digraph.DiGraph):
        try:
            dag = nx.DiGraph(dag)
        except nx.NetworkXError:
            print 'NetworkXError: Could not convert to NetworkX DiGraph'
        except:
            raise
    
    return dag

'''
* Function to find a set S that satisfies the backdoor condition for dag G
* A backdoor path is an undirected path b/w X and Y with an arrow into X
* S satisfies back-door criterion when
  - S blocks every back-door path from X to Y
  - no node in S is a descendant of X
----------------------------------------------------------------------------
    dag - should be either adjancency list or networkx digraph
    Returns parents of X
'''
def backdoor(dag, x, y):
    # converting to networkx graph
    dag = getNXgraph(dag)
    
    # return parents of x as they will always satisfy condition
    parents = []
    for node in x:
        parents += dag.predecessors(node)
    return parents

'''
Function to check if a set S that satisfies the backdoor condition for dag G
Brute force algorithm    
    dag - should be either adjancency list or networkx digraph
    x,y,s - sets of nodes
    Returns parents of X
'''
def check_backdoor(dag, x, y, s):
    # converting to networkx graph
    dag = getNXgraph(dag)
    
    all_descendants = []
    for node in x:
        all_descendants += nx.descendants(dag, node)
    
    for node in s:
        if node in all_descendants:
            return False
        
    undir_dag = dag.to_undirected()
    #undir_dag.to_undirected()
    
    all_paths= []
    for start in x:
        for end in y:
            all_paths = nx.all_simple_paths(undir_dag, source=start, target=end)
            for path in all_paths:
                # check if some node from s is in path -> path is blocked
                # this loop might take a lot of time to execute
                value = sum([1 if set_node in path else 0 for set_node in s])
                print 'value = ', value
                if value < 1:
                    return False
        
    return True