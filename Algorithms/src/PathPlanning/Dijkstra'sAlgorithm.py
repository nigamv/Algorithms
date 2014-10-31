'''
Created on May 24, 2014

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

def dijkstrasAlgorithm(startPoint,goalPoint,listofMidPoints):
    distance_dict={}
    dijkstra_Path=[]
    dijkstra_Path.append(startPoint)
    lines =[]
    print " length of list of mid points is:"+ str(len(listofMidPoints))
    for k in xrange(len(listofMidPoints)-1):
        i=k+1
        while i<= len(listofMidPoints)-1:
            lines.append(zip(listofMidPoints[k],listofMidPoints[i]))
            i+=1
    distanceFromStart=0
    path_visited=[]
    key_notallowed = [startPoint,goalPoint]
    
    while True:
        print " start point is"+str(startPoint)
        if startPoint in listofMidPoints:
            listofMidPoints.remove(startPoint)
        if not listofMidPoints:
            break
        for point in listofMidPoints:
            temp_dijkstra_Path = copy.deepcopy(dijkstra_Path)
#             result = pathIntersectsAnyLines(startPoint, point, lines)
#             if result:
#                 continue
            dist_bw_points = distanceFromStart + distance(startPoint,point)
            temp_dijkstra_Path.append(point)
            curr_Point_Used = False
            for key in distance_dict.keys():
                list_key = list(key)
                if point == list_key[len(list_key)-1]:
                    value = distance_dict.get(key)
                    if dist_bw_points < value and temp_dijkstra_Path != key_notallowed:
                        distance_dict.pop(key) 
                        distance_dict.update({tuple(temp_dijkstra_Path):dist_bw_points})
                        curr_Point_Used = True
                        break
            if not curr_Point_Used and temp_dijkstra_Path != key_notallowed:
                distance_dict.update({tuple(temp_dijkstra_Path):dist_bw_points})
        
        values_dict = sorted(distance_dict.values())
        index =0
        path_Changed=False
        while True:
            value = values_dict[index]
            for key, values in distance_dict.iteritems():
                if values == value and key not in path_visited:
                    dijkstra_Path = list(key)
                    distanceFromStart = value
                    path_Changed=True
                    break
            if path_Changed:
                break
            index+=1
                
        startPoint = dijkstra_Path[len(dijkstra_Path)-1]
        if startPoint == goalPoint:
            break
        path_visited.append(tuple(dijkstra_Path))  
    print "Path found by Dijkstra is :" + str(dijkstra_Path)    
        
            
        
    
if __name__ == '__main__':
    list1= read("big_triangles")
    list2=read("square_in_the_middle")
    list3= read("triangle_in_the_middle")
    combined_allpoints= extractallPoints(list1)
    startPoint= (combined_allpoints[0],combined_allpoints[1])
    goalPoint = (combined_allpoints[2],combined_allpoints[3])
    combined_allpoints[0:4]=[]
    listofMidPoints= traverseMidPoints(combined_allpoints)
    temp_list = [(-5,-5),(-5,5),(5,5),(5,-5)]
    for elem in temp_list:
        if elem in listofMidPoints:
            listofMidPoints.remove(elem)
    if startPoint not in listofMidPoints:
        listofMidPoints.append(startPoint)
    if goalPoint not in listofMidPoints:
        listofMidPoints.append(goalPoint)
    
    dijkstrasAlgorithm(startPoint,goalPoint,listofMidPoints)