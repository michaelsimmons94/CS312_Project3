#!/usr/bin/python3


class CS312GraphEdge:
    def __init__( self, src_node, dest_node, edge_length ):
        self.src   = src_node
        self.dest  = dest_node
        self.length= edge_length

    def __repr__( self ):
        return self.__str__()

    def __str__( self ):
        return '(src={} dest={} length={})'.format(self.src,self.dest,self.length)

class CS312GraphNode:
    def __init__( self, node_id, node_loc):
        self.node_id   = node_id
        self.loc       = node_loc
        self.neighbors = []
        self.src_dist = float('inf')
        self.prev_node = None
        self.used=False

    def addEdge( self, neighborNode, weight ):
        self.neighbors.append( CS312GraphEdge(self,neighborNode,weight) )

    def __str__( self ):
        neighbors = [edge.dest.node_id for edge in self.neighbors]
        if self.prev_node==None:
            return 'Node(id:{},neighbors:{}, prev_node:{})'.format(self.node_id,neighbors, "None")
        return 'Node(id:{},neighbors:{}, prev_node:{})'.format(self.node_id,neighbors, self.prev_node.node_id)


class CS312Graph:
    def __init__( self, nodeList, edgeList ):
        self.nodes    = []
        for i in range(len(nodeList)):
            self.nodes.append( CS312GraphNode( i, nodeList[i] ) )

        for i in range(len(nodeList)):
            neighbors = edgeList[i]
            for n in neighbors:
                self.nodes[i].addEdge( self.nodes[n[0]], n[1] )
        
    def __str__( self ):
        s = []
        for n in self.nodes:
            s.append(n.neighbors)
        return str(s)

    def getNodes( self ):
        return self.nodes

