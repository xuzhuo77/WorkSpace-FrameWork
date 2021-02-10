



m=[[1,0],[0,1]]

d=[]
for row in m:
    d.append(row)
    d.append(row)

print(d)

md = {0: "  ",
      1: "##",
      2: "XX"}
for row in d:
    s = ''
    for entry in row:

        s += md[entry]
    print(s)