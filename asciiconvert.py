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
        for line in lines:
            command1="{ "
            for char in line:
                if char != '\n':
                    command1+="'"+str(char)+"' , "
            command1+="} ,\n"
            print(command1)
    except Exception as e:
        print(e)

else:
    print("File not found")
