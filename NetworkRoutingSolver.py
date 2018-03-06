#!/usr/bin/python3


from CS312Graph import *
import time


class NetworkRoutingSolver:
    def __init__( self, display ):
        pass



    def initializeNetwork( self, network ):
        assert( type(network) == CS312Graph )
        self.network = network



    def getShortestPath( self, destIndex ):
        self.dest = destIndex

        # TODO: RETURN THE SHORTEST PATH FOR destIndex
        #       INSTEAD OF THE DUMMY SET OF EDGES BELOW
        #       IT'S JUST AN EXAMPLE OF THE FORMAT YOU'LL 
        #       NEED TO USE

        path=[]
        pathtext=[]
        graph= self.network.nodes
        dest_node= graph[self.dest]
        start_node = graph[self.source]
        node= dest_node
        while node.prev_node!=None:
            path.insert(0,(node.prev_node.loc, node.loc, '{:.0f}'.format(node.src_dist-node.prev_node.src_dist)))
            pathtext.insert(0, node.node_id)
            node=node.prev_node
        path.insert(0,(node.loc, start_node.loc, '{:.0f}'.format(node.src_dist-start_node.src_dist)))
        #print(path)
        print("path traveled:")
        for x in pathtext:
            print("node ", x)
        #print("SPath fin")
        return {'cost':dest_node.src_dist, 'path':path}

            

    def computeShortestPaths( self, srcIndex, use_heap=False ):
        self.source = srcIndex

        t1 = time.time()
        # TODO: RUN DIJKSTRA'S TO DETERMINE SHORTEST PATHS.
        #       ALSO, STORE THE RESULTS FOR THE SUBSEQUENT
        #       CALL TO getShortestPath(dest_index)
        # Dajkstra's Implementation

        
        graph= self.network.nodes
        self.reset(graph)
        start_node=graph[self.source]
        start_node.src_dist=0
        if use_heap==False:
            #MakeQueue---
            queue_size=len(graph)
            while queue_size>0:
                node=self.deleteMin(graph)
                queue_size= queue_size-1
                for edge in node.neighbors:
                    neighbor = edge.dest
                    new_dist = edge.length+node.src_dist
                    if neighbor.src_dist > new_dist:
                        neighbor.prev_node = node
                        neighbor.src_dist = new_dist
            
        else:
            #Make Queue
            heap=[]
            heap.append(start_node)
            while len(heap)>0:
                node=self.deleteHeapMin(heap)
                for edge in node.neighbors:
                    neighbor = edge.dest
                    new_dist = edge.length+node.src_dist
                    if neighbor.src_dist > new_dist:
                        neighbor.prev_node = node
                        neighbor.src_dist = new_dist
                        self.decreaseKey(heap, neighbor)#think about edge case when a new node has already been used
            #print("finished")
        t2 = time.time()
        return (t2-t1)
                    
                
    def reset(self, graph):
        for node in graph:
            node.prev_node=None
            node.src_dist=float('inf')
            node.used=False
    def deleteMin(self, graph):
        min_dist=float('inf')
        min_node_index=0
        for node in graph:
            if node.used==False and node.src_dist<min_dist:
                min_dist=node.src_dist
                min_node_index=graph.index(node)
        min_node=graph[min_node_index]
        min_node.used= True
        return min_node
    def decreaseKey(self,heap,node):
        heap[len(heap)]= node
        self.bubbleUp(heap)
    def deleteHeapMin(self, heap):
        node=heap[0]
        node.used=True
        new_min=heap[len(heap)-1]
        heap[0]=new_min
        heap.pop()
        self.bubbleDown(heap)
        return node
    def decreaseKey(self, heap, neighbor):
        heap.append(neighbor) 
    def getLeftChildIndex(self,parent_index):
        return 2*parent_index+1
    def getRightChildIndex(self,parent_index):
        return 2*parent_index+2
    def getParentIndex(self,child_index):
        return (child_index-1)//2
    def getLeftChild(self,heap, parent_index):
        return heap[self.getLeftChildIndex(parent_index)]
    def getLeftChildWeight(self, heap, parent_index):
        return self.getLeftChild(heap, parent_index).src_dist
    def getRightChild(self,heap, parent_index):
        return heap[self.getRightChildIndex(parent_index)]
    def getRightChildWeight(self, heap, parent_index):
        return self.getRightChild(heap, parent_index).src_dist
    def getParent(self,heap, child_index):
        return heap[self.getParentIndex(child_index)]
    def getParentWeight(self, heap, child_index):
        return self.getParent(heap,child_index).src_dist
    def swap(self,heap, index1, index2):
        temp=heap[index1]
        heap[index1]=heap[index2]
        heap[index2]=temp
    def bubbleDown(self, heap):
        index=0
        while(self.getLeftChildIndex(index)<len(heap)-1):
            smallerChildIndex = self.getLeftChildIndex(index)
            rightChildWeight=self.getRightChildWeight(heap, index)
            leftChildWeight=self.getLeftChildWeight(heap,index)
            if self.getRightChildIndex(index)<=len(heap)-1 and rightChildWeight < leftChildWeight:
                smallerChildIndex = self.getRightChildIndex(index)
            if heap[index].src_dist < heap[smallerChildIndex].src_dist:
                break
            else:
                self.swap(heap,index,smallerChildIndex)
            index = smallerChildIndex
    def bubbleUp(self, heap):
        index=len(heap)-1
        while(self.getParentIndex(index)>=0 and self.getParentWeight(heap, index)>heap[index].src_dist):
            swap(heap,self.getParentIndex(index),index)
            index=self.getParentIndex(index)


