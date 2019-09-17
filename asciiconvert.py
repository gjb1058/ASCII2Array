import os
import sys

print(sys.argv[1])

if os.path.exists(sys.argv[1]):
    try:
        with open(sys.argv[1], 'r') as i:
            lines = i.readlines()
        rows = 0
        cols = 0
        colsMAX = cols
        for line in lines:
            for char in line:
                if char != '\n':
                    print(char)
                    cols = cols+1
            if (cols>colsMAX):
                colsMAX=cols
            cols = 0
            rows = rows+1

        cols=colsMAX
        print("SIZE: "+str(rows)+" by "+ str(cols))
        rows = rows-1
        cols = cols-1
        command = "char art["+str(rows)+"]["+str(cols)+"] = { \n "
        print(command)
        count = 0
        for line in lines:
            command1="{ "
            for char in line:
                if char != '\n':
                    command1+="'"+str(char)+"' , "
                    count+=1
                else:
                    if count < cols:
                        while(count<cols):
                            command1+="' ' , "
                            count+=1
            
            command1 = command1[:-3]
            command1+="} ,\n"
            count = 0
            print(command1)
    except Exception as e:
        print(e)

else:
    print("File not found")
