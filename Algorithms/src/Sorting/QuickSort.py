'''
Created on Jul 6, 2014

@author: nigamv
'''
import random
def partition(array,low,high):
    i=low+1
    j= high
    start=array[low]
    
    while True:
        while array[i]<= start:
            if i >= high:
                break
            i=i+1
        while array[j]>= start:
            if j <= low:
                break
            j=j-1
        if j <= i:
            break
        exchange(array,i,j)
    exchange(array,low,j)
    return j
def exchange(array,i,j):
    temp = array[i]
    array[i]=array[j]
    array[j]=temp
def sort( array,low,high):
    if high < low:
        return
    k= partition(array,low,high)
    sort(array,low,k-1)
    sort(array,k+1,high)     
if __name__ == '__main__':
    array =[]
    for i in xrange(100):
        array.append(random.randint(0,100))
    print " actual array is"
    print array
    sort(array,0,array.__len__()-1)
    print " sorted array is"
    print array