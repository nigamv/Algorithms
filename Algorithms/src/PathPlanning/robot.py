'''
Created on Feb 17, 2014

@author: user
'''
import re
from math import sqrt
import copy

EPSILON=.0000000001


            
def read(filename):
    inFile=open(filename, "r")
    startLine=inFile.readline()
    endLine=inFile.readline()
    
    number=re.compile("-?[0-9]+\.[0-9]+")

    (startXStr, startYStr)=number.findall(startLine)
    (endXStr, endYStr)=number.findall(endLine)
    
    polygons=[]
    curPolygon=[]
    
    polygons.append(((-5,-5),(5, -5),(5, 5),(-5, 5)))
    
    for line in inFile.readlines():
        if line.strip()=="":
            polygons.append(tuple(curPolygon))
            curPolygon=[]
        else:
            (curXStr, curYStr)=number.findall(line)
            curPolygon.append((float(curXStr), float(curYStr)))
    return ((float(startXStr), float(startYStr)), (float(endXStr), float(endYStr)), polygons)
def pathIntersectsAnyLines(start, end, lines):
    #print "Checking paths in between " + str(start) + " and " + str(end)

    for (one, two) in lines:
        if (linesIntersect((start, end), (one, two))):
            #print "Intersects " + str((one, two))
            return True
    return False

def verticalIntersection(vertical, other):
    if (isVertical(other)):
        ((ax1,ay1), (ax2, ay2))=vertical
        ((bx1,by1),(bx2, by2))=other
        return ((abs(ax1-bx1)<=EPSILON) and (((ay1-by1)*(ay1-by2)<=EPSILON) or ((ay2-by1)*(ay2-by2)<=EPSILON))) 
    else:
        ((x1,y1), (x2,y2))=other
        ((vx1, vy1), (vx2, vy2))=vertical
        slope=(y2-y1)/(x2-x1)
        deltaY=slope*(vx1-x1)
        projectedY=y1+deltaY
        return (projectedY-vy1)*(projectedY-vy2)<=EPSILON

def isVertical(line):
    ((x1,y1),(x2,y2))=line
    return (abs(x1-x2)<=EPSILON)

def linesIntersect(line1, line2):        
    (a, b)=line1
    (c, d)=line2
    
    acd=counterclockwise(a,c,d)
    bcd=counterclockwise(b,c,d)
    abc=counterclockwise(a,b,c)
    abd=counterclockwise(a,b,d)
    
    if (abs(acd)<=EPSILON):
        if (between(d, a, c)):
            return False
    if (abs(bcd)<=EPSILON):
        if (between(b,c,d)):
            return False
    if (abs(abc)<=EPSILON):
        if (between(a,b,c)):
            return False
    if (abs(abd)<=EPSILON):
        if (between(a,b,d)):
            return False
            
    if (abs(acd-bcd)<=EPSILON):
        return False
    if (abs(abc-abd)<=EPSILON):
        return False
    
    if (isVertical(line1)):
        return verticalIntersection(line1, line2)
    elif (isVertical(line2)):
        return verticalIntersection(line2, line1)

    
    return True

def between(a,b,c):
    (a1,a2)=a
    (b1,b2)=b
    (c1,c2)=c
    
    return (((b1-a1)*(c1-a1)<=EPSILON) and ((b2-a2)*(c2-a2)<=EPSILON))
        
def counterclockwise(pt1, pt2, pt3):
    (a,b)=pt1
    (c,d)=pt2
    (e,f)=pt3
    
    det=(c-a)*(f-b)-(d-b)*(e-a)
    
    if (det>=EPSILON):
        return 1
    elif (det<=-EPSILON):
        return -1
    else:
        return 0

def distance(p1, p2):
    (x1,y1)=p1
    (x2,y2)=p2
    
    return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
def extractallPoints(list1):
    list_temp=[]
    for x in list1:
        for k in x:
            list_temp.append(k)

    return list_temp

def traverseMidPoints(list_curr):
    temp_list=[]
    for x in list_curr:
        for k in x:
            temp_list.append(k)
    return temp_list
def depthList(list_curr,startPoint,goalPoint,called):
    tempDepth_list=[]
    for x in list_curr:
        if  x[0]> startPoint[0]+2*(called-1) and x[0]<=startPoint[0]+2*called and x[0]<=goalPoint[0]:
            tempDepth_list.append(x)
    return tempDepth_list
def breadthFirstSearch(listofMidPoints,startPoint,goalPoint,combined_allpoints):
    
    var_check=1
    tree_dictionary={}
    zipped_bfirst=[]
    list_gen_nodes=[]
    list_gen_nodes.append(startPoint)
    update=0
    path_array = []
    temp_list_bfirst= copy.deepcopy(listofMidPoints)
    temp_list_bfirst.append(goalPoint)
    #path_array.append(bfirst_startPoint)
    #while depth < count:
        #for bfirst in temp_list_bfirst:
            #distance_check =0
    
    end= False
    while update < len(list_gen_nodes):
        constant_list=[]
        for elem in list_gen_nodes:
            bfirst_startPoint = copy.deepcopy(elem)
#             print " length of general nodes"+ str(len(list_gen_nodes))
            update=update+1
#             print update
            
            temp_list=[]
#             print "length of nodes to check"+ str(len(temp_list_bfirst))
            for curr in temp_list_bfirst:
                #print var_check
#                 print "current node :"+ str(var_check)
#                 print "current element :"+ str(curr)
                
                #temp_bfirst= copy.deepcopy(temp_list_bfirst)
                #temp_bfirst.remove(curr)
                # for i in xrange(len(temp_bfirst)):
                #    k=i+1
                #   while(k< len(temp_bfirst)):
                #      zipped_bfirst.append(zip(temp_bfirst[i],temp_bfirst[k]))
                #     k=k+1
                #i=0
                #k=0
                for elem_combine in combined_allpoints:
                    for k in xrange(len(elem_combine)-1):
                        zipped_bfirst.append(zip(elem_combine[k],elem_combine[k+1]))
                    result = pathIntersectsAnyLines(bfirst_startPoint,curr,zipped_bfirst)
                    if result == True:
                        break
                    else:
                        continue    
#                 print result
                    #temp_dist = distance(bfirst_startPoint,curr)
                if result == False  and curr!= goalPoint:
                        #if distance_check == 0 or temp_dist< distance_check:
                        if curr not in temp_list:
                            temp_list.append(curr)
                        if curr not in constant_list:
                            constant_list.append(curr)
                elif result ==False and curr == goalPoint:
                        end= True
                        tree_dictionary.update({tuple(bfirst_startPoint):curr})
                        break
                var_check=var_check+1
            if   temp_list!=[] and update!= len(list_gen_nodes):
                tree_dictionary.update({tuple(bfirst_startPoint):temp_list})
            elif  temp_list!=[] and update == len(list_gen_nodes):
                tree_dictionary.update({tuple(bfirst_startPoint):temp_list})
                list_gen_nodes = copy.deepcopy(constant_list)
                elem = copy.deepcopy(constant_list[0])
                update=0
            elif end:
                break
        for x in temp_list:
            temp_list_bfirst.remove(x)
            #if depth!= count:
                #print "success"            
                #bfirst_startPoint = next_start
                #path_array.append(bfirst_startPoint)
            #else:
                #path_array.append(next_start)
                #break
#     print tree_dictionary
    #path_array.append(goalPoint)
    path_array.append(goalPoint)
    while goalPoint!= startPoint and goalPoint!= tuple(startPoint):
        for key,value in tree_dictionary.iteritems():
            if goalPoint == value or goalPoint in value:
                path_array.append(key)
                goalPoint = key
    return path_array              
            
def depthFirstSearch(listofMidPoints,startPoint,goalPoint,combined_allpoints):
    
    var_check=1
    tree_dictionary={}
    zipped_bfirst=[]
    path_array = []
    temp_list_bfirst= copy.deepcopy(listofMidPoints)
    temp_list_bfirst.append(goalPoint)
    end= False
    parent_node=copy.deepcopy(startPoint)
    last_node_checked=[]
    list_of_children=[]
    while parent_node:
        constant_list=[]
        tree_keys=[]
#         bfirst_startPoint=copy.deepcopy(parent_node)
        if tree_dictionary.has_key(tuple(parent_node)) and list_of_children==[]:
            list_of_children= tree_dictionary.get(parent_node)
        if list_of_children!=[] and last_node_checked!=[]:
            list_of_children.remove(last_node_checked)
            parent_node=list_of_children[0]
        tree_keys= tree_dictionary.keys()
        if parent_node not in tree_keys or tree_keys==[]:
            temp_list=[]
            for curr in temp_list_bfirst:
                
                #print var_check
#                 print "current node :"+ str(var_check)
#                 print "current element :"+ str(curr)
                for elem_combine in combined_allpoints:
                    for k in xrange(len(elem_combine)-1):
                        zipped_bfirst.append(zip(elem_combine[k],elem_combine[k+1]))
                    result = pathIntersectsAnyLines(parent_node,curr,zipped_bfirst)
                    if result == True:
                        break
                    else:
                        continue    
#                 print result
                    #temp_dist = distance(bfirst_startPoint,curr)
                if result == False  and curr!= goalPoint:
                        #if distance_check == 0 or temp_dist< distance_check:
                        if curr not in temp_list:
                            temp_list.append(curr)
                        if curr not in constant_list:
                            constant_list.append(curr)
                elif result ==False and curr == goalPoint:
                        end= True
                        tree_dictionary.update({tuple(parent_node):curr})
                        
                        break
                var_check=var_check+1
            if   temp_list!=[] and end==False:
                tree_dictionary.update({tuple(parent_node):temp_list})
                path_array.append(parent_node)
                parent_node=temp_list[0]
            elif temp_list!=[] and end == True:
                tree_dictionary.update({tuple(parent_node):temp_list})
                path_array.append(parent_node)
                parent_node=[] 
            elif temp_list==[]and end ==False:
                path_array.remove(parent_node)
                for k,v in tree_dictionary.iteritems():
                    if parent_node==v or parent_node in v:
                        last_node_checked=parent_node
                        parent_node= k
                        
            elif temp_list==[] and end== True:
                path_array.append(parent_node)
                break 
            for x in temp_list:
                temp_list_bfirst.remove(x)
   
    return path_array
def Astarsearch(listofMidPoints,startPoint,goalPoint,combined_allpoints):
    
    var_check=1
    tree_dictionary={}
    zipped_bfirst=[]
    path_array = []
    path_array.append(startPoint)
    temp_list_bfirst= copy.deepcopy(listofMidPoints)
    temp_list_bfirst.append(goalPoint)
    end= False
    parent_node=copy.deepcopy(startPoint)
    last_node_checked=[]
    list_of_children=[]
    distancefromStart=0
    gn=0
    fn=0
    hn=0
    while parent_node:
        constant_list=[]
        tree_keys=[]
#         bfirst_startPoint=copy.deepcopy(parent_node)
        if tree_dictionary.has_key(tuple(parent_node)) and list_of_children==[]:
            list_of_children= tree_dictionary.get(parent_node)
        if list_of_children!=[] and last_node_checked!=[]:
            list_of_children.remove(last_node_checked)
            parent_node=list_of_children[0]
        tree_keys= tree_dictionary.keys()
        if parent_node not in tree_keys or tree_keys==[]:
            temp_list=[]
            for curr in temp_list_bfirst:
                
                #print var_check
#                 print "current node :"+ str(var_check)
#                 print "current element :"+ str(curr)
                for elem_combine in combined_allpoints:
                    for k in xrange(len(elem_combine)-1):
                        zipped_bfirst.append(zip(elem_combine[k],elem_combine[k+1]))
                    result = pathIntersectsAnyLines(parent_node,curr,zipped_bfirst)
                    
                    if result == True:
                        break
                    else:
                        continue    
#                 print result
                    #temp_dist = distance(bfirst_startPoint,curr)
                if result == False  and curr!= goalPoint:
                        #if distance_check == 0 or temp_dist< distance_check:
                        if curr not in temp_list:
                            temp_list.append(curr)
                        if curr not in constant_list:
                            constant_list.append(curr)
                elif result ==False and curr == goalPoint:
                        end= True
                        tree_dictionary.update({tuple(parent_node):curr})
                        
                        break
                
                    
                var_check=var_check+1
            if   temp_list!=[] and end==False:
                tree_dictionary.update({tuple(parent_node):temp_list})
                for elem in temp_list:
                    node_to_append=[]
                    gn = distancefromStart+ distance(parent_node,elem)
                    fn = distance(goalPoint,elem)
                    hn_new=fn+gn
                    if hn==0 or hn_new<hn:
                        distancefromStart= distance(parent_node,elem)
                        node_to_append=elem
                path_array.append(node_to_append)
                parent_node = node_to_append
            elif temp_list!=[] and end == True:
                tree_dictionary.update({tuple(parent_node):temp_list})
                path_array.append(parent_node)
                parent_node=[] 
            elif temp_list==[]and end ==False:
                path_array.remove(parent_node)
                for k,v in tree_dictionary.iteritems():
                    if parent_node==v or parent_node in v:
                        last_node_checked=parent_node
                        parent_node= k
                        
            elif temp_list==[] and end== True:
                path_array.append(parent_node)
                break 
            for x in temp_list:
                temp_list_bfirst.remove(x)
    
    return path_array                                         
      
             
if __name__ == '__main__':
    list1= read("big_triangles")
    list2=read("square_in_the_middle")
    list3= read("triangle_in_the_middle")
    combined_allpoints= extractallPoints(list1)
    startPoint= [combined_allpoints[0],combined_allpoints[1]]
    goalPoint = [combined_allpoints[2],combined_allpoints[3]]
    #temp = combined_allpoints[0:4]
    combined_allpoints[0:4]=[]
    
    listofMidPoints= traverseMidPoints(combined_allpoints)
    listofMidPoints[0:4]=[]
    #lists_depth= []
    #called=1
    count=(goalPoint[0]-startPoint[0])/2 -1
    #while called <= count:
        #lists_depth.append(depthList(listofMidPoints,startPoint,goalPoint,called))
        #called =called+1
    #print lists_depth
    path_breadthFirst = breadthFirstSearch(listofMidPoints,startPoint,goalPoint,combined_allpoints)
    print " path accprding to breadth first search is "
    path_breadthFirst.reverse()
    print path_breadthFirst
    #seconddepthList= depthList(listofMidPoints,startPoint,goalPoint,called+1)
    path_depthFirst= depthFirstSearch(listofMidPoints,startPoint,goalPoint,combined_allpoints)
    path_depthFirst.append(goalPoint)
    print "path according to depth first"
    print path_depthFirst
    path_astar = Astarsearch(listofMidPoints,startPoint,goalPoint,combined_allpoints)
    path_astar.append(goalPoint)
    print "path after Astar search is "
    print path_astar