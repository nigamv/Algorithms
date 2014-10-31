'''
Created on Jun 9, 2014

@author: ACASADev
'''
""" Insertion Sort: Algorithm below sorts a given array according to insertion sort. It works on the principle that of comparing two consecutive numbers
    till the time you are able to find them in descending order. It stores the smaller number temporarily and stores the position
    of the larger number. Then it runs a backward loop till the point it can find a suitable position for the smaller number i.e.
    till the time it finds a number smaller than the temp. Temp value is then inserted at one position ahead of the current smaller number
    found. In this way whole array is sorted in ascending order. Worst time taken by the algorithm is O(n^2)"""
import random
if __name__ == '__main__':
    my_list = random.sample(xrange(100),30)
    for i in xrange(my_list.__len__()-1):
        if my_list[i] > my_list[i+1]:
            j=i
            temp = my_list[i+1]
            while j>=0:
                if my_list[j]> temp:
                    my_list[j+1]=my_list[j]
                    my_list[j]= temp
                else:
                    break
                j-=1

           
      
    print " Sorted array is : "
    print my_list            