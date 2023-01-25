# write tests for bfs
import pytest
from search import graph

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    
    g = graph.Graph("./data/tiny_network.adjlist")
    traversal = g.bfs("Michael Keiser")

    #check traversal of nodes
    assert traversal == ['Michael Keiser', '33232663', 'Charles Chiu', 'Martin Kampmann', 
                        '33242416', '33483487', '32790644', '31806696', '31626775', '31540829', 
                        'Atul Butte', 'Luke Gilbert', 'Steven Altschuler', 'Lani Wu', 'Neil Risch', 'Nevan Krogan', 
                        '33765435', '31395880', '30944313', '32036252', '32042149', '30727954', '29700475', '34272374', '32353859', 
                        'Marina Sirota', 'Hani Goodarzi', 'Michael McManus', '31486345', '32025019']

    #check right number of nodes
    assert len(traversal) == 30

def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    
    g = graph.Graph("./data/citation_network.adjlist")

    shortestpath = g.bfs('Lani Wu', 'Atul Butte')

    assert shortestpath == ['Lani Wu', '30727954', 'Michael McManus', '32025019', 'Atul Butte']

    #check path length
    assert len(shortestpath) == 5

    #edge case 1: run bfs from a start node that does not exist in graph

    missing_start = g.bfs('Jennifer Coolidge')
    assert missing_start == None

    #edge case 2: run bfs search for an end node that doesn't exist in graph

    missing_end = g.bfs('Lani Wu', 'Banksy')
    assert missing_end == None

    #edge case 3: run bfs on nodes that are not connected and raise exception

    with pytest.raises(Exception):
        assert g.bfs('Lani Wu', 'Neil Rish'), "These nodes are not connected"




