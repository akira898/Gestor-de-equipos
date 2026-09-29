
import os
def checkFile(check):
    check=os.path.join(check+".txt")
    if os.path.exists(check):
        with open(check,"r",encoding="utf-8") as c:
            lines=c.read().splitlines()
            for line in lines:
               print(line)
    else:
        print("File not found")
        with open(check,"w") as c:
            c.write("group")