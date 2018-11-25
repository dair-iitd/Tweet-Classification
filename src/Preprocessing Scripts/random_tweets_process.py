import io
import sys
import random
infile=sys.argv[1]
outfile=sys.argv[2]
strings=[]
with io.open(infile,encoding='utf-8') as infile:
	i=0
	for line in infile:
		if not(i%4==3): 
			i+=1
			continue
		i+=1
		a=line.split("\t")
		b=""
		for j in range(1,len(a)):
			if j>1:
				b+=" "
			b+=a[j]
		strings.append(str(b.encode('ascii','ignore')))
random.shuffle(strings)
f=io.open(outfile,"w")
for i in range(0,12000):
	f.write(strings[i]+"\n")
f.close()