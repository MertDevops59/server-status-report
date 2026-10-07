
import subprocess

def run_cmd(komut):
    result = subprocess.run (komut, capture_output=True, text=True)
    return result.stdout.strip()

hostname = run_cmd(["hostname"])
username = run_cmd(["whoami"])
files    = run_cmd(["ls","-al"])
uptime   = run_cmd(["uptime"])
disk     = run_cmd(["df","-h"])


ram      = run_cmd(["free","-h"])

print ("========================== LİNUX SYSTEM CEHCKER ===========================")
print ("UserName:",username,"\nHostName:",hostname,"\nUpTime:",uptime,"\nRam:",ram,"\nDisk:",disk,"\nFiles:",files)
print ("============================================================================")
