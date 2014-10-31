'''
Created on Jun 9, 2014

@author: ACASADev
'''
import random
import math
if __name__ == '__main__':
    my_list = random.sample(xrange(100),30)
    h=1
    i=0
    h_array=[]
    while h < my_list.__len__():
        h_array.append(h)
        h=3*h+1
        i=i+1
    h_req = h_array[i-2]
    
    while h_req>0:
        i=0
        while i+h_req < my_list.__len__()-1:
            if my_list[i]> my_list[i+h_req]:
                temp = my_list[i+h_req]
                my_list[i+h_req]=my_list[i]
                my_list[i]=temp
            i+=1
        h_req= h_req/3
    
    print " Sorted Array is :"
    print my_list
    
             
    