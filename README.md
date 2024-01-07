A Python script for system processes monitoring. It can be used by monitoring systems such as Zabbix, or as a system service.

It uses psutil library, so make sure it's installed before using the script. 

The principle is simple: there's a list of "good" processes and the program verifies if all of running processes are in that list. By default, it's stored in trust_process.txt. Here's an example of such a file.
If some unknown processes are discovered after verification, the script generates a message with a name of each unknown process, it's PIDs and it's path. This information is also written to the log file (by default log.txt).
Otherwise, there will be terminated with "OK" message.

A list of currently running processes can be generated as a base with generate_process_list.py script.You can also add or delete manually the "good" processes.
The date and time of last verification are stored in another file (last_check.txt by default).

The script can be adapted to your needs: you can integrate it to your monitoring system, run it as a system service, add email notificaitons, configure an automatic remove of unknown processes, etc.
