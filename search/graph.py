import networkx as nx
from queue import Queue

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """
        #check if start and end nodes exist

        if start not in self.graph:
            return None
        
        if end and end not in self.graph:
            return None

        if len(self.graph) == 0:
            return None

        #initialize queue and add start to visited and queue

        q= Queue(maxsize=0)
        visited =[]
        q.put(start)
        visited.append(start)
        path=[]

        #while queue is not empty
        while not q.empty():
            curr_node = q.get()
            path.append(curr_node)

            #check if end is reached
            if curr_node == end:
                return path
            
            #loop through neighbors of curent node and check if it's been visited, if not, put in visited and queue
            neighbors = self.graph.neighbors(curr_node)
            for n in neighbors:
                if n not in visited:
                    visited.append(n)
                    q.put(n)
        
        #if end not reached, return None. if end not provided, return entire traversal
        if end:
            return None
        else:
            return path







        



        

        







