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

        #initialize queue, path, and visited dictionary to store parent nodes

        visited = {}
        q = Queue()
        path=[]

        q.put(start)
        visited[start] = None

        #while queue is not empty
        while not q.empty():
            curr_node = q.get()
            path.append(curr_node)

            #check if current node is end node
            if curr_node == end:
                path = [curr_node]

                while curr_node != start:
                    curr_node = visited[curr_node]
                    path.append(curr_node)
                return path[::-1]
                            
            
            #loop through neighbors of curent node and check if it's been visited, if not, put in visited and queue
            neighbors = self.graph.neighbors(curr_node)
            for n in neighbors:
                if n not in visited:
                    q.put(n)
                    visited[n] = curr_node
        
        #if end not reached, return None. if end not provided, return entire traversal
        if end:
            return None
        else:
            return path







        



        

        







