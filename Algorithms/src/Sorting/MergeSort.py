'''
Created on Jul 6, 2014

@author: nigamv
'''
import random
import copy
def merge(array,temp_array,low,mid,high):
    temp_array= copy.deepcopy(array)
    i=low
    j=mid+1
    k=low
    while (k<=high):
        if i> mid:
            array[k]= temp_array[j]
            j=j+1
            k=k+1
        elif j > high:
            array[k]= temp_array[i]
            k=k+1
            i=i+1
        elif temp_array[i]<temp_array[j]:
            array[k]= temp_array[i]
            k=k+1
            i=i+1
        else:
            array[k]=temp_array[j]
            j=j+1
            k=k+1
        
def sort(array,temp_array,low,high):
    if (high<=low):
        return
    mid= low+(high-low)/2
    sort(array,temp_array,low,mid)
    sort(array,temp_array,mid+1,high)
    merge(array,temp_array,low,mid,high)
    

if __name__ == '__main__':
    array =[]
    for i in xrange(100):
        array.append(random.randint(0,100))
    temp_array =[]
    print " actual array is"
    print array
    sort(array,temp_array,0,array.__len__()-1)
    print "Sorted array is \n"
    print array
    