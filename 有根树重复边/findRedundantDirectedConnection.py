class Solution:
    def findRedundantDirectedConnection(self, edges):
        # multiple parent check
        children_parent = {}
        duplicate_parent_child = None
        for edge in edges:
            if edge[1] not in children_parent:
                children_parent[edge[1]] = [edge[0]]
            else:
                children_parent[edge[1]].append(edge[0])
                duplicate_parent_child = edge[1]
        if duplicate_parent_child:
            return [children_parent[duplicate_parent_child][-1], duplicate_parent_child]
        # detect the last recorded edge of loop
        class Node:
            def __init__(self, val):
                self.val=val
                self.next=None
                self.parent=None
        # overall_nodes = len(edges)
        nodes = {}
        for edge in edges:
            p_val = edge[0]
            c_val = edge[1]
            # create or find existed nodes
            if p_val in nodes:
                p_node = nodes[p_val]
            else:
                p_node = Node(p_val)
                nodes[p_val] = p_node
            if c_val in nodes:
                c_node = nodes[c_val]
            else:
                c_node = Node(c_val)
                nodes[c_val] = c_node
            # create relationship between the two nodes
            if p_node.next:
                p_node.next.append(c_node)
            else:
                p_node.next = [c_node]
            # mulitple parents problem should've resolved before
            c_node.parent = p_node
        start_node = nodes[edges[0][0]]
        queue = [start_node]
        visited = []
        while queue:
            nodes_num = len(queue)
            for i in range(nodes_num):
                pending_node = queue.pop()
                if pending_node.val in visited:
                    return [pending_node.parent.val, pending_node.val]
                else:
                    visited.append(pending_node.val)
                if pending_node.next:
                    for next_pending_node in pending_node.next:
                        queue.insert(0, next_pending_node)
        return None
    
    def findRedundantDirectedConnection_v2(self, edges):
        # detect the last recorded edge of loop
        class Node:
            def __init__(self, val):
                self.val=val
                self.next=None
                self.parent=None
        # overall_nodes = len(edges)
        nodes = {}
        for edge in edges:
            p_val = edge[0]
            c_val = edge[1]
            # create or find existed nodes
            if p_val in nodes:
                p_node = nodes[p_val]
            else:
                p_node = Node(p_val)
                nodes[p_val] = p_node
            if c_val in nodes:
                c_node = nodes[c_val]
            else:
                c_node = Node(c_val)
                nodes[c_val] = c_node
            # create relationship between the two nodes
            if p_node.next:
                p_node.next.append(c_node)
            else:
                p_node.next = [c_node]
            if c_node.parent:
                c_node.parent.append(p_node)
            else:
                c_node.parent = [p_node]
        start_node = nodes[edges[0][0]]
        queue = [start_node]
        visited = []
        while queue:
            nodes_num = len(queue)
            for i in range(nodes_num):
                pending_node = queue.pop()
                if pending_node.val in visited:
                    return [pending_node.parent[-1].val, pending_node.val]
                else:
                    visited.append(pending_node.val)
                if pending_node.next:
                    for next_pending_node in pending_node.next:
                        queue.insert(0, next_pending_node)
        return None
    def findRedundantDirectedConnection_v3(self, edges):
        start_node, nodes_num = self.build_nodes(edges)
        count = 0
        has_loop = len(edges) == nodes_num


        while queue:
            x = len(queue)
            y = queue.pop()
            count += 1
            if count > len(edges):
                has_loop = True
            if y.next:
                for z in y.next:
                    queue.insert(0, z)

        # multiple parent check
        children_parent = {}
        duplicate_parent_child = None
        for edge in edges:
            if edge[1] not in children_parent:
                children_parent[edge[1]] = [edge[0]]
            else:
                children_parent[edge[1]].append(edge[0])
                duplicate_parent_child = edge[1]
        if duplicate_parent_child:
            if not has_loop:
                return [children_parent[duplicate_parent_child][-1], duplicate_parent_child]
            else:

        # detect the last recorded edge of loop
        class Node:
            def __init__(self, val):
                self.val=val
                self.next=None
                self.parent=None
        
        queue = [start_node]
        visited = []
        while queue:
            nodes_num = len(queue)
            for i in range(nodes_num):
                pending_node = queue.pop()
                if pending_node.val in visited:
                    return [pending_node.parent.val, pending_node.val]
                else:
                    visited.append(pending_node.val)
                if pending_node.next:
                    for next_pending_node in pending_node.next:
                        queue.insert(0, next_pending_node)
        return None
    
    def build_nodes(edges):
        nodes = {}
        for edge in edges:
            p_val = edge[0]
            c_val = edge[1]
            # create or find existed nodes
            if p_val in nodes:
                p_node = nodes[p_val]
            else:
                p_node = Node(p_val)
                nodes[p_val] = p_node
            if c_val in nodes:
                c_node = nodes[c_val]
            else:
                c_node = Node(c_val)
                nodes[c_val] = c_node
            # create relationship between the two nodes
            if p_node.next:
                p_node.next.append(c_node)
            else:
                p_node.next = [c_node]
            # mulitple parents problem should've resolved before
            c_node.parent = p_node
            return nodes[edges[0][0]]

if __name__ == "__main__":
    s = Solution()
    edges = [[1,2], [2,3], [3,4], [4,1], [1,5]]
    ret = s.findRedundantDirectedConnection_v2(edges)
    print('first case', ret)
    # assert ret == [4,1]

    edges = [[1,2], [1,3], [2,3]]
    ret = s.findRedundantDirectedConnection_v2(edges)
    # assert ret == [2,3]
    print('second case', ret)

    edges = [[2,1],[3,1],[4,2],[1,4]]
    ret = s.findRedundantDirectedConnection_v2(edges)
    # assert ret == [2,1]
    print('third case', ret)