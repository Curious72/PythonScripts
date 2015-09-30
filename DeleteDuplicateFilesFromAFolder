import os
path='put the path of the folder here' // using pwd ,u can find the path of the folder 
l=list()
for file in os.listdir(path):
	if file.endswith("type of extension"): //for example ".txt"
		f=open(file,"r")
		l.append(f.read())
t=len(l)
r=[0]*t
for i in range(0,t-1):
	if(r[i]==0):
		for j in range(i+1,t):
			if(l[i] == l[j]):
				print l[j]
				r[j]=1

y=0

for file in os.listdir(path):
	if file.endswith("type of extension"):   // for example ".txt"
		if(r[y]==1):
			print file
			os.remove(file)
			
		y=y+1






