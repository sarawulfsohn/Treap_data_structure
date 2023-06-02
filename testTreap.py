from Treap  import *
import pytest
import random


alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
ts = 1000 #torture size for # of inserts
TS = 100 #torture size that repeats each function
    

#insert nodes- keys are str- and then assert that they can be found in the treap
#we are searching for the key inmediately after insertion
def testInsertionsStr():
    for i in range(TS):
        t = Treap()
        for i in range(ts):
            
            data = ''
            for i in range(10): #length of data
                data += random.choice(alphabet)
            
            key = random.choice(alphabet)
            t.insert(key, data)
            
            #make sure we can find the key in treap
            assert t.find(key) != False

#insert nodes- keys are int- and then assert that they can be found in the treap   
#we are searching for the key inmediately after insertion
def testInsertionsInt():
    for i in range(TS):
        t = Treap()
        for i in range(ts):
            
            data = ''
            for i in range(10): #length of data
                data += random.choice(alphabet)
            
            key = random.randint(1,ts)
            t.insert(key, data)
            
            #make sure we can find the key in treap
            assert t.find(key) != False

#insert nodes- keys are int- and then assert that they can be found in the treap   
#we are searching for the key after all the keys have been inserted       
def testInsertionAfterINT():
    for i in range(TS):
        t = Treap()
        inserted = [] #keep track of inserted keys
        for i in range(ts):
            
            data = ''
            for i in range(10): #length of data
                data += random.choice(alphabet)
            
            key = random.randint(1,ts)
            t.insert(key, data)
            inserted += [key]
        
        #make sure we can find the key in treap
        for i in inserted:       
            assert t.find(i) != False    

#using the checkPriority function, make sure that the heap priority is not violated
def testHeapPropertySTR():
    for i in range(TS):
        t = Treap()
        for i in range(ts):
            
            data = ''
            for i in range(10): #length of data
                data += random.choice(alphabet)
            
            key = random.choice(alphabet)
            t.insert(key, data)    
        
        ans = t.checkPriority()
        assert False not in ans #in the case of heap violation a False would have been appended to ans

#using the checkPriority function, make sure that the heap priority is not violated    
def testHeapPropertyINT():
    for i in range(TS):
        t = Treap()
        for i in range(ts):
            
            data = ''
            for i in range(10): #length of data
                data += random.choice(alphabet)
            
            key = random.randint(1,ts)
            t.insert(key, data)    
        
        ans = t.checkPriority()
        assert False not in ans #in the case of heap violation a False would have been appended to ans
    
#it will delete a node that is both the root and a leaf node
def testDeleteRootLeaf():
    for i in range(TS):
        t = Treap()
        for i in range(ts):
            key = random.choice(alphabet)
            t.insert(key, "foo")           
            t.delete(key)
            assert t.getRoot() == None

#delete nodes from treap and make sure they can be found
def testDelete():
    for i in range(TS):
        t = Treap()
        inserted = []
        
        for i in range(ts):
            
            data = ''
            for i in range(10): #length of data
                data += random.choice(alphabet)
            
            key = random.randint(1,ts)
            t.insert(key, data)  
            inserted += [key]
        
        random.shuffle(inserted)
        for i in inserted:
            t.delete(i)
            assert t.find(i) == False

#check that the treap is balances -according to BST- after insertions, when keys are ints       
def testBstBalanceINT():
    for i in range(TS):
        t = Treap()
        for i in range(ts):
            
            data = ''
            for i in range(10): #length of data
                data += random.choice(alphabet)
            
            key = random.randint(1,ts)
            t.insert(key, data)    
        
        l = t.inOrderPrint()  
        for i in range(len(l)-1):
            assert int(l[i+1]) > int(l[i])
        
#check that the treap is balances -according to BST- after deletions, when keys are str           
def testBstDeleteBalanceINT():
    for i in range(TS):
        t = Treap()
        inserted = []
        for i in range(ts):
            
            data = ''
            for i in range(10): #length of data
                data += random.choice(alphabet)
            
            key = random.randint(1,ts)
            t.insert(key, data) 
            inserted += [key]
        
        remove = random.choice(inserted) #randomly select a key to be deleted
        j = t.inOrderPrint()  
    
        for i in range(len(j)-1):
            assert int(j[i+1]) > int(j[i])        

#check that the treap is balances -according to BST- after insertions, when keys are str           
def testBstBalanceSTR():
    for i in range(TS):
        t = Treap()
        for i in range(ts):
            
            data = ''
            for i in range(10): #length of data
                data += random.choice(alphabet)
            
            key = random.choice(alphabet)
            t.insert(key, data)    
        
        j = t.inOrderPrint()  
    
        for i in range(len(j)-1):
            assert j[i+1] > j[i]

#check that the treap is balances -according to BST- after deletions, when keys are str           
def testBstDeleteBalanceSTR():
    for i in range(TS):
        t = Treap()
        inserted = []
        for i in range(ts):
            
            data = ''
            for i in range(10): #length of data
                data += random.choice(alphabet)
            
            key = random.choice(alphabet)
            t.insert(key, data) 
            inserted += [key]
        
        remove = random.choice(inserted) #randomly select a key to be deleted
        j = t.inOrderPrint()  
    
        for i in range(len(j)-1):
            assert j[i+1] > j[i]        
        
    
pytest.main(["-v", "-s", "testTreap.py"])  