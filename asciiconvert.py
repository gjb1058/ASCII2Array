# File  : asciiconvert.py
# Author: Grant J. Bierly (gjb1058)
# Date  : 09/17/2019

import os
import sys

# If the length is 3, then there is a custom name at the end.
if len(sys.argv) == 3:
    name = sys.argv[2]
else:
    name = "art"

# If the file exists
if os.path.exists(sys.argv[1]):
    try:
        with open(sys.argv[1], 'r') as i:
            lines = i.readlines()
        rows = 0
        cols = 0
        colsMAX = cols

        #Count the length of each line to get the max
        for line in lines:
            for char in line:
                if char != '\n':
                    cols = cols+1
            if (cols>colsMAX):
                colsMAX=cols
            cols = 0
            rows = rows+1

        cols=colsMAX
        #Inform the user of the size.
        print("SIZE: "+str(rows)+" by "+ str(cols))
        rows = rows-1
        cols = cols-1
        #Convert to C arrays, which start at 0.
        #Then, print the array declaration.
        command = "char "+name+"["+str(rows)+"]["+str(cols)+"] = { \n "
        print(command)
        #First line printed.
        count = 0
        #Iterate though each line and add it to the command1 string in C format
        for line in lines:
            command1="{ "
            for char in line:
                if char != '\n':
                    command1+="'"+str(char)+"' , "
                    count+=1
                else:
                    #If we're not at the max yet, add spaces.
                    #If it's a \n, then we move on.
                    if count < cols:
                        while(count<cols):
                            command1+="' ' , "
                            count+=1
            #Cut off the extra commam then add the end of the line.
            command1 = command1[:-3]
            command1+="} ,\n"
            count = 0
            #print the line.
            print(command1)
        #print the end.
        print("};")

        #Now we're done!
    except Exception as e:
        print(e)

else:
    print("File not found")
