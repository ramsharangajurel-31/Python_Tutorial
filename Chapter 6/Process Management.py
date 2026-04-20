import os
# get process id
pid=os.getpid()
print("PID:",pid)

# get parent process id
ppid=os.getppid()
print("PPID:",ppid)