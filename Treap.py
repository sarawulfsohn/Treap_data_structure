'''this treap is to be used for running the pytests, as the other class includes
   print statements that explain each step, and interferes with the performance
   of pytest
'''
from BitHash import BitHash
import random
import math
import pytest

'''I hereby certify that this program is solely the result of my own work and 
is in compliance with the Academic Integrity policy of the course syllabus and 
the academic integrity policy of the CS department.
                                                            ~ Sara Wulfsohn'''

 
   
class Treap(object):  
   
   class __Node(object):         
      # create a Node with key/data pair, and possible children
      def __init__(self, key, data, priority, left=None, right=None):         
         self.key  = key   
         self.data = data
         self.priority = priority
         self.leftChild = left
         self.rightChild = right     
         
      def __str__(self):      
         return "{" + str(self.key) + ", " + str(self.data) + "}"    
      
   # Create a Treap object, initially empty
   def __init__(self): self.__root = None  
   
   #getter method
   def getRoot(self):
      return self.__root
   
      
   # Check for empty tree
   def isEmpty(self):  return self.__root is None
  
   def insert(self, key, data):

      #insert key as BST 
      parent, node, priority = self.__insertBST(key, data)      
      
      #restore heap-property
      #if we didnt insert the key because we only updated its data, dont re-balance
      if parent != False and node != False and priority != False:
         self.heapBalanceR(node)
      
   
   #helper method, will insert new key as a BST
   def __insertBST(self, k, data):  
      priority = BitHash(k)
      #priority = random.randint(1, 100)
      
      # Try finding the k already in the tree, and getting parent node.
      node, parent = self.__find(k) 
      
      if node:                # If we find a node with this k,
         node.data = data     # then update the node's data
         return False, False, False         # and return flag for no insertion

      # for empty tree, insert new node as root. 
      if parent is None: 
         node = self.__Node(k, data, priority)  
         self.__root = node
         return None, node, priority
      
      # insert the new k/data node to left or right based on the k
      elif k < parent.key:  
         node = self.__Node(k, data, priority) 
         parent.leftChild  = node
      else:
         node = self.__Node(k, data, priority) 
         parent.rightChild = node
      
      return parent, node, priority 
   
   
   #will check that the whole tree is in balance going from the bottom up   
   def heapBalanceR(self, i): #i stands for the recently inserted key
      
      cur, parent = self.__find(i.key)
      
      #in case we need to rotate, we will rotate the parent regarding the grandparent
      if parent:
         parent, grandp = self.__find(parent.key) 
      
      
      #we have reached the root
      if cur.key == self.__root.key:
         return
   
      elif cur.priority > parent.priority:
         
         #if cur is the left child
         if parent.leftChild == cur:
            
            #if grandp is None, meaning that the parent is the root
            if grandp is None:
               self.__root = self.rotateRight(self.__root)
               self.heapBalanceR(parent)
               return
            
            #if parent is the left child:
            elif grandp.leftChild == parent:
               grandp.leftChild = self.rotateRight(grandp.leftChild)
               self.heapBalanceR(parent)
               return
            
            # if parent is the right child
            else:
               grandp.rightChild = self.rotateRight(grandp.rightChild)
               self.heapBalanceR(parent)     
               return
               
         
         #cur is the right child
         else:
            
            #if grandp is None, meaning that the parent is the root
            if grandp is None:
               self.__root = self.rotateLeft(parent)
               self.heapBalanceR(parent) 
               return
            
            #if parent is the right child
            elif grandp.rightChild == parent:
               grandp.rightChild = self.rotateLeft(grandp.rightChild)
               self.heapBalanceR(parent)
               return
            
            #if parent is the left child
            else:
               grandp.leftChild = self.rotateLeft(grandp.leftChild)
               self.heapBalanceR(parent)  
               return
               
      
      self.heapBalanceR(parent)
      

   # Returns a reference to the Node whose key is goal, and also a reference to the parent of the Node.
   def __find(self, goal):

      current = self.__root   # start at the root
      parent = None           # the root node has no parent
   
      while current and goal != current.key: 
         parent = current         
         if goal < current.key:    
            current = current.leftChild  # go left.     
         else:        
            current = current.rightChild # go right
          
      # If the loop ended on a node, it must have the goal key
      return (current, parent) # Return the node or None and parent
   
   #searches the treap and returns key
   def find(self, goal):
      key, other = self.__find(goal)
      if key: 
         return key
      else:
         return False
      
   
   def rotateRight(self, top):  # Rotate a subtree rooted at top to the right
      
      toRaise = top.leftChild        # The node to raise is top's left child
      top.leftChild = toRaise.rightChild  # The raised node's right crosses over
      toRaise.rightChild = top       # to be the left subtree under the old
      
      #update reference to root
      if top.key==self.__root.key:
         self.__root = toRaise
      
      return toRaise            # Return raised node to update parent

   def rotateLeft(self, top):   # Rotate a subtree rooted at top to the left
      
      toRaise = top.rightChild       # The node to raise is top's right child
      top.rightChild = toRaise.leftChild  # The raised node's left crosses over
      toRaise.leftChild = top        # to be the right subtree under the old
      
      #update reference to root
      if top.key==self.__root.key:
         self.__root = toRaise      
      
      return toRaise            # Return raised node to update parent
   
   #deletes a key in treap
   #for this method to function, k must be either a str or int -not a Node
   def delete(self, k):
      #find key in tree
      key, parent = self.__find(k)
      
      #if there is no node on the treap with that key
      if not key: 
         return
      
      #increase its priority to inf
      key.priority = math.inf 
      
      #rotate key off fringe and delete
      self.__delete(key)

   
   #private method, rotates key untill its a leaf and deletes it
   def __delete(self, k):
      cur, parent = self.__find(k.key)
      
      #if node is a leaf:
      if k.rightChild == None and k.leftChild == None:
         
         #if node is both a leaf and root
         if parent == None:
            self.__root = None
         
         else:            
            #if k is a left child
            if parent.leftChild and parent.leftChild == k:
               parent.leftChild = None
            
            #if k is a right child
            else:
               parent.rightChild = None         
            
         return True
      
      #if k is the root
      elif self.__root == k:
         
         #if its right child is bigger than its left child
         if k.rightChild and k.leftChild and k.rightChild.key > k.leftChild.key:
            self.__root = self.rotateLeft(k) # rotate
            self.__delete(k)   # recursively 
            
         #if its left child is bigger than its eight child
         elif k.rightChild and k.leftChild and k.rightChild.key < k.leftChild.key:
            self.__root = self.rotateRight(k) # rotate
            self.__delete(k)   # recursively
            
         #if it only has a right child
         elif k.rightChild and not k.leftChild:            
            self.__root = self.rotateLeft(k) # rotate
            self.__delete(k)   # recursively
            
         #if it only has a left child
         else:
            self.__root = self.rotateRight(k) # rotate
            self.__delete(k)   # recursively  
            
         
      #if its right child is bigger than the left child
      elif (k.rightChild and k.leftChild and k.rightChild.key > k.leftChild.key):
         
         #if k is the left child:
         if parent.leftChild == k:
            parent.leftChild = self.rotateLeft(k) # rotate
            self.__delete(k)   # recursively 
            
         #if k is the right child
         else:
            parent.rightChild = self.rotateLeft(k) # rotate
            self.__delete(k)   # recursively             
            
      
      #if its left child is bigger than the right child
      elif k.rightChild and k.leftChild and k.leftChild.key < k.rightChild.key:
         
         #if k is the left child:
         if parent.leftChild == k:         
            parent.leftChild = self.rotateRight(k) # rotate
            self.__delete(k)   # recursively
         
         # if k is the right child:
         else:
            parent.rightChild = self.rotateRight(k) # rotate
            self.__delete(k)   # recursively            
            
   
      #if it only has a right child
      elif k.rightChild and not k.leftChild:
         
         #if k is the left child:
         if parent.leftChild == k:              
            parent.leftChild = self.rotateLeft(k) # rotate
            self.__delete(k)   # recursively
            
         # if k is the right child:
         else:         
            parent.rightChild = self.rotateLeft(k) # rotate
            self.__delete(k)   # recursively            
      
      #if it only has a left child
      else:
         
         #if k is the left child:
         if parent.leftChild == k:             
            parent.leftChild = self.rotateRight(k) # rotate
            self.__delete(k)   # recursively  
         
         # if k is the right child:
         else:            
            parent.rightChild = self.rotateRight(k) # rotate
            self.__delete(k)   # recursively  
   
   #recursively traverse treap at root and make sure the childrens priority is not greater than the parents         
   def checkPriority(self, cur = "start", ans = []):
      if cur == "start": cur = self.__root
      
      if cur:
         if cur.leftChild and cur.priority < cur.leftChild.priority:
            ans +=  [False] #in the case of heap violation we will have a list containinf False
            self.checkPriority(cur.leftChild, ans)
            self.checkPriority(cur.rightChild, ans)
         elif cur.rightChild and cur.priority < cur.rightChild.priority:
            ans += [False] #in the case of heap violation we will have a list containinf False
            self.checkPriority(cur.leftChild, ans)
            self.checkPriority(cur.rightChild, ans)
      return ans
            
     
   def inOrderPrint(self, cur="start", result=None):
      if cur == "start":
         cur = self.__root
      if result is None:
         result = []
      if cur:
         self.inOrderPrint(cur.leftChild, result)
         result.append(" " + str(cur.key))
         self.inOrderPrint(cur.rightChild, result)
      return result
   
   def preOrderPrint(self, cur="start"):
      if cur == "start": cur = self.__root
      if cur:
         print(" " + str(cur), end="")
         self.preOrderPrint(cur.leftChild)
         self.preOrderPrint(cur.rightChild)

   def postOrderPrint(self, cur="start"):
      if cur == "start": cur = self.__root
      if cur:
         self.postOrderPrint(cur.leftChild)
         self.postOrderPrint(cur.rightChild)
         print(" " + str(cur), end="")      

   def printTree(self):
      self.__pTree(self.__root, "ROOT:  ", "")
      print()
       
   def __pTree(self, n, kind, indent):
      print("\n" + indent + kind, end="")
      if n:   
         print(n, end="")
         if n.leftChild:
            self.__pTree(n.leftChild,  "LEFT:   ",  indent + "    ")
         if n.rightChild:
            self.__pTree(n.rightChild, "RIGHT:  ", indent + "    ")        
         
def __main():  
   t = Treap()
   
   print("it is ", t.isEmpty(), "that the tree is empty")
   print("##############")
   
   t.insert("b", "slcnein")
   t.insert("w", "vckyhjvckwv")
   t.insert("z", "kbcqliuwbcui")
   t.insert("c", "jc bk2jwbckj")
   t.insert("f", "cbekbc")
   t.insert("a", "cjibeciuwb")
   t.insert("g", "kqcj b2kwj")
   t.insert("t", "kcblekubk")
   t.insert("y", "hwvcejug")
   
   print("##############")
   
   print("making sure priority is in order")
   a = t.checkPriority()
   if False not in a: print("heap priority is ok!")
   else:              print("heap priority not working")
   print("##############")
   
   t.delete("g")
   print("##############")
   
   t.find("a")
   t.find("g")

   
   print("it is ", t.isEmpty(), "that the tree is empty")    
   
   print("root:", t.getRoot())
   print("###################")
   
   print("preOrderPrint")
   print(t.preOrderPrint())
   print()
   
   print("inOrderPrint")
   print(t.inOrderPrint())
   print()
   
   print("postOrderPrint")
   print(t.postOrderPrint())
   print()
   
   print("print tree")
   print(t.printTree())
   print("###################")
   

   listt = t.inOrderPrint()
   for i in range(len(listt)-1):
      if listt[i] > listt[i+1]:
         print("heap priority is violated")
         return False
      print("heap prority is working!")
      
if __name__ == '__main__':
   __main()       
