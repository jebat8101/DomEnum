#!/usr/bin/env python
import sys
import subprocess

subprocess.run(["sudo python3 /home/najum98/Documents/MyTools/OneForAll/oneforall.py --takeover --target "+str(sys.argv[1])+" --path "+sys.argv[1]+"-oneforall.txt run"],shell=True,text=True)
subprocess.run(["subfinder -d "+sys.argv[1] +" -o "+sys.argv[1]+"-subfinder.txt"],shell=True)
subprocess.run(["amass enum -d "+sys.argv[1]+" -o "+sys.argv[1]+"-amass.txt"],shell=True)
subprocess.run(["amass track -d "+sys.argv[1]],shell=True)

lines_seen = set()
filenames = [sys.argv[1]+'-oneforall.txt', sys.argv[1]+"-subfinder.txt",sys.argv[1]+"-amass.txt"]   
with open(sys.argv[1]+'.txt', 'w') as outfile: 
    for names in filenames: 
        with open(names) as infile: 
            outfile.write(infile.read()) 
        outfile.write("\n")

with open(sys.argv[1]+'-unique.txt', "w") as output_file:
    count=0
    for each_line in open(sys.argv[1]+'.txt',"r"):
        if each_line[0:4]!="www.":
            if each_line not in lines_seen:
                output_file.write(each_line)
                lines_seen.add(each_line)
        else:
            if each_line[4:] not in lines_seen:
                output_file.write(each_line[4:])
                lines_seen.add(each_line[4:])
        count+=1
    print("Total lines in "+sys.argv[1]+".txt are "+str(count))
subprocess.run(["cat "+sys.argv[1]+"-unique.txt | httprobe >"+sys.argv[1]+"-httprobed.txt"],shell=True)
subprocess.run(["cat "+sys.argv[1]+"-httprobed.txt | /home/najum98/Documents/MyTools/aquatone_linux_amd64_1.7.0/aquatone -out "+sys.argv[1]],shell=True)
