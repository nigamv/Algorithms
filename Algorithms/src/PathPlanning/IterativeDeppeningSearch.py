'''
Created on Feb 24, 2014

@author: user
'''

'''
Created on Feb 17, 2014

@author: user
'''
import copy

def eightPuzzleDemo(startState,goalState):
    limit=1
    max_limit=6
    tree_dict={}
    result = False
    while limit <=max_limit:
        result=depthLimitedSearch(startState,goalState,limit,tree_dict)
        if result== True:
            break  
        limit=limit+1 
    if result== False:
        print "solution not found at given depths" 

def depthLimitedSearch(startState,goalState,limit,tree_dict):
    print " Checking for depth:"+str(limit)
    local_limit=0
    nodes_visited=[]
    if startState == goalState:
        print " Goal State reached at depth:" +str(limit)
        return True
    
    print "Transition states taken:"
    print startState
    nodes_visited.append(startState)
    local_limit+=1
    depth_reached= False
    curr_startState= copy.deepcopy(startState)
    allnodes_visited= False
    
    limit_check = 1
    while True:
        
        if limit == 1:
            break
        value_found =False
        loop =True
        
        while loop:
            curr_valuePicked= False
            curr_startState_key =[]
            curr_startState_key =tuple(curr_startState)
            values = tree_dict.get(curr_startState_key)
            if not values:
                break
            for value in values:
                if value not in nodes_visited:
                    if local_limit == limit:
                        value_found = True
                        break
                    
                    elif not curr_valuePicked:
                        curr_startState = value
                        print curr_startState
                        local_limit+=1
                        curr_valuePicked= True
                        break
                    else:
                        break
                
            if value_found:
                break
            if not value_found and (curr_startState == tuple(startState) or curr_startState == startState):
                allnodes_visited = True
                break
            if not value_found and limit_check == limit:
                for keys,values in tree_dict.iteritems():
                    if curr_startState in values and curr_startState in nodes_visited:
                        curr_startState = list(keys)
                        local_limit-=1
                        limit_check = local_limit
                        break
            limit_check+=1 
            if curr_startState not in nodes_visited:
                nodes_visited.append(curr_startState)
        if allnodes_visited:
            break
            
        pos =0
        for i in xrange(curr_startState.__len__()):
            if curr_startState[i]==0:
                pos=i
                break 
        availablePos=[]          
        if pos==0:
            availablePos=[3,1]
        elif pos==1:
            availablePos=[4,2,0]
        elif pos==2:
            availablePos=[5,1]
        elif pos==3:
            availablePos=[6,4,0]
        elif pos==4:
            availablePos=[7,5,1,3]
        elif pos==5:
            availablePos=[8,2,4]
        elif pos==6:
            availablePos=[7,3]
        elif pos==7:
            availablePos=[8,4,6]
        elif pos==8:
            availablePos=[5,7]
        
        children_generated =[]    
        for x in availablePos:
            temp_currState = copy.deepcopy(curr_startState)
            if curr_startState[x]!=x:
                temp= temp_currState[x]
                temp_currState[x]= temp_currState[pos]
                temp_currState[pos]= temp
            if temp_currState == goalState:
                print " Goal state reached at depth:" + str(limit)
                print "Goal state is:" + str(temp_currState)
                depth_reached = True
                break
            elif temp_currState != curr_startState and temp_currState not in nodes_visited:
                print temp_currState
                nodes_visited.append(temp_currState)
                children_generated.append(temp_currState)
        
        if depth_reached:
            break
#         curr_startState_key=[]
#         curr_startState_key = tuple(curr_startState)
        if children_generated:
            tree_dict.update({curr_startState_key:children_generated})
        local_limit+=1
        for keys,values in tree_dict.iteritems():
            if curr_startState in values:
                curr_startState = list(keys)
                local_limit -=2
                limit_check = local_limit
                break
               
        
        
    if not depth_reached:
        print " Solution not found till depth:"+ str(limit)     
            


           
if __name__ == '__main__':
    startState = [1,0,5,3,2,4,6,7,8]
    goalState = [0,1,2,3,4,5,6,7,8]
    eightPuzzleDemo(startState,goalState)
            
