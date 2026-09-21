
import subprocess


hostname = subprocess.run(["hostname"],capture_output=True, text=True)
username = subprocess.run(["whoami"],capture_output=True, text=True)
files    = subprocess.run(["ls","-al"],capture_output=True, text=True)
uptime   = subprocess.run(["uptime"],capture_output=True, text=True)
disk     = subprocess.run(["df","-h"],capture_output=True, text=True)
disk_info = disk.stdout.split()
print (disk_info)
ram      = subprocess.run(["free","-h"],capture_output=True, text=True)

print ("========================== LİNUX SYSTEM CEHCKER ===========================")
print ("UserName:",username.stdout,"\nHostName:",hostname.stdout,"\nUpTime:",uptime.stdout,"\nRam:",ram.stdout,"\nDisk:",disk.stdout,"\nFiles:",files.stdout)
print ("============================================================================")
