




import os
w=['0','1','2','3','4','5','6','7','8','9']


file_name=os.listdir("E:\Full-Stack Track - One Million Arab Coders\prank")
new_file_name=[]
os.chdir("E:\Full-Stack Track - One Million Arab Coders\prank")
print (os.getcwd())
for i in file_name:
    file =""
    for j in i :
        if j in w:
            file+=""
        else:
            file+=j
    os.rename(i,file)
    new_file_name.append(file)


print(new_file_name)