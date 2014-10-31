'''
Created on Jul 11, 2014

@author: nigamv
'''
import copy

    
class Node():
        def __init__(self,key,value):
            self.leftNode =None
            self.rightNode =None
            self.value=value
            self.key =key
            
        
        def get(self,root,key):
            if root is None:
                print" no element present"
            
            while root is not None:
                if key<root.key:
                    root=root.leftNode
                elif key> root.key:
                    root= root.rightNode
                elif key == root.key:
                    return root.value
                else:
                    return None
        
            
        def put(self,root,node):
            
            if root is None:
                root = node
                
            else:
                if node.key < root.key:
                    if root.leftNode == None:
                        root.leftNode = node
                    else:
                        self.put(root.leftNode,node)
                elif node.key> root.key:
                    if root.rightNode == None:
                        root.rightNode = node
                    else:
                        self.put(root.rightNode,node)
                   
                
            
    
                
if __name__ == '__main__':
    node = Node(0,0)
    for i in xrange(10):
        newNode = Node(i+1,5*(i+1))
        node.put(node,newNode)
    value=[]
    for i in xrange(10):
        value.append(node.get(node,i+1))
    
    print" values are \n"
    print value