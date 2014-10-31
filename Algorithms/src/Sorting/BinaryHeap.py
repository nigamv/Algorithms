'''
Created on Jul 8, 2014

@author: nigamv
'''
import random
import copy
from random import randint
class BinaryHeap():
    
   
    def __init__(self,temp):
        self.array=copy.deepcopy(temp)
        self.N=0
    def less(self,i,j):
        return self.array[i] < self.array[j]
    def swim(self,k):
        while k >1 and self.less(k/2,k):
            self.exchange(k/2,k)
            k=k/2
    def exchange(self,i,j):
        temp= self.array[i]
        self.array[i]= self.array[j]
        self.array[j]=temp
    def insert(self,elem):
        self.array.append(elem)
        self.N=self.N+1
        self.swim(self.N)
    def sink(self,k):
        while 2*k <= self.N:
            j= 2*k;
            if j<self.N and self.less(j,j+1):
                j=j+1
            if not self.less(k,j):
                break
            self.exchange(k, j)
            k=j
    def delMax(self):
        maximum= self.array[1]
        self.exchange(i, self.N)
        self.N=self.N-1
        self.sink(1)
        return maximum    
    def heapOrder(self):
        k=self.N/2
        while k>=1:
            self.sink(k)
            k=k-1
    def sort(self):
        while self.N>1:
            self.exchange(1, self.N)
            self.N= self.N-1
            self.sink(1)
              
            
if __name__ == '__main__':
    array =[]
    array.append(0)
    for i in xrange(100):
        array.append(random.randint(0,100))
    print " actual array is"
    print array
    heap=BinaryHeap(array)
    heap.N= array.__len__()-1
    heap.heapOrder()
    for i in xrange(100):
        print str(i+1)+" : "+ str(heap.array[i+1])+"\n"
    heap.sort()
    array=copy.deepcopy(heap.array)
    print" sorted array is"
    print array
    
    