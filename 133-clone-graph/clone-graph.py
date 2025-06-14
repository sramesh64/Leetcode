"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        if (node == None): return None

        visited = {}
        

        def dfs(node):
            if (node in visited): return visited[node]

            new_node = Node(node.val)
            visited[node] = new_node
            for neighbor in node.neighbors:
                new_node.neighbors.append(dfs(neighbor)) 
            return new_node

        return dfs(node)






        