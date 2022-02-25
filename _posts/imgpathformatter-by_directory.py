import sys


if len(sys.argv) != 2:
    print("Insufficient arguments")
    sys.exit()


directory_path = sys.argv[1]


print("Directory path : " + directory_path)

f= open(file_path, 'r')
lines  = f.readlines()

with open(file_path,'w') as f:
    for line in lines:
        if "![Untitled]" in line:
            object = line.split("(")
            # f.write(object[0] + "(/assets/img/" + object[1][:-1] + '{: width="70%" height="70%"}'+'{:.aligncenter}\n')
            f.write(object[0] + "(./../.." + object[1][:-1] )
        else:
            f.write(line)

