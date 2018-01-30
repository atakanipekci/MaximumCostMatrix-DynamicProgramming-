#This function finds the maximum amount of money you can
#steal from a given matrix where each element represents
#a land piece with money hidden in it. You can only start
#from the first column and each time you move you have to
#move towards right. This means that you can only go 1
#element right,right-up or right-down. This is basically a
#maximum cost question. I will use the term cost instead of
#money/steal to explain the further details. First of all
#it is obvious that the cost of reaching a cell on first
#column is only its own cost since we can start in any row
#we want. We will find the cost of all other cells using these
#values so we have to first create a new 2d array and assign
#the corresponding elements to its first column. Note that
#this takes O(R) amount of time where R is the total number of
#rows. After that we will keep finding the costs of other cells
#starting from col 1 row 0 to col 1 row 1 col 1 row 2 ... to
#col C-1 row R-1(C is the total number of columns and since it
#is an array the starting index is 0). The movement restrictions
#come in handy here. Since we can only move towards right we only
#have to check the costs of the previous column. And since we can move
#1 cell at a time we only have to compare [j][i-1],[j+1][i-1] and
#[j-1][i-1]( where i is the current column and j is the current row)
#to find the max cost of getting to the desired cell.
#Of course we also have to add the cost of the desired cell also.
#As you can see the column value is always the same:i-1 since
#we can only approach from the left column. But since we can also
#go right-down and right-up we have to check the other rows on that
#column also. The important part here is that you shouldn't forget
#that there are some exceptions. For example if we are finding the costs
#for row no 0, then there is no element that can reach it by going right-down.
#Also if we are finding the costs for last row, then there is no element
#that can reach it by going right-up. So we need to check these conditions
#while calculating. After we are done finding all the cost values we only
#have to find the maximum element on the last column. We do that by comparing
#every element on last column which takes O(R) amount of time.
#And finally the total time complexity for worst case is
#O(R+R+(C-1)*R)=O(2R+CR-R)=O(CR).



def theft(matrix):
    noOfRows=len(matrix)
    noOfColumns=len(matrix[0]) 
    result=0

    costMatrix = [[0 for x in range(noOfColumns)] for y in range(noOfRows)]
    
    i=0
    while(i<noOfRows):
        costMatrix[i][0]=matrix[i][0]
        #print(costMatrix[i][0])
        i+=1
    
    i=1
    while(i<noOfColumns):
        j=0
        while(j<noOfRows):
            
            if(j==0):
                costMatrix[j][i]=max(costMatrix[j][i-1],costMatrix[j+1][i-1])+matrix[j][i]
            elif(j+1<noOfRows):
                costMatrix[j][i]=max(costMatrix[j][i-1],costMatrix[j+1][i-1],costMatrix[j-1][i-1])+matrix[j][i]
            else:
                costMatrix[j][i]=max(costMatrix[j][i-1],costMatrix[j-1][i-1])+matrix[j][i]
                
            j+=1
        i+=1
    #print(costMatrix)
        
    i=noOfColumns-1
    j=0
    
    while(j<noOfRows):
        if(costMatrix[j][i]>result):
            result=costMatrix[j][i]
        j+=1
    
    return result
        
    
    
#amountOfMoneyInLand= [[1,3,1,5], [2,2,4,1], [5,0,2,3], [0,6,1,2]]

#print(len(amountOfMoneyInLand[0]))

#theft(amountOfMoneyInLand)


amountOfMoneyInLand= [[1,3,1,5], [2,2,4,1], [5,0,2,3], [0,6,1,2]]
res = theft(amountOfMoneyInLand)
print(res)
#Output: 16
amountOfMoneyInLand= [[10,33,13,15], [22,21,4,1], [5,0,2,3], [0,6,14,2]]
res = theft(amountOfMoneyInLand)
print(res)
#Output: 83