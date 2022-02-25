import sys


if len(sys.argv) != 2:
    print("Insufficient arguments")
    sys.exit()


file_path = sys.argv[1]


print("File path : " + file_path)

f= open(file_path, 'r')
lines  = f.readlines()

with open(file_path,'w') as f:
    for line in lines:
        if "<img src=" in line:
            object = line.split('src="')
            # f.write(object[0] + "(/assets/img/" + object[1][:-1] + '{: width="70%" height="70%"}'+'{:.aligncenter}\n')
            f.write(object[0] + 'src="./' + object[1][:-1] )
        else:
            f.write(line)

