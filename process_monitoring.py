import psutil
from datetime import datetime


trust_process_file='trust_process.txt' # file with a list of trust processes
log_file='log.txt' 
last_check_file='last_check.txt'

def extract_list(filename):
    # Returns a list of processes from file with a given filename
    # We use it for list of trust processes
    f = open(filename, "r")
    e_list=f.read().splitlines()
    f.close()
    return e_list

def check_current_process(t_list):
    # This fonction compares running processes with a list of trust processes (t_list)
    # It returns either an empty list, if everything is ok and each runnin process is in t_list,
    # or a 2D-list proc_list[][] which contains a suspect processes that haven't been found in t_list
    # proc_list[ [PID-s, process name, path] ] 
    proc_list = []
    for process in psutil.process_iter():
        if process.name() not in t_list: 
            p_flag=0
            # We will use p_flag to indicate whether the current process in already in our list or not
            # If the process in question is already in our list, then a new PID will just be added to others PID of the process
            # (each process name may have multiple PID-s)
            # Otherwise, a new row will be added to the proc_list table with process ID, it's name, and it's path
            for i in range(len(proc_list)):
                if process.name()==proc_list[i][1]:
                    proc_list[i][0]=proc_list[i][0]+' '+str(process.pid)
                    p_flag=1
                    break
            if p_flag==0:
                proc_list = proc_list+[[str(process.pid),process.name(),psutil.Process(process.pid).exe()]]
    return proc_list

def generate_alert(p_list):
    # generation of alert message containing the information about detected suspect processes: their PID, name and path
    # p_list contains the names of processes
    p_message="New processes detected! \n \n"
    for i in range(len(p_list)):
        p_message=p_message+"PID             : "
        #for j in range(len(p_list)):
        p_message=p_message+str(p_list[i][0])+"  " # There may be several PID number for a single process name
        p_message=p_message+" \n"
        p_message=p_message+"Name of process : "+p_list[i][1]+" \n"
        p_message=p_message+"Path            : "+p_list[i][2]+"\n\n\n" # I suppose that the the process with the same name don't have several pathes, so we search the path only for the first PID in the list
    return p_message

def add_to_logfile(f_log, f_lastcheck, logstring):
    # Adds a new entry to a log file
    f = open(f_log, "a") 
    f.write(str(datetime.now())+"\n"+logstring)
    f.close()

    f = open(f_lastcheck, "w") 
    f.write("Last check: "+str(datetime.now()))
    f.close()
    
trust_list=extract_list(trust_process_file)
suspect_process=check_current_process(trust_list)

if len(suspect_process)==0:
    print('OK')
else:
    message=generate_alert(suspect_process)
    print(message)
    add_to_logfile(log_file,last_check_file,message)


   

