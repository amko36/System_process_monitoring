import psutil

filename="trust_process.txt"

f = open(filename, "w")
process_list=[]
for process in psutil.process_iter():
    if process.name() not in process_list:
        f.write(process.name()+'\n')
        process_list=process_list+[process.name()]
f.close()

