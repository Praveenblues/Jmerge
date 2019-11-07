import sys
import os
import json


def Merge(path,inp_basename,out_basename,max_size):
    outdata={}
    filecount=0
    outcounter=1
    namearray=[]

    allfiles=os.listdir(path)
    for file in allfiles:
        if((file.startswith(inp_basename)) and (file.split('.')[1]=='json')):       #Checking whether it is a .json file
            namearray.append(file.split('.')[0])
    sortednamearray = sorted(tuple(namearray))                                      #Sorting Json file names in ascending order

    for name in sortednamearray:
        fname=path+"\\"+name+'.json'
        with open(fname, "r") as read_file:
            dat = json.load(read_file)
            title=list(dat.keys())[0]                                               #Getting the root key

            if(filecount==0):
                outdata[title] = []
                if(not os.path.isfile(path+"\\"+out_basename+str(outcounter)+'.json')):
                    with open(path+"\\"+out_basename+str(outcounter)+'.json', 'w') as outfile:
                        json.dump(outdata, outfile)                                                             #Creating empty Json file
            
            for p in dat[title]:
                    outdata[title].append(p)
                    with open(path+"\\"+out_basename+str(outcounter)+'.json', 'w') as outfile:
                        json.dump(outdata, outfile)
                        
                    try:
                        if(os.stat(path+"/"+out_basename+str(outcounter)+'.json').st_size>max_size):            #Checking file size
                            print("Size exceeded, Creating new file...")
                            newoutdata={}
                            outdata[title].pop()
                            newoutdata[title] = outdata[title]
                            with open(path+"\\"+out_basename+str(outcounter)+'.json', 'w') as outfile:
                                json.dump(newoutdata, outfile)                                                  #Taking back the most recent data
                                
                            outcounter+=1
                            outdata[title]=[]
                            outdata[title].append(p)
                    except FileNotFoundError:
                        print("File not found")
##        print(outdata)
        
        filecount+=1

    if(not os.path.isfile(path+"\\"+out_basename+str(outcounter+1)+'.json')):                                   
        with open(path+"\\"+out_basename+str(outcounter)+'.json', 'w') as outfile:
            json.dump(outdata, outfile)                                                                         #Appending the remaining data to the output file

path=input()
prefix=input()
outprefix=input()
limit=int(input())
Merge(path,prefix,outprefix,limit)
##Merge('Jfolder','data','out',150)

